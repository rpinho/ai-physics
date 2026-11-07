"""Independent source reconstruction and attacks. No claimant code imported.

Inputs: literal energy 2104.11131v2 (2.12), tau=0; physical equations
(1.1)-(1.3). The 2020 energy is a second primary-source transcription.
Run on mscr only. All exact checks are symbolic over QQ.
"""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, time
import sympy as S
import numpy as np
from scipy.integrate import solve_ivp

started=time.time()
x,y,nu=S.symbols('x y nu',positive=True)
a,z,u,Z=S.symbols('alpha z u Z',real=True)
h,v=S.symbols('h v',real=True)
checks=[]
def check(name,expression):
 result=S.factor(expression)
 assert result==0,(name,result)
 checks.append(name)

# eta=x^3, delta=x^3*y. All terms below are from 2021 equation (2.12).
W=(3*(5+8*nu)/(16*(1+nu))*x**-3/y
  -3*(1+4*nu)/(4*(1+nu))*x**-1*(1/y+y/2)
  +x*(3/(4*(1+nu))/y+3/(4*(1+nu))*y+3/(16*(1+nu))*y**3)
  -3*(1-2*nu)/(2*(1+nu)))
Pr=S.factor(x**3*y**2*S.diff(W,y))
Pt=S.factor(Pr+x**3*y/2*(x*S.diff(W,x)-3*y*S.diff(W,y)))
# Chain rule for (1.2): d_delta=x^-3 d_y;
# d_eta|delta=(3x^2)^-1 d_x - y/x^3 d_y.
lam=3*nu/(1+nu)
mu=3*(1-2*nu)/(2*(1+nu))
W20=((9*lam+5*mu)/8*x**-3/y
 -x**-1*((3*lam+mu)/2/y+(3*lam+mu)/4*y)
 +x*((lam+mu)/2/y+(lam+mu)/2*y+(lam+mu)/8*y**3)-mu)
check('2020 and 2021 literal stored energies agree',W-W20)
Rprinted=(3*(1+4*nu)/(8*(1+nu))*x**2*(2-y**2)
 +3/(16*(1+nu))*x**4*(-4+4*y**2+3*y**4)-3*(5+8*nu)/(16*(1+nu)))
Tprinted=(3*(1+4*nu)/(8*(1+nu))*x**2*y**2
 -3/(16*(1+nu))*x**4*(-4+y**4)-3*(5+8*nu)/(16*(1+nu)))
check('source radial pressure from energy',Pr-Rprinted)
check('source tangential pressure from energy',Pt-Tprinted)
check('natural state radial',Pr.subs({x:1,y:1}))
check('natural state tangential',Pt.subs({x:1,y:1}))
check('center pressure from source',Pr.subs(y,1)-3*(x*x-1)*(3*x*x+8*nu+5)/(16*(nu+1)))
check('center compressibility from source',S.diff(Pr,y).subs(y,1)/x**3-3*(5*x*x-4*nu-1)/(4*(nu+1)*x))

# Obtain claim's abbreviated polynomials from the source, not its verifier.
B=3/(2*(a+6))
R=S.factor(Pr.subs(nu,(a-2)/8))
T=S.factor(Pt.subs(nu,(a-2)/8))
F=S.Poly(S.cancel(R/B),x,y).as_expr().subs({x**4:z**2,x**2:z,y**4:u**2,y**2:u})
F=S.expand(F)
F0=S.expand(F.subs(u,0))
Fexpected=z**2*(3*u*u+4*u-4)+a*z*(2-u)-a-3
check('claimed radial polynomial equals source',F-Fexpected)
check('zero density negative form',F0+(2*z-3)**2+(6-a)*(2*z-1))
check('x=1 exit pressure',F.subs(z,1)-(u-1)*(3*u+7-a))
check('positive pressure gives denominator gap',
 S.diff(F,u)*2*u/2-F-(3*z*z*u*u-F0))
# y*P_y/(2B)=u F_u. Positive pressure implies u F_u>=6-alpha.
H=7*Z*Z+6*Z
bracket=S.cancel((F-F0)/u)
slack=7*(Z*Z-z*z)+6*(Z-z)+(a+6)*z+3*z*z*(1-u)
check('epsilon lower face certificate',H-bracket-slack)
theta=S.cancel((T-R)/(1-y))
check('center stable eigenvalue minus three',
 (x*S.diff(R,x)+2*theta-3*S.diff(R,y)).subs(y,1))
