"""Independent forward-map inversion, from arXiv:1301.7750v2 Sec. 5.2.
No claimant implementation is read or imported. Exact SymPy QQ(i) polynomials.
"""
import hashlib
import itertools as it
import json
import math
from functools import lru_cache
from pathlib import Path
import sympy as s

X = s.symbols('X1:4')
I = s.I
R = s.Rational
MAPS = ('symmetric', 'duflo', 'flm')
DATA = Path('friends_board_guedes_1103/artifacts/coordinate_words.json')

def eps(i, j, k):
    return s.LeviCivita(i, j, k)

def clean(d):
    return {k: s.expand(v) for k, v in d.items() if s.expand(v) != 0}

@lru_cache(None)
def normal(w):
    """PBW order 1<=2<=3, using only [Xi,Xj]=2i eps_ijk Xk."""
    for t in range(len(w)-1):
        a, b = w[t:t+2]
        if a > b:
            out = dict(normal(w[:t] + (b, a) + w[t+2:]))
            k = 6-a-b
            factor = 2*I*eps(a,b,k)
            for u, c in normal(w[:t]+(k,)+w[t+2:]).items():
                out[u] = out.get(u,0) + factor*c
            return clean(out)
    return {w: s.Integer(1)}

def lap(f):
    return s.expand(sum(s.diff(f,x,2) for x in X))

def euler(f):
    return s.expand(sum(x*s.diff(f,x) for x in X))

def transform(f, name):
    # D = S o (1 + Delta/6 + Delta^2/120 + ...).
    # Q_F(exp(i p.X)) = S(exp(i asin(|p|)/|p| p.X)).
    # To degree 4, asin(r)/r=1+r^2/6+O(r^4) gives
    # T_F(f)=f-Euler(Delta(f))/6 (higher terms start degree 5).
    if name == 'symmetric': return f
    if name == 'duflo': return s.expand(f+lap(f)/6+lap(lap(f))/120)
    if name == 'flm': return s.expand(f-euler(lap(f))/6)
    raise ValueError(name)

@lru_cache(None)
def sym_monomial(a):
    w = tuple(i+1 for i, e in enumerate(a) for _ in range(e))
    perms = set(it.permutations(w))
    out = {}
    for p in perms:
        for u,c in normal(p).items(): out[u] = out.get(u,0)+c/R(len(perms))
    return clean(out)

def symmetrize(f):
    out = {}
    for a,c in s.Poly(f,*X).terms():
        for w,v in sym_monomial(a).items(): out[w] = out.get(w,0)+c*v
    return clean(out)

@lru_cache(None)
def forward_monomial(a, name):
    f = s.prod(x**e for x,e in zip(X,a))
    return symmetrize(transform(f,name))

def forward(f,name):
    out = {}
    for a,c in s.Poly(f,*X).terms():
        for w,v in forward_monomial(a,name).items(): out[w] = out.get(w,0)+c*v
    return clean(out)

def invert(w,name):
    remaining = dict(normal(w))
    answer = 0
    while remaining:
        u = max(remaining,key=lambda v:(len(v),v))
        c = remaining[u]
        a = tuple(u.count(i) for i in (1,2,3))
        answer += c*s.prod(x**e for x,e in zip(X,a))
        for v,b in forward_monomial(a,name).items():
            remaining[v] = s.expand(remaining.get(v,0)-c*b)
        remaining = clean(remaining)
    answer = s.expand(answer)
    assert forward(answer,name) == normal(w), (w,name,'forward round trip')
    return answer

def encode(f):
    return [[list(a),str(s.re(c)),str(s.im(c))] for a,c in sorted(s.Poly(f,*X).terms()) if c]

def decode(terms):
    # Strict rational coefficient parse; no eval or symbolic string parsing.
    return s.expand(sum((R(re)+I*R(im))*s.prod(x**e for x,e in zip(X,a)) for a,re,im in terms))

def printed(w,name):
    i,j = w[:2]
    x = lambda a:X[a-1]
    if len(w)==2:
        return s.expand(x(i)*x(j)+I*sum(eps(i,j,m)*x(m) for m in (1,2,3))-(R(1,3) if name=='duflo' and i==j else 0))
    k=w[2]
    base=x(i)*x(j)*x(k)+I*sum((eps(i,j,m)*x(k)+eps(i,k,m)*x(j)+eps(j,k,m)*x(i))*x(m) for m in (1,2,3))
    coeff={'symmetric':(R(2,3),-R(1,3),R(2,3)), 'duflo':(R(1,3),-R(2,3),R(1,3)), 'flm':(1,-1,1)}[name]
    return s.expand(base+coeff[0]*int(j==k)*x(i)+coeff[1]*int(i==k)*x(j)+coeff[2]*int(i==j)*x(k))

def main():
    # Complete independent construction BEFORE opening the claimant JSON.
    rebuilt = {(name,w):invert(w,name) for n in range(1,5) for w in it.product((1,2,3),repeat=n) for name in MAPS}
    records=[{'map':name,'word':list(w),'terms':encode(f)} for (name,w),f in rebuilt.items()]
    Path('rebuilt_forward.json').write_text(json.dumps({'records':records},indent=2)+'\n')
    raw=DATA.read_bytes()
    original=json.loads(raw)
    assert original['normalization']=='[Xi,Xj]=2i epsilon_ijk Xk'
    selected=[r for r in original['records'] if 1<=len(r['word'])<=4]
    indexed={(r['map'],tuple(r['word'])):r for r in selected}
    assert len(indexed)==len(selected)==360, 'missing, duplicate or extra records'
    assert set(indexed)==set(rebuilt), 'wrong word coverage'
    failures=[]
    counts={name:{} for name in MAPS}
    paper_counts={name:{} for name in MAPS}
    paper_failures=[]
    for (name,w),f in rebuilt.items():
        n=len(w)
        g=decode(indexed[name,w]['terms'])
        counts[name].setdefault(str(n),{'agree':0,'total':0})
        counts[name][str(n)]['total']+=1
        if f==g: counts[name][str(n)]['agree']+=1
        else: failures.append({'map':name,'word':list(w),'rebuilt':encode(f),'claimed':encode(g),'difference':encode(s.expand(f-g))})
        if n in (2,3):
            p=printed(w,name)
            paper_counts[name].setdefault(str(n),{'agree':0,'total':0})
            paper_counts[name][str(n)]['total']+=1
            if f==p: paper_counts[name][str(n)]['agree']+=1
            else: paper_failures.append({'map':name,'word':list(w),'rebuilt_minus_printed':encode(s.expand(f-p))})
    result={'method':'PBW reduction and forward-map inversion','claim_sha256':hashlib.sha256(raw).hexdigest(),'agreement':counts,'disagreements':failures,'forward_roundtrips':len(rebuilt),'printed_agreement':paper_counts,'printed_disagreements':paper_failures,'pure_quartic':{name:str(rebuilt[name,(1,1,1,1)]) for name in MAPS},'max_degree':4}
    Path('comparison.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    assert not failures

if __name__=='__main__': main()
