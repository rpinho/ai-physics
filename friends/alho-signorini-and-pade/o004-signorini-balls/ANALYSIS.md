# Independent mathematical audit

The verdict concerns the theorem in CLAIM.md, not an optimal numerical radius,
priority, uniqueness, or dynamical stability. `reviewed_PROOF.md` preserves the
proof reviewed. No claimant implementation was imported or executed.

## Agreement with the primary problem

I independently transcribed the energy in 2104.11131v2 (2.12), with tau=0,
and differentiated using (1.2). A separate transcription of the energy in
1907.09970v2 §6.4 agrees exactly after lambda=3nu/(1+nu),
mu=3(1-2nu)/(2(1+nu)), kappa=1. These formulas permit negative lambda;
no extra assumption nu>=0 is made. SymPy's symbolic identities are rational
identities valid throughout -1<nu<1/2.

Writing eta=x^3 and delta=x^3 y, the physical mass equation implies
s x'=x(y-1), and the force equation gives
P'=2(Q-P)/s-s x^6 y for
s=r sqrt(4 pi G K^2/(3 kappa)). The dimensional factor is correct.
The density-variable solver uses the paper's (1.3), with independently
derived a=partial_delta P and b=2(Q-P)/(eta-delta)+3 partial_eta P.
Its RHS is different from the claimant's shooting formulation.

I also inspected the actual PDF Figure 8, rendered on the pod (retained as
figure8_page18.png). Its horizontal axis is labelled Radius, with apparent
surfaces near 0.60 and 0.53, not the dimensionless s radii 1.23 and 1.08.
Setting G=K=kappa=1 gives r=s sqrt(3/(4 pi)), which visually matches those
plots. The nearby paper text does not state the numerical unit convention,
so this unit choice is an inference. It does not justify attributing the
claimant's many-digit s values to the paper. The constitutive equations,
parameters, and exact physical scaling agree; no printed numerical record
is being improved. See figure_units.json for the conversion.

The primary 2020 definition of a strongly regular ball requires positive
interior principal pressures, vanishing radial surface pressure, isotropic
center, C1 interior fields up to the center and surface, and zero center
derivatives. It permits positive one-sided surface density and tangential
pressure followed by vacuum. The claim uses exactly this meaning.

## Singular center: checked beyond the polynomial certificate

Put h=1-y, v=s^2 and time tau=log s. Direct source differentiation gives
the smooth vector field

    xdot=-xh, hdot=-L(x,h)h+v C(x,h), vdot=2v,

where L=(x P_x+2(Q-P)/(1-y))/P_y, C=x^6(1-h)/P_y,
and L(x,0)=3. The apparent quotient is polynomial after cancelling 1-y.
At xc>1, P_y=2B xc^2(10 xc^2-alpha)>0 and Cc>0.
The exact Jacobian has eigenvalues 0,-3,2 and outgoing eigenvector
(-xc Cc/10,Cc/5,1). The zero eigenvalue is tangent to the equilibrium line,
not an extra growing direction. A compact local segment of that line has
uniform transverse spectral gaps, so the strong unstable fiber at the
specified equilibrium applies. Its v>0 branch is a graph over v near zero,
because the unstable tangent has nonzero v component. Translation in tau
does not introduce an unspecified physical parameter: v=s^2 fixes it.
The fiber is smooth as an individual curve, giving
h=Cc s^2/5+O(s^4), x=xc-xc Cc s^2/10+O(s^4).
All required center derivatives therefore vanish. Also Q-P=O(s^2),
which gives a C1 Cartesian stress at the center.

As an independent check on the use of the fiber theorem, one can write
the local branch as a contraction problem in the norm sup|h(v)|/v:

    x[h](v)=xc exp(-1/2 integral_0^v h(w)/w dw),
    h(v)=v^(-3/2)/2 integral_0^v w^(1/2)
          [-(L(x[h](w),h(w))-3)h(w)+w C(x[h](w),h(w))] dw.

Here L-3=O(h) uniformly near xc; the first term in brackets is O(w^2),
and the second is w Cc+O(w^2). On |h|<=M v, for M>Cc/5,
the map preserves this ball on a sufficiently short interval and has
Lipschitz constant O(v_max). Thus the required outgoing branch is not
being inferred from a numerical start near the singular point.

## First exit and finite radius

