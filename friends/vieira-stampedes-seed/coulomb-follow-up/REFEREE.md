# Independent referee of the seed's physical interpretation

**Verdict: the radial Coulomb interpretation and its stated mathematical consequences hold, within the projected sector. No independently established new physical phenomenon.** This check was written separately from the main computation, without importing its implementation or the earlier X004 worker/referee code.

## Direct answer and exact mapping

For real L>0 and B, divide the proposed ODE by L. It is exactly the m=0 radial equation of the two-dimensional operator

    H_B = -d_L^2 - L^(-1) d_L + B/L,    H_B tau = pi^2 tau.

Here L is radius, B is Coulomb coupling, and the energy is the fixed number pi^2, in units hbar^2/(2m)=1. The potential is repulsive for B>0. It is not the usual three-dimensional hydrogen s wave, nor a bound-state spectrum with B as energy. The origin condition selects the regular, no-log branch: tau(0)=1 and tau'(0)=B. Removing the radial measure, u=sqrt(L)tau satisfies

    -u'' + [B/L - 1/(4L^2)]u = pi^2 u.

The extra critical inverse-square term is essential. The usual regular boundary excludes sqrt(L)log(L). Setting rho=pi L and eta=B/(2pi) gives the Coulomb equation of formal angular momentum ell=-1/2. Continuing the [DLMF regular normalization, Eqs.33.2.4–5](https://dlmf.nist.gov/33.2#ii), to ell=-1/2,

    tau(L,B) = F_{-1/2}(eta,rho)/(C_{-1/2}(eta)sqrt(rho)),
    C_{-1/2}(eta)^2 = pi/(1+exp(B)).

This is an exact special-function/Schrodinger dictionary, not a derived microscopic Hamiltonian for a new particle in SYM. In particular, the literal two-dimensional electrostatic potential of an isolated point charge would be logarithmic; the operator here is the mathematically standard 1/r Coulomb potential restricted to a plane.

## Consequences derived independently

At fixed real B, the [DLMF large-rho Coulomb expansion](https://dlmf.nist.gov/33.11), continued to ell=-1/2, gives

    tau ~ sqrt(1+exp(B))/(pi sqrt(L)) sin[pi L - eta log(2pi L)
                                                    + pi/4 + arg Gamma(1/2+i eta)],

with additive O(L^(-3/2)) corrections for fixed B (and continuous Gamma phase). At B=0 it reduces exactly to J0(pi L), including the Bessel phase and amplitude. The factor 1+exp(B) comes from the Gamma reflection identity, not an independent identification of a thermal stampede.

Every positive zero is simple and moves strictly to larger L as B increases. If r_n(B) is such a zero,

    dr_n/dB = integral_0^{r_n} tau(L,B)^2 dL / [r_n tau_L(r_n,B)^2] > 0.

Proof: write (L tau')'+(pi^2 L-B)tau=0, differentiate in B, and set v=partial_B tau. Then [L(tau v'-tau'v)]'=tau^2. The regular origin contributes zero boundary Wronskian. At a zero, differentiating tau(r_n(B),B)=0 gives the formula. For example the first zeros at B=0,2,5 are respectively 0.76547974956201235684, 1.13298306096691880155, and 1.62076904982393453201.

For the strict double-scaling limit x=LB fixed, L tends to zero and B to infinity. The equation becomes x f''+f'-f+(pi^2/B^2)xf=0. Dropping the vanishing energy correction gives f=I0(2sqrt(x)), precisely Stampedes II's seed. This explains why its strict limit loses the term that distinguishes the present equation.

## What was recomputed

Run `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 10 .venv/bin/python code/referee_check.py`. Output is `data/referee_check.json`.

The code starts from the defining exponential and Kummer power series, using their finite Cauchy product. It independently transcribes the Bessel formula in Stampedes I arXiv v2 Eq.(93), Appendix E, PDF p32/printed p31. Its pi^0, pi^2 and pi^4 families give 39 exact rational symbolic coefficient identities through L^14. These all hold. Fourteen coefficients obey the proposed ODE. Exact generic substitutions verify Kummer's equation, the radial reduction, and the moving-zero Wronskian identity.

As a distinct numerical representation, Euler's beta integral gives

    tau = cosh(pi eta)/pi integral_0^pi
                    cos[rho cos(theta)-2 eta log(cot(theta/2))] dtheta.

Direct quadrature agrees with Kummer evaluation at (L,B)=(1/8,2),(5/4,2),(7/2,-1), to over 40 decimal places. At twelve zeros (first three at B=-2,0,2,5), implicit differentiation agrees with the positive Wronskian integral. Large-L examples at L=20.25,100.25,1000.25 illustrate the stated Coulomb phase/amplitude. These are mathematical corroboration, not comparisons to new observed octagon data. No predictive accuracy score or trained predictor is involved.

## Other proposed pictures

A direct nonnegative-probability interpretation of tau on all L>0 fails: even B=0 gives J0(pi L), which changes sign. The differential part D=L d_L^2+d_L is a valid squared-Bessel backward diffusion generator (dX=dt+sqrt(2X)dW), but the complete equation is (D+pi^2 L)tau=B tau. It is a spectral equation with a growth/weight term, not a normalized Fokker-Planck evolution equation. This does not forbid more elaborate weighted stochastic representations; none establishes the stampede's microscopic randomness here.

A first-order two-component system can always be built from this scalar ODE. Calling that a transfer matrix does not identify it with the spin-chain Hamiltonian or an existing physical transfer matrix. Similarly the seed together with the already published mixed-derivative determinant generates the Toda hierarchy, but this ODE alone neither derives the Toda structure nor proves a new Painleve reduction. Those additional physical explanations have not been established by this check.

## Independent full-text reading relevant to equivalents

I read Stampedes I Appendix E and all nine pages of [Stampedes II](https://arxiv.org/abs/2205.04476), plus the following full papers including appendices and references:

- [Spinning Hexagons, 2207.08931](https://arxiv.org/abs/2207.08931), 41 PDF pages. Eq.(42) gives two Pfaffians for asymptotic three-spinning structure constants. Eqs.(56)-(57), PDF p32/printed p31, relate their large-spin limit to Wilson-loop/pentagon observables; explicitly evaluating that limit is future work. No seed-equivalent differential equation or Kummer answer occurs.
- [Complex Spin: The Missing Zeroes and Newton's Dark Magic, 2211.13754](https://arxiv.org/abs/2211.13754), 14 PDF pages. Appendix F, PDF p13, already uses the hydrogen/Coulomb scattering analogy for Regge trajectories. Its f_S(E)=Gamma(1+S-eta)/Gamma(1+S+eta), eta=1/sqrt(-E), and Eq.(F1) residue zeros concern three-dimensional orbital spin and missing bound states. They are not this octagon's two-log seed or zeros versus L. Do not claim the first Coulomb analogy in Vieira's work.
- [Light-Ray Wave Functions and Integrability, 2409.02160](https://arxiv.org/abs/2409.02160), 52 PDF pages. Its tau(u) in Eqs.(21)-(25) is a polynomial transfer-matrix eigenvalue in spectral rapidity u; Eq.(24) is third-order in the angular parton coordinate theta and depends on spin S and charge q. Fourier recursion (27) has cubic-in-mode coefficients. Appendix C, Eqs.(111)-(118), constructs Baxter Q integrals and recovers Janik's twist-two function. These are not the second-order two-log seed, even though tau, hypergeometric functions, and differential equations appear.
- [The Loom for General Fishnet CFTs, 2212.09732](https://arxiv.org/abs/2212.09732), 42 PDF pages. Conclusions, PDF p36/printed p35, fourth bullet, asks how to count stampedes on M-Loom diagrams. It gives no seed-equivalent octagon formula or Coulomb radial equation. The classification of chiral integrable graphs and tT spectral reality is distinct from the present seed.

Stampedes II, first page, Eq.(2) and following paragraph, expressly has seed I0(2s) and leading-log cusp scaling, not all inverse-log corrections. Its random walks in Weyl chambers, Appendix E Eq.(25), concern this stricter Bessel-determinant limit. These do not supply the corrected Kummer seed. This reading supports a narrow absence statement for these papers, not exhaustive literature novelty.

## Novelty assessment

The exact radial dictionary, Coulomb phase, and zero-delay identity are useful explanatory consequences of the seed. They are standard consequences of the already identified confluent hypergeometric function. None of the checks here tests a new physical prediction on new data, beats a printed numerical target, or derives the missing microscopic Toda/spin-chain mechanism. I recommend `NEW: no` for a new physical-result claim from this check alone. The parent should separately judge whether the existing seed resummation still settles the stated printed open problem after its full prior-art search. An absence in the selected papers does not prove priority. Large-L zeros of a resummed leading-power projection must not be presented as zeros of the literal finite-cross-ratio octagon without a uniform control of the discarded terms.

## Additional author-scope cross-check (requested separately)

I retrieved and read both remaining papers in full, including supplements and references. Their PDFs and extracted full text are in `sources/2210.04923.pdf`, `sources/2210.04923.referee.txt`, `sources/2404.10812.pdf`, and `sources/2404.10812.referee.txt`.

- [Structure Constants in N=4 SYM and Separation of Variables, 2210.04923](https://arxiv.org/abs/2210.04923), 14 PDF pages: Eqs.(2)–(6) are finite-dimensional SoV overlaps of Baxter functions for three-point functions, with one-particle measure proportional to sech²(pi u). Appendix B Eq.(B1) gives Hahn 3F2 polynomials, and Eqs.(9)–(10)/(B5) are finite-difference Baxter equations in spectral rapidity u. These are not the Kummer 1F1 two-log octagon seed. The discussion on PDF p7 specifically proposes recasting Coronado's four-point octagon in this SoV language as future work, possibly using its existing determinant; the large-spin/Wilson-loop connection is likewise prospective. No equivalent Coulomb radial equation or resummation of the Appendix E inverse-log seed appears. The overlap ratios concern individual OPE structure constants, not the summed four-point bridge ratio O1/O0.
- [Multiparticle Flux Tube S-matrix Bootstrap, 2404.10812](https://arxiv.org/abs/2404.10812), 18 PDF pages: this studies collinear Goldstone/branon jets on the confining flux tube of primarily three-dimensional Yang-Mills theories. Eqs.(3)–(5) define jet states; Eq.(7) defines finite-energy S-matrix observables at s=i; Eq.(11) is a conformal-map scattering-amplitude ansatz. Supplement S4 concerns a Nambu–Goto effective string, with tau(x)=x(1-x)(1-x+x²) in Eq.(S4.7) just a jet energy-fraction polynomial. None is an N=4 null-polygon/light-cone octagon seed, and no Kummer, Whittaker or Coulomb equivalent occurs. The shared phrase 'flux tube' refers to a different physical problem and supplies no missing microscopic interpretation for the Stampedes seed.
