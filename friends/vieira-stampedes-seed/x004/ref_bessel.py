"""Independent exact Fredholm expansion from BK 2006.01831 (29),(35),(39).

No claimant implementation is read or imported. Run on the authorized pod only.
The [0,1] monomial basis yields Cauchy--Binet sums over pairs of subsets.
"""
import argparse
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from itertools import combinations, permutations
from math import factorial as fac, comb, prod
from pathlib import Path
import json
import os
import time
from flint import fmpq as Q, fmpq_mat
from sympy import bernoulli


def zeta_even(j, p2):
    if j == 0:
        return Q(-1, 2)
    bn = bernoulli(2*j)
    return Q((-1)**(j+1) * int(bn.p) * 2**(2*j),
             int(bn.q) * 2 * fac(2*j)) * p2**j


def ladder_moments(N, B, p2):
    """Raw coefficient of A^k in BK (39), then closed-polynomial audit.

    Polylog inversion: Li_n -> -sum_j c_j A^(n-2j)/(n-2j)!,
    c_j=(2-2^(2-2j))*zeta(2j), on the real null-log sheet.
    The cross-ratio prefactor in (39) tends to -1. This cancels
    the polylog minus sign. Only t=m+2j-k can yield A^k.
    """
    cs = [(Q(2)-Q(2)**(2-2*j))*zeta_even(j, p2)
          for j in range(N//2+1)]
    qs = [Q(0)]
    for k in range(1, N+1):
        raw = Q(0)
        for m in range(k+1):
            weight = Q((-1)**m * fac(2*k-m)*fac(k), fac(k-m)*fac(m))
            for j in range(k//2+1):
                t = m+2*j-k
                if 0 <= t <= m:
                    raw += weight*cs[j]*comb(m,t)*(-B)**(m-t)/fac(2*k-m-2*j)
        simplified = sum((Q(fac(k), fac(k-2*j))*cs[j]*B**(k-2*j)
                          for j in range(k//2+1)), Q(0))
        assert raw == simplified, ('moment derivation',k,raw,simplified)
        qs.append(raw)
    return qs


def subsets_bounded(r, bound):
    def rec(prefix, start, left, budget):
        if not left:
            yield tuple(prefix)
            return
        for a in range(start, budget+1):
            # Minimum sum after choosing a: consecutive larger indices.
            tail = (left-1)*(2*a+left)//2
            if a+tail > budget:
                break
            yield from rec(prefix+[a], a+1, left-1, budget-a)
    return list(rec([],0,r,bound))


def exact_fredholm(N, ell, qs):
    out = [Q(1)]+[Q(0)]*N
    sectors = {}
    terms = {}
    r = 1
    while r*(r+ell) <= N:
        budget = N-r*(ell+1)
        minimum = r*(r-1)//2
        subsets = subsets_bounded(r,budget-minimum)
        subsets.sort(key=lambda a:(sum(a),a))
        meta = []
        for a in subsets:
            vand = prod(a[j]-a[i] for i in range(r) for j in range(i+1,r))
            norm = prod(fac(x)*fac(ell+x) for x in a)
            meta.append((a,sum(a),Q(vand,norm)))
        sec = [Q(0)]*(N+1)
        count = 0
        for ia,(a,sa,wa) in enumerate(meta):
            for b,sb,wb in meta[ia:]:
                degree = r*(ell+1)+sa+sb
                if degree > N:
                    break
                # det(H_b,a), H_b,a=1/(ell+a+b+1), exact Cauchy formula.
                weight = wa*wb/prod(ell+x+y+1 for x in a for y in b)
                if a != b:
                    weight *= 2
                if (r+sa+sb)%2:
                    weight = -weight
                core = fmpq_mat([[qs[ell+x+y+1]/(ell+x+y+1)
                                  for y in b] for x in a]).det()
                sec[degree] += weight*core
                count += 1
        out = [x+y for x,y in zip(out,sec)]
        sectors[str(r)] = list(map(str,sec))
        terms[str(r)] = count
        print(json.dumps(dict(event='sector',pid=os.getpid(),ell=ell,r=r,
                              subset_pairs=count,utc=time.time())),flush=True)
        r += 1
    return out,sectors,terms


def convolve(a,b,N):
    out=[Q(0)]*(N+1)
    for i,x in enumerate(a[:N+1]):
        if x:
            for j,y in enumerate(b[:N+1-i]):
                if y:
                    out[i+j]+=x*y
    return out


def gaussian(N,B,p2,sign=1):
    a=[Q(1)]
    for n in range(1,N+1):
        a.append((-B*a[-1]+(sign*p2*a[-2]/3 if n>1 else 0))/n)
    return a


def seed_recurrence(N,B,p2):
    a=[Q(1)]
    for n in range(1,N+1):
        a.append((B*a[-1]-(p2*a[-2] if n>1 else 0))/(n*n))
    return a


def mul_complex(a,b,p2):
    return (a[0]*b[0]-p2*a[1]*b[1],a[0]*b[1]+a[1]*b[0])


def seed_kummer(N,B,p2):
    """Direct 1F1 times exponential in Q[w]/(w^2+p2); w=i*pi.

    (1/2+iB/(2*pi))_k * (-2*i*pi)^k = product_j (B-(2j+1)w).
    """
    poch=[(Q(1),Q(0))]
    wpow=[(Q(1),Q(0))]
    for k in range(N):
        poch.append(mul_complex(poch[-1],(B,Q(-(2*k+1))),p2))
        wpow.append(mul_complex(wpow[-1],(Q(0),Q(1)),p2))
    out=[]
    for n in range(N+1):
        s=[Q(0),Q(0)]
        for k in range(n+1):
            v=mul_complex(poch[k],wpow[n-k],p2)
            d=fac(n-k)*fac(k)**2
            s[0]+=v[0]/d; s[1]+=v[1]/d
        assert s[1]==0,('Kummer imaginary remainder',n,s)
        out.append(s[0])
    return out


def seed_polynomials(N,p2):
    """a_n(B) as coefficient lists; used only for mixed derivatives."""
    a=[[Q(1)]]
    for n in range(1,N+1):
        p=[Q(0)]+a[-1]
        if n>1:
            for j,x in enumerate(a[-2]): p[j]-=p2*x
        a.append([x/(n*n) for x in p])
    return a


def derivative_entry(polys,di,dj,B,N):
    result=[]
    for k in range(N+1):
        n=k+di
        poly=polys[n]
        v=sum((poly[b]*Q(fac(b),fac(b-dj))*B**(b-dj)
               for b in range(dj,len(poly))),Q(0))
        result.append(v*Q(fac(n),fac(k)))
    return result


def mixed_determinant(N,ell,B,p2):
    p=seed_polynomials(N+ell-1,p2)
    entries=[[derivative_entry(p,i,j,B,N) for j in range(ell)] for i in range(ell)]
    out=[Q(0)]*(N+1)
    for perm in permutations(range(ell)):
        inv=sum(perm[i]>perm[j] for i in range(ell) for j in range(i+1,ell))
        term=[Q((-1)**inv)]+[Q(0)]*N
        for i,j in enumerate(perm): term=convolve(term,entries[i][j],N)
        out=[x+y for x,y in zip(out,term)]
    return out


def case_run(case):
    label,Bstr,pstr,N,ells=case
    start=time.time()
    B,p2=Q(Bstr),Q(pstr)
    qs=ladder_moments(N,B,p2)
    seed=seed_recurrence(N,B,p2)
    kummer=seed_kummer(N,B,p2)
    assert seed==kummer
    gplus=gaussian(N,B,p2,1)
    gminus=gaussian(N,B,p2,-1)
    baseline=[Q(1)]+[(B**n)/fac(n)**2 for n in range(1,N+1)]
    result=dict(label=label,B=str(B),pi_squared=str(p2),N=N,
                method='BK35 Bessel-monomial Cauchy-Binet Fredholm expansion',
                moments=list(map(str,qs)),seed=list(map(str,seed)),bridges={},
                kummer_recurrence_mismatches=[],
                trivial_I0_mismatches=[n for n in range(N+1) if seed[n]!=baseline[n]])
    for ell in ells:
        d,sectors,terms=exact_fredholm(N,ell,qs)
        if ell==0:
            expected=gplus
        else:
            tau=seed if ell==1 else mixed_determinant(N,ell,B,p2)
            expected=convolve(gplus,tau,N)
        mismatch=[n for n in range(N+1) if d[n]!=expected[n]]
        info=dict(coefficients=list(map(str,d)),sector_coefficients=sectors,
                  subset_pair_counts=terms,mismatches=mismatch)
        if ell==0:
            info['minus_gaussian_mismatches']=[n for n in range(N+1) if d[n]!=gminus[n]]
        result['bridges'][str(ell)]=info
        Path('results').mkdir(exist_ok=True)
        Path('results',label+'.json').write_text(json.dumps(result,indent=2))
        print(json.dumps(dict(event='bridge_done',label=label,ell=ell,
                              mismatches=mismatch,seconds=time.time()-start)),flush=True)
    result['seconds']=time.time()-start
    Path('results',label+'.json').write_text(json.dumps(result,indent=2))
    return dict(label=label,seconds=result['seconds'],
                comparisons=sum(len(v['coefficients']) for v in result['bridges'].values()),
                failures=sum(len(v['mismatches']) for v in result['bridges'].values()))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--smoke',action='store_true')
    args=parser.parse_args()
    cases=[('negative','-3/2','7/3',32,[0,1,2,3]),
           ('fractional','2/7','7/3',32,[0,1,2,3]),
           ('large','31','7/3',32,[0,1,2,3]),
           ('zero','0','7/3',32,[0,1,2,3])]
    if args.smoke: cases=[('smoke','2','1',8,[0,1,2,3])]
    with ProcessPoolExecutor(max_workers=min(4,len(cases))) as pool:
        summary=list(pool.map(case_run,cases))
    Path('results','summary.json').write_text(json.dumps(summary,indent=2))
    print(json.dumps(summary,indent=2),flush=True)
