# Referee's source-based derivation and scope audit

The submitted identity survives as a formal identity of the leading-power double-light-cone coefficients. This statement does not identify that formal object with an exact finite-cross-ratio observable.

## Independent determinant construction

Use Belitsky–Korchemsky [2006.01831](https://arxiv.org/html/2006.01831v2), equations (29), (30), (35), (36), and (39). Expanding the two Bessel functions in the kernel on [0,1] gives a coefficient matrix C in the basis t^(ell/2+a). For k=ell+a+b+1,

    C_ab = (-1)^(a+b) g^(2k) q_k /
           [k a! b! (ell+a)! (ell+b)!],
    H_ab = integral_0^1 t^(ell+a+b) dt = 1/(ell+a+b+1),
    O_ell = det(1-C H).

The leading A^k coefficient of q_k, with A=log(z) on the source's null-log sheet, follows from the polylog formula (39) and the inversion polynomial in Stampedes I E.11. The code first evaluates the unsimplified finite sum from (39), then checks its simplification:

    [A^k] q_k = k! sum_{j=0}^{floor(k/2)} c_j B^(k-2j)/(k-2j)!,
    c_j = (2-2^(2-2j))*zeta(2j),  c_0=1.

Even zeta values are evaluated rationally with Bernoulli numbers; pi^2 is a formal rational parameter. This step uses no seed recurrence. The coupling scaling replaces g^(2k) A^k by L^k.

Cauchy–Binet expresses the r-particle sector as a sum over two increasing r-subsets a,b. Its L degree is r(ell+1)+sum(a)+sum(b). Thus r(r+ell)>N excludes an entire sector through degree N, and a bounded enumeration exhausts every term. The Gram minor has the exact Cauchy determinant

    det(H_b,a) = Vandermonde(a)*Vandermonde(b) /
                 product_{i,j}(ell+a_i+b_j+1).

The remaining small Hankel determinant has entries q_k/k. `ref_bessel.py` uses exact FLINT rational determinants of those minors, rather than the claimant's KPS matrix and power-series Gaussian elimination. Symmetry permits summing unordered subset pairs and doubling unequal pairs.

Fresh tests: N=32, ell=0,1,2,3, B=-3/2, 2/7, 31, 0, pi^2=7/3. Every one of the 528 coefficients agrees. These include five-particle contributions for ell=0 and ell=1. At each point, direct expansion of the proposed confluent hypergeometric function also agrees with its recurrence, including cancellation of all imaginary coefficients. The mixed derivative determinant is evaluated by permutations and exact series convolution. Four evaluation points alone do not certify polynomial equality for all B through degree 32; the all-order reasoning below is necessary.

The source's 30 table entries were separately reproduced from KPS (1.38)–(1.40), with symbolic ladders and the precise factorial normalization of Stampedes I (4.1). In particular c^(1)_(2,4)=1 and c^(0)_(2,4)=18/5. This tiny baseline audit is in `ref_source_audit.py`; it does not share the Bessel determinant implementation.

## All-order reasoning

Let D_nu=det(1-K_nu chi) for the Bessel kernel in 2006.01831 (23)–(25). The recurrence for J_(nu+2) gives, with r=sqrt(x), s=sqrt(y),

    (r/s) K_(nu+1)(x,y) = K_nu(x,y)
                         - J_nu(r) J_(nu+1)(s)/(2s).

This identity was also checked by exact symbolic substitution for arbitrary nu. Row and column factors cancel in each Fredholm minor, so unbounded analytic similarity at the origin need not be assumed. At nu=0 this is a rank-one perturbation. The determinant lemma and K_0(0,y)=J_1(sqrt(y))/(2 sqrt(y)) identify

    D_1/D_0 = Q(0),
    Q=(1-K_0 chi)^(-1) J_0(sqrt(x)).

This is precisely Q in [2003.01121](https://arxiv.org/html/2003.01121v4), equation (29). Its exact equation (30), rather than a strong-coupling approximation to that equation, is

    [(g partial_g + 2x partial_x)^2 + x + u-g partial_g u] Q = 0,
    u=-2g partial_g log(D_0).

The formal Bessel/moment expansion is regular at x=0. Consequently its x-derivative terms vanish there. For the common-symbol question, equations (20)–(21) of 2006.01831 show that the simplest/asymptotic numerator difference is suppressed by an inverse power of z in the relevant limit; it disappears under the stated projection.

The remaining delicate step is the coefficientwise scaling of D_0. Stampedes I E.1 and 2003.01121 (4)–(5) imply

    log D_0 -> -LB + pi^2 L^2/6.

At every weak-coupling order, the projected ladder coefficients are polynomials in both logarithms. Their products, formal inverses, and formal logarithms remain polynomial. A polynomial remainder vanishing as the null variable y tends to infinity for every fixed xi is the zero polynomial. This is why the null polynomial can be specialized to the single scaling without claiming a uniform analytic remainder at xi comparable to y. The leading-log projection preserves multiplication, and sends g partial_g to 2L partial_L. Terms with lower A degree vanish in this coefficientwise operation.

It follows that u=4LB-(4/3)pi^2 L^2 and u-2L u_L=-4LB+4pi^2 L^2. Substituting in the boundary equation gives

    L tau_LL + tau_L + (pi^2 L-B) tau=0.

The unit constant coefficient fixes the only regular formal solution: n^2 a_n=B a_(n-1)-pi^2 a_(n-2). The substitution tau=exp(i*pi*L) F(-2i*pi*L) turns this into Kummer's equation with parameter 1/2+iB/(2pi). This establishes the submitted expression within the stated projection. No new proof of the source's whole Toda hierarchy is required or supplied.

## Source sign and finite-B control

The published PDF page 28 really prints a minus sign in the standalone single-LCDS Gaussian. Page 27 E.1–E.2 instead gives the plus sign above: log(cosh(2pi g))/(8pi^2)=g^2/4-pi^2g^4/6+..., with an overall minus sign multiplying the squared logarithm. Independent Fredholm coefficients support the plus sign. In the fresh tests, the minus Gaussian disagrees in 101 of 132 coefficient entries. This is an internal source sign inconsistency, not an arithmetic failure of the submitted formula.

The full finite-B limit is a useful scope control. From the real Bessel symbol (20), at A -> infinity, L=g^2 A fixed, the symbol tends to

    chi(x) = (1+exp(-B))/(1+exp(x/(4L)-B)).

Its exact first moment gives

    [L] (D_1/D_0) = (1+exp(-B))*log(1+exp(B)),

whereas the submitted formal seed has [L] tau=B. At B=2 these are 2.414776415841358... and 2. Their difference is B exp(-B)+(1+exp(-B))*log(1+exp(-B)), invisible to every inverse-log order. Thus a literal finite-B interpretation would fail already at first order. CLAIM.md explicitly excludes these power corrections, and section 4 of the paper explicitly describes retaining the full inverse-log expansion. The control therefore limits interpretation without refuting the stated formal claim.

The trivial I0 control fails already at L^2: it gives B^2/4, while the verified seed gives (B^2-pi^2)/4. In the fresh tests it disagrees in 109 of 132 entries. The closed expression reorganizes an existing exact determinant; it does not improve its numerical accuracy or general coverage.

No statistical hold-out is claimed. The first displayed inverse-log corrections were fitting information. Configuration files document later exact comparisons, but their retrospective timestamps are not a sealed hold-out certificate, and no such certificate is needed or inferred for this formal identity.
