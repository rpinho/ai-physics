# What the differential equation means, and what it does not establish

All identities refer to the leading-power double-light-cone projection specified in X004, keeping every inverse logarithm. They are formal coefficientwise statements before resummation; the resulting entire Kummer function also has well-defined analytic consequences. Neither projection nor coefficient comparison supplies a uniform error estimate for the full octagon at fixed cross ratios or at large L.

## 1. Standard route: the bridge is a dressed boundary mode

Use the generalized Bessel kernels of [Belitsky–Korchemsky, 2006.01831, Eqs.(3.15)–(3.17)](https://arxiv.org/abs/2006.01831) and the zero-bridge kernel of [2003.01121, Eqs.(2.15)–(2.17)](https://arxiv.org/abs/2003.01121):

    K_nu(x,y) = [sqrt(x) J_(nu+1)(sqrt(x)) J_nu(sqrt(y))
                  - sqrt(y) J_nu(sqrt(x)) J_(nu+1)(sqrt(y))]/[2(x-y)].

The elementary recurrence J2(t)=2J1(t)/t-J0(t) gives exactly

    sqrt(x/y) K1(x,y) = K0(x,y) - J0(sqrt(x)) J1(sqrt(y))/(2 sqrt(y)).

This is a rank-one change after the multiplication conjugation. Write D_l=det(1-K_l chi) and Q=(1-K0 chi)^(-1)J0. The determinant lemma yields

    D1/D0 = 1 + integral_0^infty J1(sqrt(y))/(2 sqrt(y)) chi(y) Q(y) dy
          = Q(0),

because K0(0,y)=J1(sqrt(y))/(2 sqrt(y)) and J0(0)=1. The manipulation uses the conventional regularized Fredholm setting, or coefficientwise perturbation theory; it is not an unproved bounded similarity transformation on arbitrary weighted spaces. The corresponding finite-matrix/fermionic interpretation is already explicit in [Kostov–Petkova, 2102.05000, Eqs.(1.8), (2.34)–(2.41)](https://arxiv.org/abs/2102.05000): the bridge inserts fermions and the ratio is a resolvent entry. The physical content of this route is an auxiliary boundary wave, already present in the standard determinant formulation.

In 2003.01121 Eq.(2.24) (PDF p11, printed p10), the published auxiliary equation is

    [(g d_g + 2x d_x)^2 + x + u - g d_g u] Q(x) = 0,
    u = -2g d_g log D0.                         [Eq.(2.21)]

After the claimed coefficientwise projection, L=g^2 log z, B=log(1/zbar), so g d_g=2L d_L. At x=0 use

    log D0 = -LB + pi^2 L^2/6,
    u = 4LB - (4/3) pi^2 L^2,
    u - g d_g u = -4LB + 4pi^2 L^2.

Dividing by 4L gives L tau_LL+tau_L+(pi^2 L-B)tau=0. This explains why a linear wave equation arises: it is the existing determinant's auxiliary resolvent problem evaluated at its endpoint. The reduction still inherits X004's assumption that the simplest and asymptotic symbols agree after the specified leading-power projection. This job does not newly prove that projection, nor the Toda hierarchy's microscopic origin.

There is a source sign inconsistency already recorded in X004: the standalone single-LCDS Gaussian in Stampedes I prints a minus sign on pi^2 L^2/6, whereas its preceding expansion and the printed seed coefficients require plus. Using the standalone minus sign instead produces L tau_LL+tau_L+(-pi^2 L-B)tau=0, with coefficient (B^2+pi^2)/4 at L^2, contradicting the printed seed. We use the convention consistent with that seed, not a newly asserted correction to a full observable.

`code/resolvent_check.py` verifies the kernel identity, the endpoint, the potential and both Gaussian signs symbolically. This is a short derivation from published machinery, not a new numerical standard.

## 2. Exact radial and Kummer dictionaries

In units hbar^2/(2m)=1, the zero-angular-momentum radial Laplacian in d dimensions is d_L^2+(d-1)L^(-1)d_L. Its coefficient here fixes d=2. Thus

    H_B = -d_L^2 - L^(-1)d_L + B/L,
    H_B tau = pi^2 tau.

The natural radial measure is L dL. Requiring a finite, no-log solution at the origin fixes tau(0)=1 and tau_L(0)=B. Removing that measure gives

    u=sqrt(L)tau,
    -u_LL + [B/L - 1/(4L^2)]u = pi^2 u.

The no-log boundary excludes sqrt(L) log L; simply imposing u(0)=0 would not select it. It is the regular/Friedrichs radial boundary, not a choice of additional contact interaction at the origin. The potential is 1/r restricted to a plane; strictly 2D electrostatics has a different potential. With rho=pi L and eta=B/(2pi),

    u_rhorho + [1 - 2eta/rho + 1/(4rho^2)]u = 0.

This is the Coulomb equation with formal angular index ell=-1/2, analytically continued from the usual integer-index convention. Equivalently the Whittaker index is mu=0, kappa=-i eta, argument -2i rho. Direct substitution tau=e^(i pi L)v(-2i pi L) gives

    z v_zz + (1-z)v_z - (1/2+i eta)v = 0.

[DLMF 33.2.4–5](https://dlmf.nist.gov/33.2#ii) then gives

    tau = F_(-1/2)(eta,rho)/(C_(-1/2)(eta) sqrt(rho)),
    C_(-1/2)^2 = pi/(1+exp(B)).

The latter follows from Gamma(1/2+i eta)Gamma(1/2-i eta)=pi/cosh(pi eta). Here B is charge at fixed scattering energy. Treating B instead as a spectral parameter of -(L d_L)' - pi^2 L is another valid Sturm–Liouville rewriting, with position-dependent kinetic coefficient; it is not the conventional constant-mass hydrogen Hamiltonian. For positive B this is repulsive scattering, not a bound-state spectrum. No map from a new SYM particle's physical position to L was derived.

## 3. Consequences and comparison with the paper

At fixed real B the usual Coulomb phase is rho-eta log(2rho)+pi/4+arg Gamma(1/2+i eta). It gives the expansion in PHYSICS.md with additive O_B(L^(-3/2)) error. Use a continuous branch for the Gamma phase. At B=0 the exact answer is J0(pi L), recovering its phase and amplitude. This B=0 substitution evaluates formal coefficient polynomials; it is not itself the physical large-B light-cone limit.

For the strict double scaling set x=LB and tau=f(x), at fixed B. Exactly,

    x f_xx + f_x - f + (pi^2/B^2) x f = 0.

Taking B to infinity at fixed x gives I0(2sqrt(x)), the seed in Stampedes II. More explicitly, with s=sqrt(LB), the first three inverse-log families printed in Stampedes I Eq.(93) are

    I0(2s)
    + pi^2 L/(6B) [I2(2s)-2s I1(2s)]
    + pi^4 (L/B)^2/360 [(20s^2+7)I4(2s)+32s I3(2s)] + ... .

Substituting the ODE recurrence

    (n+1)^2 a_(n+1) = B a_n - pi^2 a_(n-1), a_0=1, a_-1=0

reproduces each of those three families through L^20 exactly. In particular

    tau=1+BL+(B^2-pi^2)L^2/4+(B^3-5Bpi^2)L^3/36+... .

The referee separately starts with the exponential/Kummer Cauchy product, transcribes the printed Bessel families, and finds the same coefficients. These are exact algebra comparisons; there is no trained predictor, split, predictive score, or accuracy-improvement claim requiring SBS. The standard determinant remains exact and more general.

For the positive zeros, differentiate (L tau')'+(pi^2L-B)tau=0 in B, with v=partial_B tau. Then

    [L(tau v'-tau'v)]' = tau^2.

The origin Wronskian vanishes. At a simple zero r_n, tau'(r_n) is nonzero by uniqueness of the regular ODE away from zero. Integration and implicit differentiation give

    r_n'(B) = integral_0^(r_n) tau^2 dL / [r_n tau'(r_n)^2] > 0.

Oscillation theory or Coulomb asymptotics supplies infinitely many positive simple zeros for every fixed real B. For example the first zero at B=0 and 2 is 0.76547974956201235684 and 1.13298306096691880155 in both implementations. These are calculated values of the projected function. The source does not print large-L zero data; this job has not tested those zeros against an independent finite-cross-ratio octagon or new observed data.

## 4. Other candidate interpretations

| Candidate | Exact test | Outcome |
|---|---|---|
| Ordinary 3D hydrogen s wave, B an energy | Radial measure removal leaves -1/(4L^2); B multiplies 1/L | Rejected in that form. Keep the 2D scattering dictionary above. |
| Direct Fokker–Planck evolution/probability tau | D=L d_L^2+d_L is the backward generator of dX=dt+sqrt(2X)dW, but the full equation is (D+pi^2 L)tau=B tau; tau at B=0 is sign-changing J0 | Reject tau as a normalized transition probability on the whole half-line. A weighted spectral/Feynman–Kac representation is algebraically possible, but no microscopic stampede identification was found. |
| Microscopic spin-chain transfer matrix | The source's actual SL(2) Hamiltonian evolves in first-order logarithmic time; no explicit conjugation or scaling map to H_B has been derived | Existing stampede language remains valid; a two-component rewrite of this ODE alone would not explain its microscopic Hamiltonian. Keep only the published fermionic boundary-resolvent interpretation. |
| Toda/Painlevé | T_l=det[partial_L^(i-1)partial_B^(j-1)tau] obeys the published Toda identity by the determinant identity; q=L partial_L log tau obeys L q'=BL-pi^2L^2-q^2 | Keep Toda as existing determinant structure and the exact Riccati reduction. No specific new Painlevé parameter map or microscopic Toda mechanism was established, so none is claimed. |

The strict radial Bessel Toda reduction cannot simply be reused at finite B: tau depends independently on LB and the inverse-log correction. Already (L partial_L-B partial_B)tau=-pi^2 L^2/2+... is nonzero, so it is not just a function of LB. This prevents promoting Stampedes II's one-variable seed to the corrected answer by renaming its argument.

## 5. Reproduction and novelty

Run these from this directory, one at a time (Python dependencies: SymPy 1.14.0 and mpmath 1.3.0):

    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 10 .venv/bin/python code/physics_check.py
    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 10 .venv/bin/python code/resolvent_check.py
    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 10 .venv/bin/python code/referee_check.py

The corresponding JSON outputs are in data/. Main and referee code were written independently; neither imports the earlier X004 implementation. The referee additionally evaluates an angular Euler integral and the zero-derivative Wronskian integral. No cluster, remote computation or person was contacted. Research computations used one core per process, thread counts 1 and nice 10, with at most two simultaneous computations on this Mini.

NEW: no for a new physical-result claim from this follow-up. The closed-form seed is the pre-existing X004 result. This job explains it and states standard consequences of its special function. It neither beats a printed number nor tests a physical prediction on new data, nor resolves the missing microscopic Toda/stochastic explanation. The narrow prior-art conclusion in PRIOR_ART.md does not turn this explanatory reformulation into a new discovery.
