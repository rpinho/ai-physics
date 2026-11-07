"""Independent implementation of arXiv:2107.13871, Eqs 5.23,5.44-5.46.
No author-job modules used. Evaluate defining 3F2 at 1 in arbitrary precision.
Numerical diagnostics only; this module does not claim interval certification.
"""
import mpmath as m
import json, sys, time, math
from fractions import Fraction as Q
from concurrent.futures import ProcessPoolExecutor, as_completed

# Frozen witness coefficients, reconstructed from ordinary Legendre definition.
# The witness lists the effective partial-wave weight w, not the original
# crossing test a. Since P(1-z)=-P(z), a=.5*[z(1-z)]^(-1/4)*P(z)
# yields (1-z)^(5/4)*(a(z)-a(1-z)) = w=z^(-1/4)*(1-z)*P(z).
TERMS = [(1,Q('30113/125000')),(3,Q('-188947/250000')),
         (5,Q(1)),(7,Q('-2967/12500'))]
P = [Q(0) for _ in range(8)]
for d,c in TERMS:
    for j in range(d+1):
        P[j] += c * (-1)**(d+j) * math.comb(d,j)*math.comb(d+j,j)
def mpq(x): return m.mpf(x.numerator)/x.denominator

def K(x):
    # identical external operators, ell=0, paper Eq 5.23
    return (m.sqrt(m.pi)*m.gamma(x-m.mpf('.5'))/m.gamma(1-x)
            * (m.gamma((1-x)/2)/m.gamma(x/2))**2)

def block_moment(d,g,s,h):
    # Integral of z^g (1-z)^(s+2h) G_d(z), Eq 5.45.
    c = d+2*h+g+s+2
    return m.beta(d+g+1, 2*h+s+1)*m.hyper([d,d,d+g+1],[2*d,c],1)

def action(d,g,s,h,discrete=False):
    x=block_moment(d,g,s,h)-block_moment(d,s,g,h)
    if discrete:
        # Limit of K_(1-n) for even n, derived using gamma duplication/reflection.
        return 2*m.gamma(d)**2/m.gamma(2*d)*x
    return 2*m.re(K(1-d)*x)

def disconnected(g,s,h):
    return m.beta(g+1,2*h+s+1)-m.beta(s+1,2*h+g+1)

def candidate(d,discrete=False):
    return sum(mpq(c)*action(d,m.mpf(j)-m.mpf('.25'),-m.mpf('.25'),m.mpf('0.625'),discrete)/2
               for j,c in enumerate(P) if c)

def job(spec):
    m.mp.dps=45
    kind,value=spec
    t=time.time()
    if kind=='baseline':
        h=m.mpf(value)
        D=disconnected(m.mpf('2.1'),m.mpf(2),h)
        F=action(m.mpf(2),m.mpf('2.1'),m.mpf(2),h,True)
        ans={'h':str(h),'D':str(D),'F2':str(F),'bound':str(-D/F)}
    elif kind=='objective':
        D=sum(mpq(c)*disconnected(m.mpf(j)-m.mpf('.25'),-m.mpf('.25'),m.mpf('.625'))/2 for j,c in enumerate(P) if c)
        F=candidate(m.mpf(2),True)
        ans={'D':str(D),'F2':str(F),'bound':str(-D/F)}
    elif kind=='principal':
        nu=m.mpf(value); ans={'nu':str(nu),'action':str(candidate(m.mpf('.5')+1j*nu))}
    else:
        ans={'n':value,'action':str(candidate(m.mpf(value),True))}
    return {'kind':kind,'input':value,'result':ans,'seconds':time.time()-t}

if __name__=='__main__':
    specs=[('baseline','.625'),('baseline','.375'),('objective',None)]
    specs += [('principal',str(x)) for x in [1,8.52,8.53,8.6,9,10,12,20,39]]
    specs += [('discrete',x) for x in [4,6,8,12,20,40]]
    print(json.dumps({'polynomial':[str(x) for x in P],'tasks':specs}),flush=True)
    with ProcessPoolExecutor(max_workers=4) as pool:
        futs={pool.submit(job,s):s for s in specs}
        for fut in as_completed(futs):
            try: row=fut.result()
            except Exception as e: row={'spec':futs[fut],'error':repr(e)}
            print(json.dumps(row),flush=True)
