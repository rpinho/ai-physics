"""Ablations and a no-gap negative control, evaluated independently of search."""
import series_referee as s
from fractions import Fraction as Q
from flint import arb,ctx
import math,json,time
ctx.prec=640
full=s.P.copy()
def set_poly(p):
    s.P=p;s.PC=[s.A(x) for x in p];s.PA=sum(abs(x) for x in p);s.WEIGHTS=None

def control(label,p):
    set_poly(p)
    D=sum((q*(1/(Q(3,4)+j)-1/(Q(7,4)+j)) for j,q in enumerate(p)),Q(0))
    target,e=s.evaluate(0,discrete=2);orient=1 if target.real>0 else -1
    bound=-s.A(D)/target.real
    bad=[]
    points=[('n',n) for n in [4,6,8,10,12,20,38]]+[('nu',v) for v in ['8.53','9','10','11','12','13','16','20','30','39']]
    for kind,x in points:
        v,e=s.evaluate(0,discrete=x) if kind=='n' else s.evaluate(x)
        if orient*v.real<0:bad.append({'kind':kind,'at':x,'oriented_action':str(orient*v.real)})
    print(json.dumps({'control':label,'D':str(D),'F2':str(target.real),'objective':str(bound),'negative_modes':bad,'feasible_on_diagnostic_grid':not bad}),flush=True)

for n,c in s.TERMS:
    poly=[Q((-1)**(n+j)*math.comb(n,j)*math.comb(n+j,j)) for j in range(n+1)]
    control('single_L'+str(n),poly)
    omitted=full.copy()
    for j,v in enumerate(poly):omitted[j]-=c*v
    control('omit_L'+str(n),omitted)
set_poly(full)
neg=[];vals=[]
for i in range(101,853,10):
    nu=Q(i,100);v,e=s.evaluate(str(float(nu)));vals.append((v.real,nu))
    if v.real<0:neg.append({'nu':str(nu),'action':str(v.real)})
print(json.dumps({'control':'remove_principal_gap','negative_modes':neg,'lowest_point':str(min(vals,key=lambda x:float(x[0]))[1])}),flush=True)