Let z=x^2, u=y^2, m0=6-alpha>0, Z=xc^2 and H=7Z^2+6Z.
The source pressure F=P/B satisfies, on z in [1,Z], u in [0,1],

    F(z,0)=-(2z-3)^2-m0(2z-1)<=-m0,
    F(z,u)=F(z,0)+u[z(4z-alpha)+3z^2u],
    z(4z-alpha)+3z^2u <= H.

The last inequality follows by expanding its slack into
7(Z^2-z^2)+6(Z-z)+(alpha+6)z+3z^2(1-u), all nonnegative.
For epsilon=m0/(2H)<1, y<=epsilon implies F<=-m0/2.
At x=1, F=(u-1)(3u+7-alpha)<0 for y<1.
At y=1, y'=-s x^6/P_y<0. Hence neither lower face nor the upper y face
can be the first positive-pressure exit; x decreases whenever y<1.

The potentially circular step is denominator loss. It is resolved by

    y P_y/(2B)-F=3z^2u^2-F(z,0)>=m0.

As long as F>=0, this proves P_y>=2B m0/y>=2B m0.
At a hypothetical finite endpoint s*>0 the derivatives are bounded,
the solution has a limit in the compact rectangle, and the smooth vector
field extends around that limit. If P>0 there, none of the exit faces is
allowed. If P=0 there, it is already the required finite surface.
Even the corner x=y=1 is excluded by the strict negative y' there.
No continuation through negative pressure and no transversal zero are
needed. Thus the proof does not use the 2020 global theorem's failed
Signorini exponent hypothesis.

For tangential pressure put t=z(2+u)>=2, b=alpha-2t. Exact algebra gives

    F=-(t-3)^2-m0(t-1)-2zu b.

If b>=0 the RHS is strictly negative. Therefore F>=0 forces b<0,
and Q-P=2Bz(1-u)(2t-alpha)>0 for positive s before and at the surface.
This establishes strict Q>0, including at a merely tangent first zero.

Finally (P+2Q)/B=t^2+alpha t-3alpha-9<(t+3)^2,
so P+2Q<=N=9B(Z+1)^2. The force equation implies

    (s^3 P)'=s^2(P+2Q)-s^4 x^6y <= N s^2-epsilon s^4.

Regularity at zero removes the integration constant. Consequently
P<=N/3-epsilon s^2/5; the alternative of positive pressure for every s
is impossible. R_s^2<=5N/(3epsilon). At the surface x>1,
y>epsilon, y<1 and P_y>0, giving positive density and regular one-sided
fields. Zero radial traction is exactly the vacuum boundary condition;
positive tangential stress does not create a nonzero surface traction.

For nu=1/4, delta_c=8 the exact certificate has epsilon=1/136,
N=135/4 and R_s^2<=7650. This is an upper bound, not a measured radius.
The proof establishes each fixed pair in the open parameter range;
it does not assert uniform bounds at nu=-1, nu=1/2, or delta_c=1.

## Numerical attacks and limitations

All 36 rational symbolic identities passed. Four independent numerical
baseline runs agree with the claimant's computed radii to about 5e-13;
those radii are not tabulated published values. Forty-two stress cases
spanning nu=-0.9999 to 0.4999 and delta_c=1.0001 to 10000 found finite
first pressure zeros with positive sampled denominators. These are
diagnostics, not quantified or interval-certified trajectories.

The original stress table is deliberately retained with its failure flag:
at nu=-0.9999, delta_c=1.0001, five-step double-precision dense output
reported min Q=-0.0003077. This is not silently counted as a pass.
Three step-limited density integrations gave positive sampled Q; two
70-digit RK4 refinements in x,h also gave min Q about 0.0001249975
and surface radius about 0.02499678. The original apparent contradiction
was a numerical interpolation/cancellation problem near a stiff material
endpoint. The exact signs and analytic proof, rather than numerical
positivity in that table, support the verdict. See flag_replay.json.

The natural zero-pressure state, an altered constant, the false universal
y=2/3 barrier and the fluid endpoint were checked as negative controls.
With gravity switched off, both density solvers remain constant and
produce no surface. Gravity is essential to the virial contradiction.

There is no dataset or hold-out. The frozen plan explicitly declares this,
and the claimed result is an exact all-parameter statement. The published
Figure 8 examples are public calibration cases, not held-out validation.
Their reuse cannot explain away the analytic result.

I found no mathematical obstruction to the stated theorem. This is a
human review of the analytic steps supported by exact algebra, not a
machine-formalized theorem or proof of novelty. Prior generic small-body
and variational results, plus the 2019 talk mentioning Signorini existence,
are recorded separately in PRIOR_ART.md for the taste reviewer.
