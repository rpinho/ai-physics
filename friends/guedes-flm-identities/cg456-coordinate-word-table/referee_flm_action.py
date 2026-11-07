"""Separate exact FLM left action from the paper's p-addition law.
No PBW, symmetrization, forward-map code, or claimant implementation imported.
Polynomial keys (a,b,c,h) mean X1^a X2^b X3^c i^h; values are Fraction.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


def add(*args):
    out={}
    for p in args:
        for a,c in p.items(): out[a]=out.get(a,F(0))+c
    return {a:c for a,c in out.items() if c}


def scale(p,c): return {a:c*b for a,b in p.items() if c*b}


def variable(p,j):
    out={}
    for a,c in p.items():
        b=list(a); b[j]+=1; out[tuple(b)]=c
    return out


def imaginary(p):
    return {(a,b,c,1-h):v*(-1 if h else 1) for (a,b,c,h),v in p.items()}


def derivative(p,j):
    out={}
    for a,c in p.items():
        if a[j]:
            b=list(a); b[j]-=1; out[tuple(b)]=a[j]*c
    return out


def laplacian(p): return add(*(derivative(derivative(p,j),j) for j in range(3)))


def sign(i,j,k):
    if len({i,j,k})<3: return 0
    return 1 if (i,j,k) in ((0,1,2),(1,2,0),(2,0,1)) else -1


def left(i,f):
    # d/dp1_i (p1 oplus p2)|p1=0 = sqrt(1-|p2|^2)e_i - e_i cross p2.
    # Replace p2 by -i*d/dX: L_i = X_i sqrt(1+Delta) + i eps_ijk X_k d_j.
    # Through length 4, sqrt(1+Delta)=1+Delta/2-Delta^2/8 exactly.
    df=laplacian(f)
    out=variable(add(f,scale(df,F(1,2)),scale(laplacian(df),F(-1,8))),i)
    for j in range(3):
        for k in range(3):
            out=add(out,scale(imaginary(variable(derivative(f,j),k)),F(sign(i,j,k))))
    return out


def build(w):
    f={(0,0,0,0):F(1)}
    for i in reversed(w): f=left(i-1,f)
    return f


def decode(terms):
    out={}
    for a,re,im in terms:
        for h,v in enumerate((re,im)):
            c=F(v)
            if c:
                key=tuple(a)+(h,)
                assert key not in out, 'duplicate term'
                out[key]=c
    return out


def encode(f):
    exps=sorted({a[:3] for a in f})
    return [[list(a),str(f.get(a+(0,),F(0))),str(f.get(a+(1,),F(0)))] for a in exps]


def main():
    # Complete independent calculations before reading any certificate.
    rebuilt={w:build(w) for n in range(1,5) for w in product((1,2,3),repeat=n)}
    # Verify commutators as operators on every commutative monomial of degree <=2.
    checks=0
    for a in product(range(3),repeat=3):
        if sum(a)>2: continue
        f={a+(0,):F(1)}
        for i,j in product(range(3),repeat=2):
            lhs=add(left(i,left(j,f)),scale(left(j,left(i,f)),F(-1)))
            rhs=add(*(scale(imaginary(left(k,f)),F(2*sign(i,j,k))) for k in range(3)))
            assert lhs==rhs, (a,i,j,'commutator')
            checks+=1
    own=json.loads(Path('rebuilt_forward.json').read_text())
    claimed=json.loads(Path('friends_board_guedes_1103/artifacts/coordinate_words.json').read_text())
    results={}
    failures=[]
    for label,certificate in [('forward_rebuild',own),('claim',claimed)]:
        rows=[r for r in certificate['records'] if r['map']=='flm' and 1<=len(r['word'])<=4]
        assert len(rows)==len(rebuilt)==120
        indexed={tuple(r['word']):decode(r['terms']) for r in rows}
        assert set(indexed)==set(rebuilt)
        counts={str(n):{'agree':0,'total':3**n} for n in range(1,5)}
        for w,f in rebuilt.items():
            if f==indexed[w]: counts[str(len(w))]['agree']+=1
            else: failures.append({'against':label,'word':list(w),'action':encode(f),'certificate':encode(indexed[w])})
        results[label]=counts
    summary={'method':'independent Fraction polynomial FLM differential action','commutator_controls':checks,'agreement':results,'disagreements':failures}
    Path('flm_action_results.json').write_text(json.dumps(summary,indent=2)+'\n')
    Path('rebuilt_flm_action.json').write_text(json.dumps({'records':[{'map':'flm','word':list(w),'terms':encode(f)} for w,f in rebuilt.items()]},indent=2)+'\n')
    print(json.dumps(summary,indent=2))
    assert not failures

if __name__=='__main__': main()
