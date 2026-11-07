"""Referee's standalone Arb evaluator, derived from the paper's block/Casimir.
Integrates convergent endpoint series exactly term by term, with rigorous tails.
No claimant search/verifier imports, no numerical quadrature, no cached spectra.
"""
from flint import arb, acb, ctx, fmpq
from fractions import Fraction as Q
import math, json, time, sys
ctx.prec=640
N=1024
TERMS=[(1,Q('30113/125000')),(3,Q('-188947/250000')),(5,Q(1)),(7,Q('-2967/12500'))]
P=[Q(0)]*8
for n,c in TERMS:
    for j in range(n+1):
        P[j]+=c*(-1)**(n+j)*math.comb(n,j)*math.comb(n+j,j)
def A(q):
    q=Q(q); return arb(fmpq(q.numerator,q.denominator))
PA=sum(abs(c) for c in P)
PC=[A(c) for c in P]

def prepare(nterms=N):
    # Exact integrals of t*P(1-t)*t^k and the corresponding log(t) term.
    r=arb(1)/2; lg=r.log(); weights=[]
    for k in range(nterms):
        w=arb(0);v=arb(0)
        for j,p in enumerate(PC):
            term=-p*r**(k+j+2)/(k+j+2)
            w+=term;v+=term*(lg-1/arb(k+j+2))
        weights.append((w,v))
    return weights
WEIGHTS=None

def evaluate(nu,nterms=N,discrete=None):
    global WEIGHTS
    if WEIGHTS is None or len(WEIGHTS)!=nterms: WEIGHTS=prepare(nterms)
    r=arb(1)/2; alpha=A(Q(3,4)); nu=acb(nu)
    if discrete is None:
        d=acb('0.5')+acb(0,1)*nu
        assert d.real>A(Q(1,100)) and (1-d).real>A(Q(1,100))
        assert nu.real>1
        ds=[d,1-d]
        ks=[(v.gamma()**2/(2*v).gamma())*(1+1/(acb.pi()*v).cos()) for v in ds]
        b0=4*arb(1).digamma()-2*d.digamma()-2*(1-d).digamma()+2*acb.pi()/(acb.pi()*d).sin()
        lam=d*(d-1)
    else:
        d=acb(discrete);ds=[d]
        ks=[2*d.gamma()**2/(2*d).gamma()]
        b0=-4*sum((arb(1)/j for j in range(1,discrete)),arb(0))
        lam=d*(d-1)
    left=acb(0);error=arb(0)
    for v,kv in zip(ds,ks):
        coeff=acb(1);power=r**(v+alpha)
        for k in range(nterms):
            moment=acb(0)
            for j,p in enumerate(PC):
                x=v+alpha+k+j
                moment+=p*r**j*(1/x-r/(x+1))
            left+=kv*coeff*power*moment
            coeff*=((v+k)**2/((2*v+k)*(k+1)))
            power*=r
        vm=abs(v).upper()
        ratio=r*(1+vm/nterms)**2
        assert ratio<1
        # Uniform 2F1 tail for z<=1/2; integrate the remaining z power.
        error+=abs(kv)*A(PA)*r**((v+alpha).real)/(v+alpha).real*abs(coeff)*r**nterms/(1-ratio)
    # v(t)=(1-t)^(-1/4)*Psi(1-t).  Frobenius recurrence for
    # t(1-t)^2 v''+[1+(2b-2)t+(1-2b)t^2]v'+[b-lambda+b^2 t]v=0.
    beta=-A(Q(1,4));aa=acb(-2);bb=acb(b0);prev_a=acb(0);prev_b=acb(0)
    right=acb(0)
    for k in range(nterms):
        w,v=WEIGHTS[k];right+=bb*w+aa*v
        kk=k+1
        B=-2*k*k+2*beta*k+beta-lam
        C=(k-1-beta)**2
        new_a=-(B*aa+C*prev_a)/(kk*kk)
        forcing=2*kk*new_a+(-4*k+2*beta)*aa+(2*(k-1)-2*beta)*prev_a
        new_b=-(B*bb+C*prev_b+forcing)/(kk*kk)
        prev_a,aa=aa,new_a;prev_b,bb=bb,new_b
    # Cauchy bound for the log and analytic Frobenius factors on |t|=3/4.
    # (D)_k/k! <= binom(k+M-1,M-1), M integer >= |d|,|1-d|.
    # Sum of squared binomials at u is <= 4^(M-1)*(1-u)^(1-2M).
    M=max(math.ceil(float(abs(v).upper())) for v in [d,1-d])+1
    rad=A(Q(3,4));rad2=A(Q(7,8));q=rad/rad2
    H=arb(4)**M*(1-rad)**(1-2*M)
    H2=arb(4)**M*(1-rad2)**(1-2*M)
    zfac=8*(arb(2)*M).exp() # bounds |(1-t)^(d-1/4)|, both shadows
    MA=4*zfac*H
    if discrete is None:
        ps=max(abs(v.digamma()).upper() for v in [d,1-d])
        MB=16*zfac*((1+ps)*H+102*q/(1-q)**2*H2)
    else:
        # Q-polynomial has the same zero-balanced analytic-series expression;
        # a single normalized block factor 2 gives the same conservative bound.
        ps=abs(d.digamma()).upper()
        MB=16*zfac*((1+ps)*H+102*q/(1-q)**2*H2)
    error+=A(PA)*(r/rad)**nterms*r*r/(nterms+2)/(1-r/rad)*(MB+MA*(-r.log()+1/arb(nterms+2)))
    total=left+right
    total+=acb(arb(0,error.upper()),arb(0,error.upper()))
    assert total.is_finite()
    return total,error

if __name__=='__main__':
    start=time.time(); WEIGHTS=prepare()
    for x in sys.argv[1:] or ['8.53','10','20','39']:
        s=time.time()
        if x.startswith('n'): val,err=evaluate(0,discrete=int(x[1:]))
        else: val,err=evaluate(acb(x))
        print(json.dumps({'input':x,'value':str(val),'tail_error':str(err),'seconds':time.time()-s}),flush=True)
    print('TOTAL_SECONDS',time.time()-start,flush=True)
