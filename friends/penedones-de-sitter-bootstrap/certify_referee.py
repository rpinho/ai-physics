"""Fresh all-spectrum certificate using the referee's endpoint-series evaluator."""
from series_referee import A, P, PA, evaluate, prepare, TERMS
from fractions import Fraction as Q
from flint import arb,acb,ctx
from concurrent.futures import ProcessPoolExecutor,as_completed
import json, pathlib, time, hashlib, math
ctx.prec=640
START=Q(853,100);STOP=Q(39);STEP=Q(1,2)
L=96;DEG=94;RS=Q(3,10);RO=Q(12,25)

def beta(x,y): return x.gamma()*y.gamma()/(x+y).gamma()
def fresh_tail():
    # u=z^(7/4)*(1-z)*P, independently apply the Casimir monomial rule.
    base=Q(7,4);c=[Q(0)]*(len(P)+1)
    for j,p in enumerate(P): c[j]+=p;c[j+1]-=p
    bs=[];attempts=[];q0=STOP*STOP+Q(1,4)
    for m in range(25):
        bs.append(sum(c))
        if m>=3:
            norm=3*arb.pi()*sum((A(abs(x))*beta(A(base+j-Q(1,2)),A(Q(1,2))) for j,x in enumerate(c)),arb(0))
            C=Q(math.ceil(float(norm.upper())*(1+1e-12)))+1
            assert A(C)>norm
            rhs=sum((2*abs(bs[j])/q0**(j-1) for j in range(2,m)),Q(0))+C/q0**(m-2)
            passed=bs[0]==0 and 2*bs[1]>rhs
            attempts.append({'m':m,'passed':passed})
            if passed:
                return {'verified':True,'V':str(STOP),'q0':str(q0),'m':m,'norm_interval':str(norm),'norm_upper':str(C),'boundary_values':[str(x) for x in bs[:m]],'positive_rational_margin':str(2*bs[1]-rhs),'attempts':attempts}
        nxt=[Q(0)]*(len(c)+1)
        for j,x in enumerate(c):
            s=base+j;nxt[j]+=x*s*(s-1);nxt[j+1]-=x*s*s
        c=nxt
    raise ArithmeticError('No independently certified tail at 39')

def one_chart(task):
    idx,lo,hi=task;t0=time.time();cen=(lo+hi)/2;rad=(hi-lo)/2
    vals=[]
    for k in range(L//2+1):
        theta=2*arb.pi()*k/L
        z=acb(A(cen)+A(RS)*theta.cos(),A(RS)*theta.sin())
        v,err=evaluate(z);vals.append(v)
    coeff=[]
    for j in range(DEG+1):
        v=vals[0].real+(-1)**j*vals[L//2].real
        for k in range(1,L//2):
            t=-2*arb.pi()*j*k/L;v+=2*(vals[k]*acb(t.cos(),t.sin())).real
        coeff.append(v/L/A(RS)**j)
    delta=A(Q(1,100))
    # Euler integral: on all outer disks, Re Delta,Re(1-Delta)>=.02.
    # |Psi|<=4 B(delta,delta) z^delta (1-z)^(-1+delta).
    M=4*beta(delta,delta)*A(PA)*beta(A(Q(3,4))+delta,1+delta)
    q=A(RS/RO);r=A(rad/RO)
    alias=M*q**L/(1-q**L)/(1-r)
    tail=M*r**(DEG+1)/(1-r)
    err=alias+tail
    todo=[(-rad,rad,0)];leaves=[]
    while todo:
        left,right,depth=todo.pop()
        x=arb(A((left+right)/2),A((right-left)/2))
        y=arb(0)
        for c in reversed(coeff):y=y*x+c
        y+=arb(0,err.upper())
        if y>0: leaves.append([str(left),str(right),str(y.lower())])
        else:
            if y<0 or depth>=28: raise ArithmeticError(('positivity failed',idx,str(y),str(left),str(right)))
            mid=(left+right)/2;todo += [(left,mid,depth+1),(mid,right,depth+1)]
    return {'index':idx,'lo':str(lo),'hi':str(hi),'center':str(cen),'radius':str(rad),'verified':True,'leaves':leaves,'minimum_lower':str(min(arb(v[2]).lower() for v in leaves)),'alias_error':str(alias),'series_error_included':True,'taylor_tail':str(tail),'outer_global_bound':str(M),'coefficients':[str(x) for x in coeff],'circle_values':[str(x) for x in vals],'seconds':time.time()-t0}

if __name__=='__main__':
    t0=time.time();out=pathlib.Path('referee_certificate');out.mkdir(exist_ok=True)
    tail=fresh_tail();print('TAIL',json.dumps(tail),flush=True)
    D=sum((p*(1/(Q(3,4)+j)-1/(Q(7,4)+j)) for j,p in enumerate(P)),Q(0))
    finite=[]
    for n in range(2,40,2):
        v,e=evaluate(0,discrete=n);assert v.real>0
        assert v.imag.contains(0)
        finite.append({'n':n,'enclosure':str(v.real),'truncation_bound':str(e)})
        if n==2:
            objective=-A(D)/v.real
            assert objective<A(Q(34113,6250))
    sources={f:hashlib.sha256(pathlib.Path(f).read_bytes()).hexdigest() for f in ['series_referee.py','certify_referee.py']}
    meta={'tail':tail,'finite_discrete':finite,'D':str(D),'objective':str(objective),'bound':'34113/6250','sources':sources,'L':L,'degree':DEG,'sample_radius':str(RS),'outer_radius':str(RO)}
    (out/'manifest.json').write_text(json.dumps(meta,indent=2))
    tasks=[];lo=START
    while lo<STOP:
        hi=min(STOP,lo+STEP);tasks.append((len(tasks),lo,hi));lo=hi
    results=[]
    with ProcessPoolExecutor(max_workers=4) as pool:
        fs=[pool.submit(one_chart,t) for t in tasks]
        for f in as_completed(fs):
            row=f.result();(out/f"chart_{row['index']:03}.json").write_text(json.dumps(row,indent=2))
            results.append(row)
            print('CHART',row['index'],'positive',row['minimum_lower'],'seconds',row['seconds'],'done',len(results),'of',len(tasks),flush=True)
    results.sort(key=lambda x:x['index']);edge=START
    for x in results:
        assert Q(x['lo'])==edge;edge=Q(x['hi'])
        ll=sorted(x['leaves'],key=lambda a:Q(a[0]));e=-Q(x['radius'])
        for l,r,v in ll:
            assert Q(l)==e and Q(r)>e and arb(v)>0;e=Q(r)
        assert e==Q(x['radius'])
    assert edge==STOP
    final={'verified':True,'principal_interval':[str(START),str(STOP)],'charts':len(results),'tail':tail,'finite_even_n':list(range(2,40,2)),'objective':str(objective),'bound':'34113/6250','seconds':time.time()-t0,'sources':sources}
    (out/'VERIFIED.json').write_text(json.dumps(final,indent=2));print('FINAL',json.dumps(final),flush=True)
