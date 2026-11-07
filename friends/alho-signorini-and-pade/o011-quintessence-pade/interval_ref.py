"""Independent interval audit, from source equations and coefficient data only.

Rebuilds residuals with exact rational polynomial arithmetic. The reference
time integral is rational in x=Omega_phi (unlike the submitted exp callback).
Only meromorphic callbacks enter acb.integral. All interval cell bounds are
validated with Arb; no claimant executable is imported or invoked.
"""
import os,json,time,math,sys
from fractions import Fraction
from flint import arb,acb,arb_poly,fmpq,fmpq_poly,ctx
ctx.prec=192
HERE=os.path.dirname(os.path.abspath(__file__))

def ball(v):
    f=Fraction(str(v)); return arb(fmpq(f.numerator,f.denominator))
def span(a,b): return arb(a).union(arb(b))
def upper(v): return v.abs_upper()
def peval(coeff,x):
    z=x*0
    for v in reversed(coeff): z=z*x+v
    return z
class Rat:
    def __init__(self,p,q=None):
        p=p if isinstance(p,fmpq_poly) else fmpq_poly(p)
        q=fmpq_poly([1]) if q is None else q
        g=p.gcd(q); self.p=p//g; self.q=q//g
        self.pc=[arb(c) for c in self.p]; self.qc=[arb(c) for c in self.q]
        self.ap=arb_poly(self.p); self.aq=arb_poly(self.q)
    @staticmethod
    def make(v): return v if isinstance(v,Rat) else Rat([fmpq(v)])
    def __add__(a,b):
        b=Rat.make(b); return Rat(a.p*b.q+b.p*a.q,a.q*b.q)
    __radd__=__add__
    def __neg__(a): return Rat(-a.p,a.q)
    def __sub__(a,b): return a+-Rat.make(b)
    def __rsub__(a,b): return Rat.make(b)+-a
    def __mul__(a,b):
        b=Rat.make(b); return Rat(a.p*b.p,a.q*b.q)
    __rmul__=__mul__
    def __truediv__(a,b):
        b=Rat.make(b); return Rat(a.p*b.q,a.q*b.p)
    def __rtruediv__(a,b): return Rat.make(b)/a
    def __pow__(a,n): return Rat(a.p**n,a.q**n)
    def derivative(a): return Rat(a.p.derivative()*a.q-a.p*a.q.derivative(),a.q**2)
    def __call__(a,x): return peval(a.pc,x)/peval(a.qc,x)
    def centered(a,x):
        # Validated polynomial composition about the dyadic midpoint avoids
        # dependency inflation from residual coefficient cancellation.
        m=x.mid(); h=x-m; shift=arb_poly([m,1])
        return a.ap(shift)(h)/a.aq(shift)(h)

def readrat(data): return Rat(fmpq_poly([fmpq(s) for s in data['P']]),fmpq_poly([fmpq(s) for s in data['Q']]))

def integrate(fn,a,b):
    a=arb(a); b=arb(b)
    value=acb.integral(lambda z,analytic:fn(z),acb(a.mid()),acb(b.mid()),rel_tol=arb('1e-32'),abs_tol=arb('1e-35'),eval_limit=100000)
    assert value.is_finite() and value.imag.contains(0),(str(a),str(b),str(value))
    assert value.real.rad()<arb('1e-25'),str(value)
    # Exact dyadic endpoints in the integrator; uncertain endpoint displacements
    # are covered by real-interval integrand bounds on their entire segments.
    endpoint_error=upper(fn(a))*a.rad()+upper(fn(b))*b.rad()
    return value.real+arb(0,endpoint_error.upper())

