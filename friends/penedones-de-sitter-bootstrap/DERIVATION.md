# Independent derivation and certification

Primary source: Hogervorst, Penedones and Salehi Vaziri, arXiv:2107.13871v2, sections 5.1, 5.3 and 5.4, especially equations (5.43)–(5.53). The journal/TeX numbering is used here; the arXiv HTML renumbers the equations consecutively. The PDF downloaded independently on the pod matches the claimant's public source byte for byte. No claimant Python module is imported by any referee evaluator.

## Quantity and functional

Set h=5/8 and nu*=853/100. Let P be the rational combination of shifted Legendre polynomials with coefficients 30113/125000, -188947/250000, 1, -2967/12500 at degrees 1,3,5,7. Its coefficients are reconstructed from the factorial formula, rather than taken from the witness's expanded arrays. Since P(1-z)=-P(z), applying the paper's crossing equation with the original test

    a(z) = (1/2) [z(1-z)]^(-1/4) P(z)

gives the effective partial-wave weight

    w(z) = (1-z)^(5/4)[a(z)-a(1-z)] = z^(-1/4)(1-z)P(z).

The witness's basis string describes w, not a. Treating w as the original crossing test changes the problem. Our first diagnostic did that, gave 5.53530, and was discarded before certification. This does not contradict the claimant's derivation, which correctly distinguishes them. The final defining-3F2 implementation expands a into (gamma,sigma)=(j-1/4,-1/4) with half the polynomial coefficients. Both endpoint exponents exceed -1, satisfying the paper's convergence criterion.

The identity contribution is D=integral(w)=-1058384983/16298734375. The spectral actions are F(nu)=integral(w Psi_(1/2+i nu,0)) and F_n=integral(w Psi_(n,0)). The exact reconstructed functional, paper normalization and prescribed gap are unchanged. Positivity of all these actions gives I-tilde_(2,0) <= -D/F_2. The fresh interval objective is 5.4580734714720031025256703361474007847041448079903959..., strictly below 34113/6250.

## Two independently implemented evaluation routes

1. `independent_check.py` evaluates the paper's gamma and 3F2 expressions in mpmath, at 45 decimal digits. It reproduces the fully specified baseline 6.431737260572546574... at h=5/8, and 2.386377515308742831... at h=3/8. It also reproduces the accepted objective and individual principal/discrete actions. These are diagnostics, not certificates.

2. `series_referee.py` uses python-flint Arb/Acb at 640 bits. It integrates two convergent endpoint series term by term, including rounding and explicit truncation bounds. It uses no quadrature rule, optimizer, stored spectral arrays, or claimant verifier code. Split z at 1/2 and write d=1/2+i nu. For the lower half, expand G_d=z^d sum_k (d)_k^2 z^k/[(2d)_k k!], with coefficient K_(1-d)=B(d,d)(1+sec(pi d)); add the shadow. The remaining tail after N=1024 terms is geometric because, for k>=N,

    |c_(k+1)/c_k|/2 <= (1+|d|/N)^2/2 < 1.

The z powers and (1-z) polynomial are integrated exactly with complex ball arithmetic. Absolute monomial coefficients bound the uncomputed remainder.

For the upper half put t=1-z and v(t)=(1-t)^b Psi(1-t), b=-1/4. The Casimir equation becomes

    t(1-t)^2 v'' + [1+(2b-2)t+(1-2b)t^2]v' + [b-lambda+b^2 t]v = 0.

Write v=sum_k (a_k log(t)+b_k)t^k. Its starting values are a_0=-2 and

    b_0=4 psi(1)-2 psi(d)-2 psi(1-d)+2 pi/sin(pi d).

For even discrete n, use d=n, lambda=n(n-1), b_0=-4 H_(n-1), and the single normalized block K_(1-n)=2 B(n,n). Substitution into the displayed differential equation gives the three-term recurrences in the source. All t powers and log(t) powers are integrated exactly against t P(1-t).