anis=S.factor((T-R)/(2*B*x*x*(1-y*y)))
check('anisotropy from source',anis-(2*x*x*(2+y*y)-a))
t=z*(2+u)
check('exclude adverse anisotropy on positive pressure',
 F-(-(t-3)**2-(6-a)*(t-1)-2*z*u*(a-2*t)))
trace=S.factor((R+2*T)/B)
check('trace expressed by t',trace-((x*x*(2+y*y))**2+a*x*x*(2+y*y)-3*a-9))
check('trace bound positive slack',(t+3)**2-(t*t+a*t-3*a-9)-((6-a)*t+3*(a+6)))

# Center: exact Jacobian of source-derived smooth autonomous vector field.
Py=S.diff(R,y)
L=S.cancel((x*S.diff(R,x)+2*theta)/Py)
C=S.cancel(x**6*y/Py)
field=S.Matrix([-x*h,(-L*h+v*C).subs(y,1-h),2*v])
J=field.jacobian([x,h,v]).subs({h:0,v:0})
cc=S.factor((x**6/Py).subs(y,1))
expected=S.Matrix([[0,-x,0],[0,-3,cc],[0,0,2]])
for i in range(3):
 for j in range(3): check(f'center Jacobian {i},{j}',J[i,j]-expected[i,j])
ev=S.Matrix([-x*cc/10,cc/5,1])
for i,e in enumerate(J*ev-2*ev): check(f'center outgoing eigenvector {i}',e)

# Reconstruct 2021 (1.3) in delta,eta, independently of the claim's x,y RHS.
Ad=S.factor(S.diff(Pr,y)/x**3)
Pe=S.factor((x*S.diff(Pr,x)/3-y*S.diff(Pr,y))/x**3)
Bd=S.factor(2*(Pt-Pr)/(x**3*(1-y))+3*Pe)
check('density equation center b coefficient is zero',Bd.subs(y,1))
rr=S.symbols('s',positive=True)
dp=(Bd*(x**3-x**3*y)/rr-rr*x**6*y)/Ad
ep=3*(x**3*y-x**3)/rr
xp=ep/(3*x*x)
yp=dp/x**3-3*y*xp/x
check('paper density equation yields claim x equation',xp-x*(y-1)/rr)
check('paper density equation yields claim pressure balance',
 S.diff(Pr,x)*xp+S.diff(Pr,y)*yp-(2*(Pt-Pr)/rr-rr*x**6*y))
check('virial identity from paper density equation',
 3*rr**2*Pr+rr**3*(S.diff(Pr,x)*xp+S.diff(Pr,y)*yp)
 - (rr**2*(Pr+2*Pt)-rr**4*x**6*y))

# Rational instance, no floating point in certificate.
params={a:S.Rational(4),Z:S.Rational(4)}
eps=S.cancel((6-a)/(2*H))
N=9*B*(Z+1)**2
check('example epsilon',eps.subs(params)-S.Rational(1,136))
check('example N',N.subs(params)-S.Rational(135,4))
check('example squared radius bound',(5*N/(3*eps)).subs(params)-7650)

# Negative controls that would fail a verifier accepting an altered law.
negative={
 'wrong constant breaks natural-state pressure':bool(S.simplify((Pr-3*(2+8*nu)/(16*(1+nu))).subs({x:1,y:1,nu:S.Rational(1,4)}))!=0),
 'natural state has no positive central pressure':Pr.subs({x:1,y:1})==0,
 'fluid endpoint loses strict epsilon':eps.subs(a,6)==0,
 'fixed two-thirds barrier can have positive pressure':bool(F.subs({a:S.Rational(599,100),z:S.Rational(36,25),u:S.Rational(4,9)})>0),
 'no gravity admits constant compressed branch':bool((dp+rr*x**6*y/Ad).subs(y,1)==0 and ep.subs(y,1)==0),
}
assert all(negative.values()),negative
exact=dict(status='PASS',checks=checks,count=len(checks),negative_controls=negative,
 source_energy=str(W),derived_radial=str(Pr),derived_tangential=str(Pt),
 source_F=str(F),density_a=str(Ad),density_b=str(Bd),center_jacobian=str(J),
 limitations='Symbolic identities are exact; domain signs, unstable-fiber existence and continuation are assessed in ANALYSIS.md, not proved by floating point.')
Path('independent_exact.json').write_text(json.dumps(exact,indent=2))
print('EXACT PASS',len(checks),flush=True)

