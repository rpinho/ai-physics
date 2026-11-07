"""The other source curve: eq81 using Hubble Padé, not eq72."""
from referee import F,sy,hj_series,pade,add,scale,mul,shift,diff,positive,trim
from exact_controls import sqrt_bounds
from pathlib import Path
import json

out={}
for n in (2,3,20,30,50,100):
    cert=json.loads(Path(f'input/certificate_n{n}.json').read_text())
    L,U=map(F,cert['f_true_interval']);out[str(n)]={}
    for degree in (1,2,3,4,5):
        p,q=pade(hj_series(n,2*degree),degree,degree)
        D=add(mul(diff(p),q),scale(mul(p,diff(q)),-1))
        G=add(scale(mul(p,q),n),scale(shift(D),-1))
        # A=y*g(y)^2/F(y)=y*G^2/(n^2*P*Q^3).
        A=shift(mul(G,G));B=scale(mul(p,mul(q,mul(q,q))),n*n)
        ep=add(scale(A,2),scale(B,-1))
        x=sy.Symbol('y');poly=sy.Poly.from_list(list(map(sy.Rational,reversed(trim(ep)))),x)
        roots=sy.polys.polytools.intervals(poly,eps=sy.Rational(1,10**60))
        roots=[(F(a),F(b),k) for ((a,b),k) in roots if a>0]
        key=f'{degree}/{degree}'
        if not roots:
            out[str(n)][key]={'status':'no endpoint'};continue
        a,b,k=roots[0];assert k==1
        # Along eq81, X^(2n)=1/(1+A), t=3/n*sqrt(y)*(1+A)^(-1/(2n)).
        Ap=add(mul(diff(A),B),scale(mul(A,diff(B)),-1))
        Tp=add(scale(mul(B,add(B,A)),n),scale(shift(Ap),-1))
        try:
            counts=[positive(z,F(0),b) for z in [p,q,G,B,Ap,Tp]]
        except AssertionError:
            out[str(n)][key]={'status':'physical branch not certified'};continue
        lo=sqrt_bounds((L*L/(3*b))**n)[0];hi=sqrt_bounds((U*U/(3*a))**n)[1]
        elo=100*(lo-1 if lo>1 else 1-hi if hi<1 else F(0));ehi=100*max(abs(lo-1),abs(hi-1))
        out[str(n)][key]={'status':'EXACT PASS','y_interval':[str(a),str(b)],'error_percent_interval':[str(elo),str(ehi)],'decimal_error_percent_interval':[float(elo),float(ehi)],'positive_leaf_counts':counts}
    print(n,{k:v.get('decimal_error_percent_interval',v['status']) for k,v in out[str(n)].items()},flush=True)
    Path('source81_controls.json').write_text(json.dumps(out,indent=2)+'\n')
print('SOURCE81_CONTROLS_PASS',flush=True)