The analytic log and regular factors are bounded on |t|=3/4 using the zero-balanced hypergeometric expansion. For integer M>=|d|,|(1-d)|, the absolute hypergeometric coefficients are bounded by binom(k+M-1,M-1)^2, whose generating function at u is at most 4^(M-1)(1-u)^(1-2M). The regular factor's digamma terms grow at most linearly in k. A second radius 7/8 bounds the extra k factor. Explicit deliberately loose Cauchy bounds MA,MB appear in the code. Their tail integral is bounded by

    PA*(r/R)^N*r^2/[(N+2)(1-r/R)] * [MB+MA*(-log(r)+1/(N+2))],

where r=1/2, R=3/4, PA=sum_j |P_j|. This includes both omitted endpoint-series tails. At nu=39 the retained bound on this error is about 5.37e-41, well below the positive action 2.342e-7. The two evaluation routes agree.

## Compact continuum, exact tails and discrete modes

`certify_referee.py` uses 61 closed intervals covering [8.53,39]. On each, it evaluates 96 equally spaced circle points of radius 3/10 (49 computations suffice by conjugation symmetry), using only the new endpoint-series evaluator. The discrete Fourier transform encloses Taylor coefficients through degree 94. The outer analytic disk radius is 12/25. An Euler integral bounds the function there by

    M*=4 B(delta,delta) PA B(3/4+delta,1+delta), delta=1/100.

The two normalized block factors are bounded by 2 each because Re(nu)>1; both real parts of d and 1-d stay above delta. The integrated bound follows from |w|<=PA z^(-1/4)(1-z). Cauchy's estimate gives explicit Fourier alias and omitted Taylor errors. Interval Horner evaluation, subdividing real intervals if needed, proves positivity throughout every interval; the final code independently checks that the accepted leaves and charts form complete partitions. This is not a finite-grid inference.

For both infinite tails, set u=z^(7/4)(1-z)P. With C=z^2(1-z)d_z^2-z^2 d_z, integration by parts gives

    lambda F = 2u(1) + integral((C u) Psi dz/z^2).

All lower-end boundary terms vanish. The upper-end term uses Psi=-2 log(1-z)+O(1). Apply C z^s=s(s-1)z^s-s^2 z^(s+1) in exact Fraction arithmetic. The common bound |Psi|<=3 pi sqrt(z/(1-z)) holds for principal nu>=1 and every even discrete n>=2, using the paper's Euler block integral. Thus the remaining norm is bounded by 3 pi sum_j |c_j| B(s_j-1/2,1/2). Arb encloses the beta values and verifies an upward integer norm bound. At 23 integrations by parts, exact rational arithmetic proves the leading positive term dominates every correction for |lambda|>=6085/4. This covers principal nu>=39 and even n>=40. All remaining even n=2,4,...,38 pass the separate endpoint-series enclosure. The target n=2 also supplies the objective inequality.

No new physical assumptions are introduced beyond the paper's positivity, spectral gap and regularized crossing/growth framework. There is no statistical dataset or hold-out: the rational witness was frozen and then checked on the full continuous/discrete spectrum by independent code.

## Controls and limitations

The single degree-1 effective weight yields objective 10.8757188312, and the other three single terms fail positivity after normalizing the target positively. Dropping degree 5 gives the tempting objective 2.78965859952 but a strictly negative n=6 action. Dropping degree 7 also fails at n=6. Dropping degree 3 worsens the diagnostic objective to 17.63037. All controls are recorded as diagnostics, not alternate certified bounds. Removing the principal gap exposes negative action at nu=2.21 (about -0.28014747), so the witness must not be used as a bound without that assumption.

The exact eight pairs and coefficients underlying the printed 5.67049 are unavailable in the recovered primary archive. We reproduce the specified single-functional baseline and prove the new bound, but do not reproduce that historical eight-functional optimization. The paper already proposes linear programming over regularizing functionals; the addition here is a concrete rational witness, lower number and all-spectrum certification within that method. No optimality, novelty or priority judgment is made.
