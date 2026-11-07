"""Resolve the apparent negative-pressure stress diagnostic independently."""
import json
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
import mpmath as mp

nu=-.9999; dc=1.0001; alpha=2+8*nu; B=3/(16*(1+nu))
def quantities(d,e):
 x=np.cbrt(e); z=x*x; y=d/e; u=y*y
 center=(z-1)*(3*z+alpha+3)
 P=B*(center+(u-1)*z*(3*z*u+7*z-alpha))
 Q=B*(center+(u-1)*z*(alpha-z*(u+1)))
 a=B*2*z*y*(6*z*u+4*z-alpha)/e
 Fz=2*z*(3*u*u+4*u-4)+alpha*(2-u)
 Fu=z*z*(6*u+4)-alpha*z
 b=B/e*(4*z*(1+y)*(2*z*(2+u)-alpha)+2*z*Fz-6*u*Fu)
 return P,Q,a,b

rows=[]
for tol,step,start in [(1e-11,1e-3,1e-4),(1e-13,2e-4,1e-4),(2.3e-14,5e-5,1e-3)]:
 ac=quantities(dc,dc)[2]
 d2=-dc*dc/(2*ac)
 def rhs(s,state):
  d,e=state
  P,Q,a,b=quantities(d,e)
  return [(b*(e-d)/s-s*e*d)/a,3*(d-e)/s]
 def event(s,state):return quantities(*state)[0]
 event.direction=-1;event.terminal=True
 sol=solve_ivp(rhs,(start,.05),[dc+d2*start**2,dc+.6*d2*start**2],
  method='DOP853',rtol=tol,atol=1e-17,max_step=step,events=event,dense_output=True)
 ts=np.linspace(start,sol.t[-1],1001)
 ds,es=sol.sol(ts)
 P,Q,_,_=quantities(ds,es)
 row=dict(rtol=tol,max_step=step,start=start,steps=len(sol.t),event_found=bool(len(sol.t_events[0])),
  R_s=float(sol.t[-1]),min_P=float(P.min()),min_Q=float(Q.min()),
  delta_surface=float(ds[-1]),eta_surface=float(es[-1]),
  max_y=float((ds/es).max()),min_y=float((ds/es).min()))
 rows.append(row)

# 70-digit integration in independent (x,h=1-y) variables, RK4 step
# refinement. All source coefficients use rational decimal input.
mp.mp.dps=70
n=mp.mpf('-0.9999'); d=mp.mpf('1.0001'); al=2+8*n; be=3/(16*(1+n))
xc=mp.root(d,3)
pyc=2*be*xc**2*(10*xc**2-al)
cc=xc**6/pyc
def rq(xx,hh):
 yy=1-hh; zz=xx**2; uu=yy**2
 cen=(zz-1)*(3*zz+al+3)
 return (be*(cen+(uu-1)*zz*(3*zz*uu+7*zz-al)),
  be*(cen+(uu-1)*zz*(al-zz*(uu+1))))
def rhs_mp(s,xx,hh):
 yy=1-hh; zz=xx**2; uu=yy**2
 py=2*be*zz*yy*(6*zz*uu+4*zz-al)
 px=be*2*xx*(2*zz*(3*uu**2+4*uu-4)+al*(2-uu))
 theta=2*be*zz*(1+yy)*(2*zz*(2+uu)-al)
 return -xx*hh/s, (-(xx*px+2*theta)*hh+s*s*xx**6*yy)/(s*py)
mp_rows=[]
for count in [500,1000]:
 start=mp.mpf('0.00001'); step=(mp.mpf('.03')-start)/count
 xx=xc-xc*cc/10*start**2;hh=cc/5*start**2;s=start
 prevP=rq(xx,hh)[0];minimumQ=rq(xx,hh)[1]
 for k in range(count):
  k1=rhs_mp(s,xx,hh)
  k2=rhs_mp(s+step/2,xx+step*k1[0]/2,hh+step*k1[1]/2)
  k3=rhs_mp(s+step/2,xx+step*k2[0]/2,hh+step*k2[1]/2)
  k4=rhs_mp(s+step,xx+step*k3[0],hh+step*k3[1])
  xx+=step*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6
  hh+=step*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
  s+=step
  pp,qq=rq(xx,hh)
  if pp<=0:
   radius=s-step+step*prevP/(prevP-pp)
   mp_rows.append(dict(steps=count,interpolated_R=str(radius),min_Q_before_surface=str(minimumQ),
    x_at_bracket=str(xx),h_at_bracket=str(hh),precision=70,certificate=False))
   break
  minimumQ=min(minimumQ,qq);prevP=pp

result=dict(flag='nu=-0.9999, delta_c=1.0001, loose double-precision dense output min Q < 0',
 refined_density_integrations=rows,high_precision_RK4=mp_rows,
 explanation='The original diagnostic took only five steps. Near nu=-1 a tiny state error is amplified by large material coefficients. Check the retained original failure alongside these refinements; numerical evidence is not the existence proof.')
Path('flag_replay.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2),flush=True)