fr=S.lambdify((x,y,nu),Pr,'numpy')
ft=S.lambdify((x,y,nu),Pt,'numpy')
fa=S.lambdify((x,y,nu),Ad,'numpy')
fb=S.lambdify((x,y,nu),Bd,'numpy')
fpy=S.lambdify((x,y,nu),S.diff(Pr,y),'numpy')

def shoot(n,dcentral,rtol,start_factor=1e-5,gravity=1):
 xc=dcentral**(1/3)
 pc=float(fr(xc,1,n))
 ac=float(fa(xc,1,n))
 # Characteristic small-overdensity radius and expansion from source (1.3).
 scale=np.sqrt(max(pc,1e-30)*ac/(dcentral*dcentral))
 s0=start_factor*min(1.,scale)
 d2=-gravity*dcentral*dcentral/(2*ac)
 state=[dcentral+d2*s0*s0,dcentral+3*d2/5*s0*s0]
 def rhs(s,state):
  d,e=state
  xx=np.cbrt(e); yy=d/e
  aa=fa(xx,yy,n); bb=fb(xx,yy,n)
  return [(bb*(e-d)/s-gravity*s*e*d)/aa,3*(d-e)/s]
 def surface(s,state):
  d,e=state
  return fr(np.cbrt(e),d/e,n)
 surface.terminal=True; surface.direction=-1
 # The theoretical bound is intentionally extremely loose; use physical scale
 # to bracket, extending the integration only when needed.
 end=max(10*scale,1.)
 sol=solve_ivp(rhs,(s0,end),state,method='DOP853',events=surface,
  rtol=rtol,atol=rtol*max(dcentral-1,1e-4)*0.01,
  max_step=max(scale/20,1e-6),dense_output=True)
 found=bool(len(sol.t_events[0]))
 d,e=sol.y[:,-1]; xx=np.cbrt(e); yy=d/e
 idx=np.linspace(s0,sol.t[-1],250)
 ds,es=sol.sol(idx); xs=np.cbrt(es); ys=ds/es
 alpha=2+8*n; zz=dcentral**(2/3)
 epsilon=(6-alpha)/(2*(7*zz*zz+6*zz))
 bound=5*(9*3/(2*(alpha+6))*(zz+1)**2)/(3*epsilon)
 return dict(nu=n,delta_c=dcentral,rtol=rtol,start=s0,gravity=gravity,
  event_found=found,success=sol.success,message=sol.message,steps=len(sol.t),
  R_s=float(sol.t[-1]),delta_surface=float(d),eta_surface=float(e),
  tangential_surface=float(ft(xx,yy,n)),radial_surface=float(fr(xx,yy,n)),
  min_y=float(ys.min()),min_x=float(xs.min()),min_Py=float(np.min(fpy(xs,ys,n))),
  min_tangential=float(np.min(ft(xs,ys,n))),epsilon=epsilon,R_squared_bound=bound,
  bound_observed=bool(sol.t[-1]**2<=bound),status='FLOATING_POINT_DIAGNOSTIC')

baselines=[shoot(n,2.,tol,factor) for n in [-.5,.25] for tol,factor in [(1e-10,1e-4),(2e-12,1e-6)]]
Path('independent_baseline.json').write_text(json.dumps(baselines,indent=2))
print('BASELINES',json.dumps(baselines),flush=True)
# Endpoint-near, large compression, and small-body controls; no random tuning.
grid=[(n,d) for n in [-.9999,-.9,-.5,0,.25,.49,.4999]
 for d in [1.0001,1.01,2.,8.,100.,1e4]]
stress=[]
for n,d in grid:
 row=shoot(n,d,2e-10)
 stress.append(row)
 Path('independent_stress.json').write_text(json.dumps(stress,indent=2))
 print('STRESS',n,d,row['event_found'],row['R_s'],row['min_Py'],flush=True)
controls=[shoot(-.5,2.,1e-11,gravity=0),shoot(.25,2.,1e-11,gravity=0)]
Path('independent_controls.json').write_text(json.dumps(controls,indent=2))
summary=dict(utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.time()-started,
 exact_checks=len(checks),negative_controls=negative,
 baseline_cases=len(baselines),stress_cases=len(stress),
 stress_events=sum(row['event_found'] for row in stress),
 stress_positive_denominators=all(row['min_Py']>0 for row in stress),
 stress_positive_tangential=all(row['min_tangential']>0 for row in stress),
 no_gravity_events=[row['event_found'] for row in controls],
 script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
Path('independent_summary.json').write_text(json.dumps(summary,indent=2))
print('DONE',json.dumps(summary),flush=True)
