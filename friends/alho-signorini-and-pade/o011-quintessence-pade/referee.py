"""Independent referee. Run ONLY on the pod. Imports no claimant code.

Exact series uses source (52) in H=3q*tildephi, A=u/sqrtq, B=v/sqrtq.
Numerical reference uses the kinetic/potential variables from Friedmann+KG.
Claimant JSON is treated solely as proposed coefficients to compare.
"""
import json, math, os, time
from fractions import Fraction as F
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq, minimize_scalar
from numpy.polynomial.polynomial import polyval

ROOT=os.path.dirname(os.path.abspath(__file__))

def add(a,b):
    n=max(len(a),len(b)); return [(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(n)]
def scale(a,s): return [s*v for v in a]
def mul(a,b,n):
    c=[F(0)]*(n+1)
    for i in range(min(len(a),n+1)):
        for j in range(min(len(b),n+1-i)): c[i+j]+=a[i]*b[j]
    return c

def series(p,n=12):
    q=p/(p+2); k=6/(p+2)
    H=[F(0)]*(n+1); A=[F(0)]*(n+1); B=A.copy()
    H[1]=A[0]=B[0]=F(1)
    for j in range(1,n+1):
        if j>1: H[j]=k*mul(mul(A,B,j),H,j)[j]/(k*(j-1))
        aa=mul(A,A,j); bb=mul(B,B,j)
        rhsA=scale(mul(add([F(2)],scale(aa,-q)),add(B,scale(A,-1)),j),F(3,2))
        rhsB=scale(mul(add(mul(add([F(1)],scale(aa,-q)),add([F(1)],scale(mul(bb,H,j),-1)),j),scale(mul(A,B,j),-2*q/p)),B,j),F(3,2))
        # Jacobian in A,B at H=0,A=B=1, solved explicitly as a 2x2 system.
        c=F(3,2)*(2-q)
        jaa=-c; jab=c; jba=-3*q*(1+1/p); jbb=-3*q/p
        d1=k*j-jaa; d2=-jab; d3=-jba; d4=k*j-jbb
        det=d1*d4-d2*d3
        A[j]=(rhsA[j]*d4-d2*rhsB[j])/det
        B[j]=(d1*rhsB[j]-d3*rhsA[j])/det
    w=add(scale(mul(A,A,n),q),[F(-1)])
    x=mul(mul(B,B,n),H,n)
    return {'A':A,'B':B,'Omega':x,'w':w,'H':H}

def pade(w,d):
    # exact rational Gaussian elimination, denominator constant normalized to 1.
    M=[[w[d+1+i-j] for j in range(1,d+1)]+[-w[d+1+i]] for i in range(d)]
    for j in range(d):
        pivot=next(i for i in range(j,d) if M[i][j]); M[j],M[pivot]=M[pivot],M[j]
        v=M[j][j]; M[j]=[x/v for x in M[j]]
        for i in range(d):
            if i!=j:
                v=M[i][j]; M[i]=[a-v*b for a,b in zip(M[i],M[j])]
    Q=[F(1)]+[M[i][-1] for i in range(d)]
    P=mul(w,Q,d)
    assert all(v==0 for v in mul(w,Q,2*d)[d+1:])
    return P,Q

def kg_reference(p,eps,tol):
    # X=phidot/(sqrt6 H), Y=sqrtV/(sqrt3 H), ell=log(lambda).
    # This is obtained directly from KG, Friedmann and dust conservation.
    q=p/(p+2)
    initial=[math.sqrt(q*eps/2), math.sqrt((2-q)*eps/2), .5*math.log(3*q/eps),0.]
    def rhs(n,s):
        X,Y,ell,lnE=s; lam=math.exp(ell); h=-1.5*(1+X*X-Y*Y)
        return [-3*X+math.sqrt(1.5)*lam*Y*Y-X*h,
                -math.sqrt(1.5)*lam*X*Y-Y*h,
                -math.sqrt(6)*X*lam/p,h]
    def hit(n,s): return s[0]**2+s[1]**2-.68
    hit.terminal=True; hit.direction=1
    sol=solve_ivp(rhs,(0,40),initial,events=hit,method='DOP853',rtol=tol,atol=tol*1e-6,dense_output=True,max_step=.04)
    assert sol.success and len(sol.t_events[0])==1
    present=sol.t_events[0][0]; lnE0=sol.sol(present)[3]
    def sample(N):
        X,Y,ell,lE=sol.sol(present+N); x=X*X+Y*Y; w=(X*X-Y*Y)/x
        return 1-x,np.exp(lE-lnE0),w
    state=sol.sol(present); X,Y,ell,_=state
    dn=rhs(present,state); xp=2*X*dn[0]+2*Y*dn[1]
    wp=(2*X*dn[0]-2*Y*dn[1]-(X*X-Y*Y)*xp/.68)/.68
    return sample,{'w0':float(sample(0)[2]),'wa':float(-wp),'steps':len(sol.t),'present':present}

def maxerr(fn,ref):
    N=np.linspace(-math.log(7),0,20001); om,E,w=ref(N); a=fn(N)
    signed=a/om-1
    def e(n): return abs(float(fn(n)/ref(n)[0]-1))
    # Refine every sampled local maximum, retaining endpoints.
    ix=np.flatnonzero((np.abs(signed[1:-1])>=np.abs(signed[:-2]))&(np.abs(signed[1:-1])>=np.abs(signed[2:])))+1
    vals=[(e(N[0]),N[0]),(e(0.),0.)]
    for i in ix:
        r=minimize_scalar(lambda n:-e(n),bounds=(N[i-1],N[i+1]),method='bounded',options={'xatol':1e-13})
        vals.append((-r.fun,r.x))
    err,n=max(vals); erat=math.sqrt(float(ref(n)[0]/fn(n)))
    # Independent E reference includes integration of Raychaudhuri, not dust identity.
    Ec=np.sqrt(.32*np.exp(-3*N)/a)
    Eerr=np.max(np.abs(Ec/E-1))
    return {'Omega_m_relative_max_float':err,'E_relative_max_float':float(Eerr),'z_at_Omega_max':math.expm1(-n)}

def run(pstr):
    t=time.time(); p=F(pstr); pf=float(p); wi=float(-2/(p+2)); k=-3*wi
    S=series(p)
    claim=json.load(open(os.path.join(ROOT,'input','attempt1_p'+('1.0' if p==1 else '0.1')+'.json')))
    assert all(S[name]==list(map(F,claim['series'][name])) for name in ['A','B','Omega','w'])
    print('Exact independent source-series matches',pstr,flush=True)
    refs=[]; diagnostics=[]
    for eps,tol in [(1e-8,2e-11),(1e-10,2e-13),(1e-12,3e-14)]:
        ref,diag=kg_reference(pf,eps,tol); refs.append(ref); diagnostics.append(diag)
    ref=refs[-1]; N=np.linspace(-math.log(7),0,20001)
    convergence=[float(np.max(np.abs(r(N)[0]-ref(N)[0]))) for r in refs[:-1]]
    dust_diff=float(np.max(np.abs(ref(N)[1]**2*ref(N)[0]/(.32*np.exp(-3*N))-1)))
    gamma=1-(1-wi*wi)/(4*wi*wi-2*wi+1)
    beta=(36*wi**4-21*wi**3+7*wi*wi-1)/((4*wi*wi-2*wi+1)*(12*wi*wi-3*wi+1))
    Tpaper=.68/(1-.68*gamma)
    def paper(n):
        T=Tpaper*np.exp(k*n)
        R=2.125*np.exp(k*n)*((1+beta*Tpaper)/(1+beta*T))**((gamma-1)/beta)
        return 1/(1+R)
    results={'p':pstr,'exact_series_match':True,'kg_reference':diagnostics,'finite_start_convergence_abs_Omega':convergence,'dust_identity_relative_difference':dust_diff,'paper_11':maxerr(paper,ref),'pade':[]}
    for d in [1,2,6]:
        P,Q=pade(S['w'],d)
        if d>1:
            crow=next(r for r in claim['rows'] if r['degree']==d)
            assert P==list(map(F,crow['P'])) and Q==list(map(F,crow['Q']))
        pp=np.array(list(map(float,P))); qq=np.array(list(map(float,Q)))
        # Integral is evaluated as a rational function with its removable zero cancelled.
        ip=np.array([float(P[i]/F(wi).limit_denominator()-Q[i]) for i in range(1,d+1)])
        def logR(T): return np.log(T)+quad(lambda s:polyval(s,ip)/polyval(s,qq),0,float(T),epsabs=2e-13,epsrel=2e-13)[0]
        T0=brentq(lambda T:logR(T)-math.log(2.125),.1,3,xtol=1e-14)
        # Evolve continuity, which is independent of the true KG reference.
        def dr(n,s):
            T=T0*np.exp(k*n); return [-3*polyval(T,pp)/polyval(T,qq)]
        den=solve_ivp(dr,(0,-math.log(7)),[math.log(2.125)],method='DOP853',rtol=3e-14,atol=1e-15,dense_output=True,max_step=.01)
        def approx(n): return 1/(1+np.exp(den.sol(n)[0]))
        item={'degree':d,'T0_float':T0,'exact_pade_match':True,**maxerr(approx,ref)}
        results['pade'].append(item)
    for name,w in [('wCDM',wi),('LambdaCDM',-1)]:
        results[name]=maxerr(lambda n:1/(1+2.125*np.exp(-3*w*n)),ref)
    results['elapsed_s']=time.time()-t
    json.dump(results,open(os.path.join(ROOT,'numerical_'+pstr.replace('/','_')+'.json'),'w'),indent=2)
    print(json.dumps(results,indent=2),flush=True)

if __name__=='__main__':
    for ps in ['1','1/10']: run(ps)
