"""Small independent primary-source symbolic and normalization audits. Pod only."""
from itertools import combinations
from math import factorial as fac
from pathlib import Path
import json
import sympy as s

L,B,P,t=s.symbols('L B P t')
f=s.symbols('f0:7')

def kps_baseline():
    # KPS (1.39), independently transcribed, with formal loop variable t.
    tables=[]
    expected={0:[1,-2,6,-20,1,70,-6,-252,28,s.Rational(18,5)],
              1:[0,1,-4,15,0,-56,0,210,0,1],
              2:[0,0,1,-6,0,28,0,-120,0,0]}
    for ell in range(3):
        mat=[]
        for k in range(4):
            row=[]
            for j in range(4):
                entry=0
                for p in range(max(k+j+ell,1+j+ell),7):
                    num=(-1)**(p-ell)*fac(2*p-1)*(2*p*(2*k+ell)-(p-j)*(p+j+ell)*(k==0))
                    den=fac(p+k-j)*fac(p-k+j)*fac(p+k+j+ell)*fac(p-k-j-ell)
                    entry+=s.Rational(num,den)*f[p]*t**p
                row.append(entry)
            mat.append(row)
        # r>=3 starts at loop r(r+ell)>=9: all sectors through six included.
        series=s.expand(1+sum(mat[i][i] for i in range(4))+
                        sum(mat[i][i]*mat[j][j]-mat[i][j]*mat[j][i]
                            for i,j in combinations(range(4),2)))
        single={p:s.expand(series.coeff(t,p)).coeff(f[p])*fac(p)*fac(p-1)
                for p in range(1,7)}
        c13=s.expand(series.coeff(t,4)).coeff(f[1]).coeff(f[3])*12
        c14=s.expand(series.coeff(t,5)).coeff(f[1]).coeff(f[4])*144
        c15=s.expand(series.coeff(t,6)).coeff(f[1]).coeff(f[5])*2880
        c24=-s.expand(series.coeff(t,6)).coeff(f[3],2)*288
        actual=[single[1],single[2],single[3],single[4],c13,single[5],c14,single[6],c15,c24]
        assert actual==expected[ell],(ell,actual,expected[ell])
        # Explicitly check the cross monomial of the two six-loop basis minors.
        assert s.expand(series.coeff(t,6)).coeff(f[2]).coeff(f[4])==-c15/2880+c24/288
        tables.append(dict(bridge=ell,columns=['1','2','3','4','1,3','5','1,4','6','1,5','2,4'],values=list(map(str,actual))))
    return tables


def source_corrections(N=32):
    a=[s.Integer(1)]
    for n in range(1,N+1):
        a.append(s.expand((B*a[-1]-(P*a[-2] if n>1 else 0))/n**2))
    checked=0
    for n in range(N+1):
        assert a[n].coeff(P,0)==B**n/fac(n)**2
        j1=0
        if n>=2:
            k=n-2
            j1=B**k*s.Rational(1,6)*(s.Rational(1,fac(k)*fac(k+2))-s.Rational(2,fac(k)*fac(k+1)))
        assert s.expand(a[n].coeff(P,1)-j1)==0
        j2=0
        if n>=4:
            k=n-4
            j2+=B**k*s.Rational(1,360)*(s.Rational(7,fac(k)*fac(k+4))+s.Rational(32,fac(k)*fac(k+3)))
        if n>=5:
            k=n-5
            j2+=B**(k+1)*s.Rational(20,360*fac(k)*fac(k+4))
        assert s.expand(a[n].coeff(P,2)-j2)==0
        checked+=3
    return dict(coefficients_compared=checked,failures=0,first_coefficients=list(map(str,a[:7])))


def proof_algebra():
    r,z,u,v,w,h,nu=s.symbols('r z u v w h nu',nonzero=True)
    K0=(r*v*w-z*h*u)/(2*(r*r-z*z))
    # u=J_nu(r), v=J_(nu+1)(r), w=J_nu(z), h=J_(nu+1)(z).
    K1=(r*(2*(nu+1)*v/r-u)*h-z*(2*(nu+1)*h/z-w)*v)/(2*(r*r-z*z))
    rank=s.factor(r*K1/z-K0+u*h/(2*z))
    assert rank==0
    boundary=s.limit((r*(r/2)*w-z*h)/(2*(r*r-z*z)),r,0)-h/(2*z)
    assert s.simplify(boundary)==0
    logD=-L*B+P*L**2/6
    potential=-4*L*s.diff(logD,L)
    reduced=s.expand(potential-2*L*s.diff(potential,L))
    assert reduced==-4*L*B+4*P*L**2
    g,A=s.symbols('g A')
    # E.1 coefficientwise projection: retain g^2 A and g^4 A^2.
    cusp=s.series(s.log(s.cosh(2*s.pi*g))/(8*s.pi**2),g,0,6).removeO()
    null_log=s.expand(-(A+B)**2*cusp+(A-B)**2*g**2/4)
    scaled=-L*B+L**2*null_log.coeff(A,2).coeff(g,4)
    assert s.expand(scaled-(-L*B+s.pi**2*L**2/6))==0
    return dict(rank_one_residual=str(rank),boundary_residual=str(boundary),
                potential=str(potential),reduced_potential=str(reduced),
                gaussian=str(scaled),all_pass=True)


def finite_B_scope():
    # BK symbol (20), A=log z -> infinity with L=g^2 A fixed:
    # chi -> (1+exp(-B))/(1+exp(x/(4L)-B)). Its first moment is exact.
    # D1 starts at L^2, so d_L(D1/D0)|L=0 equals this moment.
    first=(1+s.exp(-B))*s.log(1+s.exp(B))
    points=[]
    for b in [0,2,5,10]:
        exact=first.subs(B,b)
        points.append(dict(B=b,finite_B_seed_linear=str(s.N(exact,25)),
                           formal_seed_linear=str(b),difference=str(s.N(exact-b,25))))
    return dict(exact_linear_coefficient=str(first),formal_linear_coefficient='B',
                difference='B*exp(-B)+(1+exp(-B))*log(1+exp(-B))',examples=points,
                interpretation='Scope control: finite-B power corrections are explicitly excluded by CLAIM.md, so this is not a counterexample to its formal identity.')


if __name__=='__main__':
    out=dict(baseline=kps_baseline(),printed_E7=source_corrections(),proof=proof_algebra(),scope=finite_B_scope())
    Path('results').mkdir(exist_ok=True)
    Path('results/source_audit.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