def tube(p,ref,delta=arb('0.0000002'),splits=2048):
    q=p/(p+2); Q=arb(q); a=readrat(ref['A']); b=readrat(ref['B']); x=Rat([0,1]); W=1-q*a*a
    assert a.p[0]==a.q[0] and b.p[0]==b.q[0] and a.q[0]!=0 and b.q[0]!=0
    f=(2-q*a*a)*(b-a)/(2*W*(1-x))
    g=b/2-(q/p)*a*b*b/(W*(1-x))
    r1=x*a.derivative()-f; r2=x*b.derivative()-g
    contraction=arb('0.1'); maxres=arb(0); mindet=arb(100); maxA=arb(0); maxB=arb(0)
    for i in range(splits):
        xx=span(ball(fmpq(17*i,25*splits)),ball(fmpq(17*(i+1),25*splits)))
        aa=a.centered(xx); bb=b.centered(xx)
        A=aa+arb(0,delta); B=bb+arb(0,delta); w=1-Q*A*A
        assert w>0 and A>0 and A<arb('1.1') and B>0
        res=upper(r1.centered(xx))**2+upper(r2.centered(xx))**2
        assert res<(contraction*delta)**2,(i,str(res))
        # Jacobian derived by differentiating the two rational source equations.
        c=(1+1/w)/(2*(1-xx)); ca=Q*A/((1-xx)*w*w)
        j11=ca*(B-A)-c
        j12=c
        j21=-arb(q/p)*B*B*(1+Q*A*A)/((1-xx)*w*w)
        j22=arb('0.5')-2*arb(q/p)*A*B/((1-xx)*w)
        d1=j11+contraction; d2=j22+contraction; off=(j12+j21)/2
        determinant=d1*d2-off*off
        assert d1<0 and d2<0 and determinant>0,(i,str(determinant))
        maxres=max(maxres,res.upper()); mindet=min(mindet,determinant.lower())
        maxA=max(maxA,upper(A)); maxB=max(maxB,upper(B))
    print('Independent tube PASS',str(p),'delta',str(delta),'res2',str(maxres),flush=True)
    return a,b,{'radius':str(delta),'lambda':str(contraction),'splits':splits,'residual_squared_upper':str(maxres),'symmetric_jacobian_shift_determinant_lower':str(mindet),'A_abs_upper':str(maxA)},delta

def candidate(p,data,d):
    row=next(r for r in data['rows'] if r['degree']==d)
    w=readrat(row); wi=-2/(p+2); x=Rat([0,1]); integrand=(w/wi-1)/x
    def lr(t):
        assert t>0
        return t.log()+integrate(integrand,arb(0),t)
    # Rational positive coefficients certify Q>0 and -w>0 on the positive axis.
    assert all(c>0 for c in w.q) and all(c<0 for c in w.p)
    lo=ball('1'); hi=ball('3'); target=ball('17/8').log()
    assert lr(lo)<target and lr(hi)>target
    for _ in range(105):
        mid=(lo+hi)/2; val=lr(mid)
        if val<target: lo=mid
        elif val>target: hi=mid
        else: break
    T0=span(lo,hi); assert T0.rad()<arb('1e-25')
    # For a ball t, evaluate integral at its midpoint, then enclose variation
    # by logR'=w/(wi*t), using the whole uncertain endpoint segment.
    def lrball(t):
        tm=t.mid(); cv=lr(tm); derivative=w(t)/(arb(wi)*t)
        return cv+arb(0,upper(derivative)*t.rad())
    return w,T0,lrball

