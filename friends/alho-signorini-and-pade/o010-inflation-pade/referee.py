"""Independent referee; no submitted executable code is read or imported.

Paper eqs 4,7,8 on Omega_m=0 imply, with s=-Sigma, t=tildeT:
 t_N=3*t*s*s/n, s_N=n*t*(1-s*s)**(1-1/(2*n))-3*s*(1-s*s).
The derivation and singular comparison are recorded separately in AUDIT.md.
All calculations in this file run on the shared pod.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json, sys, time
import mpmath as mp
import sympy as sy

sys.set_int_max_str_digits(100000)
mp.mp.dps=70

def trim(a):
    a=list(a)
    while len(a)>1 and not a[-1]: a.pop()
    return a
def add(a,b):
    return trim([(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(max(len(a),len(b)))])
def scale(a,c): return trim([x*c for x in a])
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)
def shift(a,k=1): return [F(0)]*k+list(a)
def diff(a): return [i*a[i] for i in range(1,len(a))] or [F(0)]
def value(a,x):
    y=F(0)
    for c in reversed(a): y=y*x+c
    return y
def positive(a,lo=F(0),hi=F(1,2),depth=0):
    """Exact Bernstein positivity after affine substitution; no sign sampling."""
    a=trim(a); d=len(a)-1
    b=[sum((a[j]*comb(j,k)*lo**(j-k)*(hi-lo)**k for j in range(k,d+1)),F(0)) for k in range(d+1)]
    bern=[sum((b[k]*F(comb(i,k),comb(d,k)) for k in range(i+1)),F(0)) for i in range(d+1)]
    if min(bern)>0: return 1
    assert depth<20, ('unproved positive',depth)
    mid=(lo+hi)/2
    return positive(a,lo,mid,depth+1)+positive(a,mid,hi,depth+1)
def strip_origin(a):
    k=0
    while k<len(a) and a[k]==0: k+=1
    assert k<len(a)
    return k,a[k:]

def inverse_series(n,K=24):
    """Coefficient recurrence from reduced ODE, independently expanded."""
    c=[F(1)]
    for k in range(1,K+1):
        v=sum((c[i]*c[k-1-i]/n for i in range(k)),F(0))
        v-=sum(((1+2*(k-i))*c[i]*c[k-i] for i in range(1,k)),F(0))
        v-=sum((2*(k-1-i)*c[i]*c[k-1-i] for i in range(1,k-1)),F(0))
        c.append(v)
    return c

def hj_series(n,K):
    """From 3H^2-2H_phi^2=V: F(F-1)=y(F-yF'/n)^2."""
    c=[F(1)]
    for k in range(1,K+1):
        v=sum(((1-F(i,n))*(1-F(k-1-i,n))*c[i]*c[k-1-i] for i in range(k)),F(0))
        v-=sum((c[i]*c[k-i] for i in range(1,k)),F(0))
        c.append(v)
    return c

def pade(c,m,d):
    if not d: return c[:m+1],[F(1)]
    A=sy.Matrix([[sy.Rational(c[k-j]) if k-j>=0 else 0 for j in range(1,d+1)] for k in range(m+1,m+d+1)])
    b=sy.Matrix([-sy.Rational(c[k]) for k in range(m+1,m+d+1)])
    q=[F(1)]+[F(x) for x in A.inv()*b]
    p=mul(c,q)[:m+1]
    return p,q

def check_row(row,n,c):
    p=list(map(F,row['P']));q=list(map(F,row['Q']))
    assert len(p)<=row['m']+1 and len(q)<=row['d']+1
    assert p[0]==q[0]==1
    match=add(mul(c,q),scale(p,-1))
    assert all(x==0 for x in match[:row['m']+row['d']+1])
    # Rational residual formed by direct polynomial clearing of reduced ODE.
    a=add(p,scale(q,-1)); b=add(mul(p,q),shift(scale(add(mul(diff(p),q),scale(mul(p,diff(q)),-1)),2)))
    term=mul(p,mul(add(scale(p,1+F(1,n)),scale(q,-1)),q))
    residual=add(mul([F(1),F(1)],mul(a,b)),scale(shift(term),-1))
    order,remainder=strip_origin(residual)
    sign=1 if row['kind']=='upper' else -1
    assert order==row['residual_zero_order']
    counts=[positive(p),positive(q),positive(a[1:]),positive(scale(remainder,sign))]
    mono=add(mul([F(1),F(1)],b),scale(shift(mul(p,q)),-F(n+1,n)))
    counts.append(positive(mono))
    endpoint=value(p,F(1,2))/value(q,F(1,2))
    assert endpoint==F(row['f_endpoint'])
    return endpoint, {'degree':[row['m'],row['d']],'kind':row['kind'],'residual_order':order,'positive_leaf_counts':counts}

def m(x): return mp.mpf(x.numerator)/x.denominator if isinstance(x,F) else mp.mpf(x)
def ev(a,x): return mp.polyval(list(map(m,reversed(a))),x)

def first_root(coeff):
    x=sy.Symbol('x')
    poly=sy.Poly.from_list(list(map(sy.Rational,reversed(trim(coeff)))),x)
    roots=sy.polys.polytools.intervals(poly,eps=sy.Rational(1,10**65))
    positives=[(a,b,k) for ((a,b),k) in roots if a>0]
    assert positives
    a,b,k=positives[0]
    assert k==1
    return (m(F(a))+m(F(b)))/2

def controls(n,L,U,c):
    fmid=(L+U)/2
    ttrue=3*mp.sqrt(mp.mpf('.5'))/n*m(fmid)*mp.mpf('1.5')**(-mp.mpf(n+1)/(2*n))
    X=(mp.mpf(2)/3)**(mp.mpf(1)/(2*n));theta=mp.acos(X);s=1/mp.sqrt(3)
    def err(t): return 100*abs((ttrue/t)**n-1)
    out={'t_true_mid':mp.nstr(ttrue,45),'f_true_width':mp.nstr(m(U-L),10),'true_H_relative_spread_percent':mp.nstr(100*((m(U)/m(L))**n-1),15)}
    out['slow_roll_percent']=mp.nstr(err(3*s/(n*X**(n-1))),30)
    out['theta_tangent_percent']=mp.nstr(err(3*theta/mp.sqrt(n)),30)
    out['sigma_tangent_percent']=mp.nstr(err(3*s/n),30)
    # Eq 66 from eq 65, avoiding typography/transcription ambiguity.
    aa=F(n*(3*n-7),108);bb=F(n*n*(65*n*n-570*n+1081),38880)
    pp=aa-bb/aa;qq=-bb/aa
    # First endpoint of t(1+p*t²)/(1+q*t²)=target.
    for name,p,q,target in [('theta66',pp,qq,3*theta/mp.sqrt(n)),('sigma68',F(n*(5-2*n),12),F(n*(17-6*n),36),3*s/n)]:
        # Rational bracket root in t via high precision polynomial isolation.
        targetrat=F(str(target))
        rt=first_root([-targetrat,F(1),-targetrat*q,p])
        if q<0: assert rt<mp.sqrt(-1/m(q))
        out[name+'_percent']=mp.nstr(err(rt),30)
    for d in (1,2,3,4,5,6,8):
        p,q=pade(hj_series(n,2*d),d,d)
        try:
            rt=first_root(add(scale(p,2),scale(q,-3)))
        except AssertionError:
            out[f'Hubble_{d}_{d}_percent']='no positive endpoint root'
            continue
        # Exclude a positive denominator zero before this endpoint.
        if len(q)>1:
            xx=sy.Symbol('x');poly=sy.Poly.from_list(list(map(sy.Rational,reversed(q))),xx)
            if poly.count_roots(0,sy.Rational(str(rt)))!=0:
                out[f'Hubble_{d}_{d}_percent']='rejected: denominator pole before endpoint'
                continue
        D=add(mul(diff(p),q),scale(mul(p,diff(q)),-1))
        endbound=F(str(rt))+F(1,10**60)
        try:
            for pol in [p,q,D,add(scale(mul(p,q),n),scale(shift(D),-1))]:
                positive(pol,F(0),endbound)
        except AssertionError:
            out[f'Hubble_{d}_{d}_percent']='rejected: monotonic physical branch not certified'
            continue
        t=3*X*mp.sqrt(rt)/n
        out[f'Hubble_{d}_{d}_percent']=mp.nstr(err(t),30)
    for k in (4,8,12,16,24):
        C=value(c[:k+1],F(1,2))
        out[f'inverse_Taylor_{k}_percent']=mp.nstr(100*abs((m(fmid)/m(C))**n-1),30)
    return out

def independent_original_integration(n):
    """Diagnostic in source variables s and t; no inverse-ODE integration."""
    from scipy.integrate import solve_ivp
    import numpy as np
    result=[]
    # Use s as independent variable, integrate t(s); forward stable slow branch.
    # Start well after s=0 from a fourth-order local approximation in r.
    cs=inverse_series(n,4)
    for s0 in (.02,.04):
        r0=s0/np.sqrt(1-s0*s0)
        t0=3*r0/n*float(value(cs,F(str(r0*r0))))*(1+r0*r0)**(-(n+1)/(2*n))
        def fun(s,y):
            t=y[0]
            return [3*t*s*s/n/(n*t*(1-s*s)**(1-1/(2*n))-3*s*(1-s*s))]
        sol=solve_ivp(fun,(s0,1/np.sqrt(3)),[t0],method='Radau',rtol=3e-12,atol=2e-14)
        assert sol.success
        result.append({'s0':s0,'t_endpoint':float(sol.y[0,-1]),'nfev':sol.nfev})
    return result

def main():
    allout={}
    for n in (2,3,20,30,50,100):
        start=time.time();cert=json.loads(Path(f'input/certificate_n{n}.json').read_text());c=inverse_series(n)
        L,low=check_row(cert['true_lower_barrier'],n,c)
        U,up=check_row(cert['true_upper_barrier'],n,c)
        C,sel=check_row(cert['selected_approximant'],n,c)
        assert L<U and [L,U]==list(map(F,cert['f_true_interval']))
        bound=100*max(abs((L/C)**n-1),abs((U/C)**n-1))
        reported=F(cert['selected_approximant']['error_percent_upper_exact'])
        assert bound<=reported
        # Rebuild the selected rational approximant from our own coefficients.
        pp,qq=pade(c,sel['degree'][0],sel['degree'][1])
        assert pp==list(map(F,cert['selected_approximant']['P']))
        assert qq==list(map(F,cert['selected_approximant']['Q']))
        checked=0
        for row in cert['all_certified_rows']:
            e,_=check_row(row,n,c)
            claimed=F(row['error_percent_upper_exact'])
            assert 100*max(abs((L/e)**n-1),abs((U/e)**n-1))<=claimed
            checked+=1
        allout[str(n)]={'lower':low,'upper':up,'selected':sel,'reported_bound_exact':str(reported),'bound_percent':str(float(bound)),'all_rows_checked':checked,'controls':controls(n,L,U,c),'original_ode_diagnostic':independent_original_integration(n),'seconds':time.time()-start}
        Path('independent_results.json').write_text(json.dumps(allout,indent=2)+'\n')
        print(n,json.dumps(allout[str(n)]),flush=True)
    print('INDEPENDENT_REFEREE_PASS',flush=True)

if __name__=='__main__': main()
