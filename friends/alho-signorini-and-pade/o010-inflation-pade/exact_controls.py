"""Exact algebraic control endpoint enclosures, independent referee module only."""
from referee import F,sy,pade,hj_series,trim,add,scale,mul,diff,shift,positive
from math import isqrt
from pathlib import Path
import json

def sqrt_bounds(x,digits=60):
    D=10**digits
    k=isqrt(x.numerator*D*D//x.denominator)
    a,b=F(k,D),F(k+1,D)
    assert a*a<=x<b*b
    return a,b

def main():
    out={}
    for n in (2,3,20,30,50,100):
        data=json.loads(Path(f'input/certificate_n{n}.json').read_text())
        L,U=map(F,data['f_true_interval'])
        out[str(n)]={}
        sel=data['selected_approximant']
        C=F(sel['f_endpoint'])
        a,b=(L/C)**n,(U/C)**n
        elo=100*(a-1 if a>1 else 1-b if b<1 else F(0))
        ehi=100*max(abs(a-1),abs(b-1))
        out[str(n)]['selected_inverse']={'status':'EXACT PASS','error_percent_interval':[str(elo),str(ehi)],'decimal_error_percent_interval':[float(elo),float(ehi)]}
        degrees=sorted(set([(2,2),(3,3),(4,4),(5,5),(6,6),(8,8),(9,9),(sel['m'],sel['d'])]))
        for m,d in degrees:
            p,q=pade(hj_series(n,m+d),m,d)
            x=sy.Symbol('y')
            poly=sy.Poly.from_list(list(map(sy.Rational,reversed(trim(add(scale(p,2),scale(q,-3)))))),x)
            roots=sy.polys.polytools.intervals(poly,eps=sy.Rational(1,10**65))
            rr=[(F(a),F(b),k) for ((a,b),k) in roots if a>0]
            key=f'{m}/{d}'
            if not rr:
                out[str(n)][key]={'status':'no positive endpoint root'}
                continue
            a,b,k=rr[0]
            assert k==1
            D=add(mul(diff(p),q),scale(mul(p,diff(q)),-1))
            try:
                counts=[positive(pol,F(0),b) for pol in [p,q,D,add(scale(mul(p,q),n),scale(shift(D),-1))]]
            except AssertionError:
                out[str(n)][key]={'status':'physical branch not certified'}
                continue
            # t_true/t_control=f/sqrt(3y) at q=0, exactly.
            lower=sqrt_bounds((L*L/(3*b))**n)[0]
            upper=sqrt_bounds((U*U/(3*a))**n)[1]
            errlo=100*(lower-1 if lower>1 else 1-upper if upper<1 else F(0))
            errhi=100*max(abs(lower-1),abs(upper-1))
            out[str(n)][key]={'status':'EXACT PASS','y_interval':[str(a),str(b)],'error_percent_interval':[str(errlo),str(errhi)],'decimal_error_percent_interval':[float(errlo),float(errhi)],'positive_leaf_counts':counts}
            assert errlo>0
        print(n,{k:v.get('decimal_error_percent_interval',v['status']) for k,v in out[str(n)].items()},flush=True)
        Path('exact_controls.json').write_text(json.dumps(out,indent=2)+'\n')
    print('EXACT_CONTROLS_PASS',flush=True)

if __name__=='__main__': main()