def audit(ps):
    start=time.time(); p=fmpq(ps); q=p/(p+2); Q=arb(q); k=arb(6/(p+2)); xmax=ball('17/25')
    suffix='1.0' if p==1 else '0.1'
    ref=json.load(open(HERE+'/input/enclosure_p'+suffix+'.json'))
    data=json.load(open(HERE+'/input/attempt1_p'+suffix+'.json'))
    a,b,tubereceipt,delta=tube(p,ref)
    xrat=Rat([0,1]); wcenter=1-q*a*a
    def time_integrand(z): return 1/(3*(1-Q*a(z)**2)*z*(1-z))
    # Rigorously integrate in x, a rational meromorphic callback.
    def Ncenter(x): return integrate(time_integrand,xmax,x)
    Wmin=1-Q*ball('1.1')**2
    D=Q*delta*(ball('2.2')+delta)
    Nerr_per_y=D/(3*Wmin**2*(1-xmax))
    cands={d:candidate(p,data,d) for d in [2,6]}
    maxima={d:arb(0) for d in cands}; maxys={d:None for d in cands}
    h=ball('1/2048'); end=-arb(7).log(); cellcount=0
    # L(y)=log(Omega_m,candidate(Ntrue(y))/(1-x(y))).
    # L_y=[-w_candidate*Omega_phi,candidate/Wtrue-x]/(1-x).
    # Center value plus a whole-cell derivative enclosure covers every point.
    for i in range(12000):
        y=ball(fmpq(2*i+1,4096)); yy=span(ball(fmpq(i,2048)),ball(fmpq(i+1,2048)))
        xc=xmax*(-y).exp(); xx=xmax*(-yy).exp()
        nc=Ncenter(xc); nc=nc+arb(0,(y*Nerr_per_y).upper())
        A=a.centered(xx)+arb(0,delta); W=1-Q*A*A; assert W>0
        nd=1/(3*W*(1-xx))
        ncell=nc+arb(0,(upper(nd)*h/2).upper())
        for d,(w,T0,lr) in cands.items():
            tc=T0*(k*nc).exp(); logrc=lr(tc); logom=-(1+logrc.exp()).log()
            lc=logom-(1-xc).log()
            tall=T0*(k*ncell).exp(); wall=w(tall)
            # Propagate candidate log-density over the entire time cell.
            lograll=logrc+arb(0,(3*upper(wall)*upper(nd)*h/2).upper())
            candx=lograll.exp()/(1+lograll.exp())
            derivative=(-wall*candx/W-xx)/(1-xx)
            bound=upper(lc)+h*upper(derivative)/2
            boundpoint=bound.upper()
            if boundpoint>maxima[d]: maxima[d]=boundpoint; maxys[d]=str(y)
        cellcount=i+1
        if ncell.upper()<end: break
        if i%1000==0: print('cells',ps,i,{d:str(v) for d,v in maxima.items()},flush=True)
    else: raise AssertionError('coverage failed')
    out={'p':ps,'precision_bits':ctx.prec,'tube':tubereceipt,'cells':cellcount,'last_N_cell':str(ncell),'domain_z':['0','6'],'T0':{d:str(v[1]) for d,v in cands.items()},'results':[]}
    for d in cands:
        M=maxima[d]; om=M.exp()-1; E=(M/2).exp()-1
        out['results'].append({'degree':d,'log_error_upper':str(M),'Omega_m_uniform_relative_upper':str(om),'E_uniform_relative_upper':str(E),'worst_bound_y':maxys[d]})
        if d==6:
            # Check the submitted p-specific bound, not merely its rounded common bar.
            assert om<ball('0.00001326' if p==1 else '0.00001209')
            assert E<ball('0.00000663' if p==1 else '0.00000605')
    # Verify published and normalization-only controls at an exact interior density.
    x=ball('2/5'); y=(xmax/x).log(); n=Ncenter(x)+arb(0,upper(y*Nerr_per_y))
    assert n> end and n<0
    wi=arb(-2/(p+2)); gamma=1-(1-wi*wi)/(4*wi*wi-2*wi+1)
    beta=(36*wi**4-21*wi**3+7*wi*wi-1)/((4*wi*wi-2*wi+1)*(12*wi*wi-3*wi+1))
    Tp=xmax/(1-gamma*xmax); T=Tp*(k*n).exp()
    Rpub=ball('17/8')*(k*n).exp()*(((gamma-1)/beta)*((1+beta*Tp)/(1+beta*T)).log()).exp()
    w1=Rat([fmpq(-2/(p+2)),fmpq(0)])
    # [1/1] exact numerator/denominator from the independently rederived T series.
    from referee import series,pade
    from fractions import Fraction
    P1,Q1=pade(series(Fraction(str(p)))['w'],1)
    fake={'rows':[{'degree':1,'P':list(map(str,P1)),'Q':list(map(str,Q1))}]}
    wc,Tc,lrc=candidate(p,fake,1)
    Rc=lrc(Tc*(k*n).exp()).exp()
    ratios={'published_11':Rpub,'normalization_only_11':Rc,'wCDM':ball('17/8')*(-3*wi*n).exp(),'LambdaCDM':ball('17/8')*(3*n).exp()}
    out['controls_at_true_Omega_2over5']={}
    for name,R in ratios.items():
        ratio=1/((1+R)*(1-x)); ome=abs(ratio-1); ee=abs(1/ratio.sqrt()-1)
        assert ome>maxima[6].exp()-1 and ee>(maxima[6]/2).exp()-1
        out['controls_at_true_Omega_2over5'][name]={'Omega_m_error_interval':str(ome),'E_error_interval':str(ee)}
    out['status']='PASS'; out['elapsed_s']=time.time()-start
    json.dump(out,open(HERE+'/interval_'+ps.replace('/','_')+'.json','w'),indent=2)
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':
    for p in (sys.argv[1:] or ['1','1/10']): audit(p)
