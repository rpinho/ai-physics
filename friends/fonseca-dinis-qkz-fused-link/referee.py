#!/usr/bin/env python3
"""Independent reconstruction from arXiv:1212.4672 (2.1), C.1 and C.2.
No submitter program is imported. Run only on the authorized pod.
"""
import itertools, json, math, time, hashlib
from functools import lru_cache
from flint import fmpq, fmpq_poly, nmod_mat

T0=time.time()
def note(*s): print(round(time.time()-T0,2),*s,flush=True)

class Arithmetic:
    def __init__(self, root, order=5):
        self.root=root
        assert order in [3,5]
        self.order=order
        self.mod=fmpq_poly([1]*order)
        self.zero=self.c(0); self.one=self.c(1)
        self.q=fmpq_poly([0,1]) if root else fmpq(2)
    def c(self,n): return fmpq_poly([n]) if self.root else fmpq(n)
    def mul(self,a,b): return (a*b)%self.mod if self.root else a*b
    def inv(self,a):
        if self.root:
            g,s,t=a.xgcd(self.mod)
            assert g==1
            return s%self.mod
        return 1/a
    def div(self,a,b): return self.mul(a,self.inv(b))
    @lru_cache(None)
    def qp(self,k):
        if self.root: return (self.q**(k%self.order))%self.mod
        return self.q**k
    @lru_cache(None)
    def integer(self,n):
        return self.div(self.qp(n)-self.qp(-n),self.qp(1)-self.qp(-1))
    @lru_cache(None)
    def choose(self,n,k):
        v=self.one
        for i in range(k): v=self.div(self.mul(v,self.integer(n-i)),self.integer(i+1))
        return v
    def encode(self,a):
        if self.root: return [str(a[i]) for i in range(self.order-1)]
        return str(a)
    def residue(self,a,p,z):
        def rat(x): return int(x.numerator)%p*pow(int(x.denominator),-1,p)%p
        if not self.root: return rat(a)
        return sum(rat(a[i])*pow(z,i,p) for i in range(self.order-1))%p

def put(v,b,c):
    if c:
        t=v.get(b,0)+c
        if t: v[b]=t
        elif b in v: del v[b]

@lru_cache(None)
def states(ell,L,t):
    return tuple(b for b in itertools.product(range(ell+1),repeat=L) if sum(b)==t)

class Tensor:
    def __init__(self,A,ell,L): self.A=A; self.ell=ell; self.L=L
    @lru_cache(None)
    def terms(self,b,op):
        A=self.A; ell=self.ell; out=[]
        for i in range(self.L):
            if op=='E' and b[i]<ell:
                c=A.mul(A.integer(ell-b[i]),A.qp(sum(2*x-ell for x in b[:i])))
                t=list(b); t[i]+=1; out.append((tuple(t),c))
            if op=='F' and b[i]>0:
                c=A.mul(A.integer(b[i]),A.qp(-sum(2*x-ell for x in b[i+1:])))
                t=list(b); t[i]-=1; out.append((tuple(t),c))
        return tuple(out)
    def act(self,v,op):
        out={}
        for b,c in v.items():
            for t,a in self.terms(b,op): put(out,t,self.A.mul(c,a))
        return out
    @lru_cache(None)
    def divided_terms(self,b,r,op):
        # Quantum multinomial for ordered coproduct summands; local factorials
        # only run up to ell, hence no division by [5] at the fifth root.
        A=self.A; ell=self.ell; out=[]
        caps=[ell-x if op=='E' else x for x in b]
        for a in itertools.product(*(range(c+1) for c in caps)):
            if sum(a)!=r: continue
            exponent=sum(a[i]*a[j] for i in range(self.L) for j in range(i+1,self.L))
            if op=='E': exponent+=sum(a[i]*sum(2*x-ell for x in b[:i]) for i in range(self.L))
            else: exponent-=sum(a[i]*sum(2*x-ell for x in b[i+1:]) for i in range(self.L))
            coeff=A.qp(exponent)
            for cap,k in zip(caps,a): coeff=A.mul(coeff,A.choose(cap,k))
            t=tuple(x+y if op=='E' else x-y for x,y in zip(b,a))
            out.append((t,coeff))
        return tuple(out)
    def divided(self,v,r,op='E'):
        out={}
        for b,c in v.items():
            for t,a in self.divided_terms(b,r,op): put(out,t,self.A.mul(c,a))
        return out

@lru_cache(None)
def matchings(lo,hi,ell):
    if lo==hi: return ((),)
    out=[]
    for j in range(lo+1,hi,2):
        if lo//ell==j//ell: continue
        for inside in matchings(lo+1,j,ell):
            for outside in matchings(j+1,hi,ell):
                out.append(((lo,j),)+inside+outside)
    return tuple(out)

def projector_coordinates(A,ell):
    """Actual Jones-Wenzl recursion, then coordinates in the (2.1) basis."""
    one=A.one; zero=A.zero
    def ident(n): return [[one if i==j else zero for j in range(n)] for i in range(n)]
    def mm(X,Y):
        return [[sum((A.mul(X[i][k],Y[k][j]) for k in range(len(Y))),zero)
                 for j in range(len(Y[0]))] for i in range(len(X))]
    P=ident(2)
    for k in range(1,ell):
        n=2**(k+1)
        old=[[P[i//2][j//2] if i%2==j%2 else zero for j in range(n)] for i in range(n)]
        step=ident(n); alpha=A.div(A.integer(k),A.integer(k+1))
        # ordered binary basis 00,01,10,11; e from Appendix C.2
        for prefix in range(n//4):
            i=4*prefix+1; j=i+1
            step[i][i]+=A.mul(alpha,-A.qp(1)); step[j][j]+=A.mul(alpha,-A.qp(-1))
            step[i][j]+=alpha; step[j][i]+=alpha
        P=mm(mm(old,step),old)
    assert mm(P,P)==P
    words=list(itertools.product(range(2),repeat=ell)); ix={b:i for i,b in enumerate(words)}
    fundamental=Tensor(A,1,ell); u={(0,)*ell:one}; embeddings=[]
    for b in range(ell+1):
        embeddings.append(u)
        if b<ell:
            u={w:A.div(c,A.integer(ell-b)) for w,c in fundamental.act(u,'E').items()}
    # Check basis is fixed by P and intertwines both local generators.
    fused=Tensor(A,ell,1)
    for b,u in enumerate(embeddings):
        projected={w:sum((A.mul(P[ix[w]][ix[v]],c) for v,c in u.items()),zero) for w in words}
        assert {w:c for w,c in projected.items() if c}==u
        for op in ['E','F']:
            expected={}
            for (j,),c in fused.terms((b,),op):
                for w,a in embeddings[j].items(): put(expected,w,A.mul(c,a))
            assert fundamental.act(u,op)==expected
    table={}
    for w in words:
        b=sum(w); u=embeddings[b]; anchor=next(iter(u))
        table[w]=(b,A.div(P[ix[anchor]][ix[w]],u[anchor]))
    return table

def columns(A,ell,L):
    table=projector_coordinates(A,ell); patterns=matchings(0,ell*L,ell)
    out=[]
    for pattern in patterns:
        v={}
        for flips in itertools.product(range(2),repeat=ell*L//2):
            w=[0]*(ell*L); c=A.one
            for (i,j),flip in zip(pattern,flips):
                w[i]=1-flip; w[j]=flip
                if flip: c=A.mul(c,-A.q)
            b=[]
            for i in range(L):
                k,d=table[tuple(w[ell*i:ell*(i+1)])]; b.append(k); c=A.mul(c,d)
            put(v,tuple(b),c)
        assert v
        out.append(v)
    return patterns,out

def prime(n): return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))
def embedding(p,order):
    assert prime(p)
    return next(z for z in range(2,p) if pow(z,order,p)==1)

def rank_cols(vectors,basis,A,p,z):
    M=[[A.residue(v.get(b,A.zero),p,z) for v in vectors] for b in basis]
    return nmod_mat(M,p).rank()

def operator_rank(T,t,ops,p,z):
    basis=states(T.ell,T.L,t); rows={}; sparse=[]
    for b in basis:
        col={}
        for op in ops:
            terms=T.terms(b,op) if op in ['E','F'] else T.divided_terms(b,int(op[1:]),op[0])
            for dest,c in terms:
                key=(op,dest)
                if key not in rows: rows[key]=len(rows)
                col[rows[key]]=T.A.residue(c,p,z)
        sparse.append(col)
    data=[[0]*len(basis) for _ in rows]
    for j,col in enumerate(sparse):
        for i,c in col.items(): data[i][j]=c
    return {'size':len(basis),'rows':len(rows),'rank':nmod_mat(data,p).rank()}

def saved_input(A,filename):
    raw=json.load(open(filename)); out={}
    for w in raw['witnesses']:
        out[w['sum_b']]={tuple(b):fmpq_poly([fmpq(x) for x in c]) for b,c in zip(w['states'],w['coefficients_low_to_high']) if any(fmpq(x) for x in c)}
    return out

def run(ell,L,root,compare=False):
    order=ell+2
    A=Arithmetic(root,order); T=Tensor(A,ell,L); s=ell*L//2
    label=f'ell{ell}_L{L}_'+('root' if root else 'generic2'); note('START',label)
    patterns,cols=columns(A,ell,L); note('constructed actual projected columns',len(cols))
    for col in cols:
        assert not T.act(col,'E'); assert not T.act(col,'F')
    # Independently check regular divided-power expansion against repeated action
    # for r=2,3 (where no denominator vanishes) on representative states.
    for b in [states(ell,L,s)[0],states(ell,L,s)[len(states(ell,L,s))//2],(0,)*L]:
        for op in ['E','F']:
            v={b:A.one}; factorial=A.one
            for r in range(1,ell+1):
                v=T.act(v,op); factorial=A.mul(factorial,A.integer(r))
                normalized={x:A.div(c,factorial) for x,c in v.items()}
                assert normalized==T.divided({b:A.one},r,op)
    result={'label':label,'patterns':len(patterns),'exact_EF_columns':True,'projector_idempotent_and_intertwining':True,'modular':[]}
    witnesses={}
    if root:
        sectors=[t for t in range(ell*L+1) if (2*t-ell*L)%order==0]
        for t in sectors:
            w=T.divided({(0,)*L:A.one},t)
            assert w and not T.act(w,'E') and not T.act(w,'F')
            witnesses[t]=w
        if compare:
            claimed=saved_input(A,'claimant_witness.json')
            assert claimed==witnesses
            result['claimant_coefficients_equal_reconstruction']=True
        ws=witnesses[s]; target=witnesses[s+order]
        assert T.divided(ws,order)=={b:A.mul(A.c(2),c) for b,c in target.items()}
        for col in cols:
            assert not T.divided(col,order)
            assert not T.divided(col,order,'F')
        result['exact_divided_EF_links_zero']=True; result['exact_divided_E_witness_equals_2w']=True
        result['witness_supports']={str(t):len(w) for t,w in witnesses.items()}
        # Full exact small-kernel lower bounds: links plus three witnesses.
        expected={t:(len(cols)+1 if t==s else 1) for t in sectors}
    else:
        sectors=[s]; expected={s:len(cols)}
    for p in ([101,151] if order==5 else [103,151]):
        z=embedding(p,order) if root else 2
        rcols=rank_cols(cols,states(ell,L,s),A,p,z)
        assert rcols==len(cols)
        rec={'p':p,'q':z,'column_rank':rcols,'sectors':{}}
        for t in sectors:
            r=operator_rank(T,t,['E','F'],p,z)
            assert r['size']-r['rank']==expected[t]
            rec['sectors'][str(t)]=r
        if root:
            assert rank_cols(cols+[witnesses[s]],states(ell,L,s),A,p,z)==len(cols)+1
            r=operator_rank(T,s,['E','F','E'+str(order)],p,z)
            assert r['size']-r['rank']==len(cols)
            rec['with_divided_E']=r
            r=operator_rank(T,s,['E','F','E'+str(order),'F'+str(order)],p,z)
            assert r['size']-r['rank']==len(cols)
            rec['with_both_divided']=r
        result['modular'].append(rec); note('rank certificates',label,p,rec)
    result['exact_dimensions']={str(t):d for t,d in expected.items()}
    if root: result['full_K1_dimension']=sum(expected.values())
    with open(label+'.json','w') as f: json.dump(result,f,indent=2)
    if root and ell==3:
        with open('referee_patterns.json','w') as f: json.dump(patterns,f)
        with open('referee_witnesses.json','w') as f:
            json.dump({str(t):[[list(b),A.encode(c)] for b,c in w.items()] for t,w in witnesses.items()},f)
    note('PASS',label)
    return result

if __name__=='__main__':
    results=[]
    # Published generic baseline before the root obstruction.
    results.append(run(3,6,False))
    results.append(run(3,6,True,compare=True))
    results.append(run(1,10,True))
    json.dump({'results':results,'seconds':time.time()-T0,'status':'ALL PASS'},open('referee_results.json','w'),indent=2)
    note('ALL PASS')
