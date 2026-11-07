# Independent referee: stated bounds verified

Both independent continuous certificates returned PASS, with exit status 0.
The p=1 audit covered 6067 y cells; p=1/10 covered 9112. Each tracker tube
was checked on 2048 intervals at 192-bit precision with radius 2e-7.
The certified relative error upper bounds (fractions) are:

| p | degree | Omega_m | E |
|---|---:|---:|---:|
| 1 | 6 | <3.294e-6 | <1.647e-6 |
| 1/10 | 6 | <3.010e-6 | <1.505e-6 |
| 1 | 2 | <2.173e-5 | <1.087e-5 |
| 1/10 | 2 | <1.013e-5 | <5.063e-6 |

Thus every submitted p-specific degree-6 limit, and its common limits
Omega_m <0.0014% and E <0.0007%, holds. These are conservative uniform
upper bounds, not exact maxima. The independent proof and implementation
are INDEPENDENT_PROOF.md and interval_ref.py. The actual receipts are
pod_results/interval_1.json and interval_1_10.json.

At the exact true density x=2/5, all four interval-enclosed control errors
are strictly larger than the degree-6 uniform bound for both metrics and
both p values. This proves strict reduction in maximum error without
needing certified exact baseline maxima or pointwise dominance.

After the interval audit, the exact source-series and coefficient comparison
and the independent numerical solver were rerun on the same retained inputs
(pod_results/numerical_final.log). All comparisons passed again.

No claimant search or verification module is imported or run. The four input
JSON files are proposed coefficients, not trusted computation. `referee.py`
derives its series directly from equations (50)-(55) of the primary paper:
https://arxiv.org/html/2407.14378v3 . Set q=p/(p+2), A=u/sqrt(q), B=v/sqrt(q),
H=3q*tildephi. Then

H_N=(6q/p)ABH,
A_N=(3/2)(2-qA^2)(B-A),
B_N=(3/2)[(1-qA^2)(1-B^2H)-(2q/p)AB]B,
Omega_phi=B^2H and w=qA^2-1.

For k=6/(p+2), replace d/dN with kT*d/dT, fix H_1=1, and solve each
coefficient's 2x2 rational linear system. All 13 coefficients of A, B,
Omega_phi and w match the submitted data exactly. Separate exact Gaussian
elimination reproduces the [2/2] and [6/6] numerators and denominators.

The floating reference instead integrates Friedmann plus Klein-Gordon in
X=phidot/(sqrt(6)H), Y=sqrt(V)/(sqrt(3)H), ell=log(p/phi), log(E).
Its equations are written explicitly in referee.py. Raychaudhuri integration
of E checks the dust identity independently to 1.6e-14. Three past starts
Omega=1e-8,1e-10,1e-12 agree within 3.6e-15 in Omega over the test interval.
These diagnostics are floating computations, not uniform proof.

Numerical relative errors (fractions, multiply by 100 for percent):

| p | method | Omega_m | E |
|---|---|---:|---:|
| 1 | published [1/1] | 0.00267253612456 | 0.001338952454 |
| .1 | published [1/1] | 0.000207264881719 | 0.000103648552 |
| 1 | normalization-only [1/1] | 0.000690257893678 | 0.000345307721 |
| .1 | normalization-only [1/1] | 0.000182315611361 | 0.0000911702710 |
| 1 | [2/2] | 0.000020781144652 | 0.0000103907342 |
| .1 | [2/2] | 0.000009586529539 | 0.00000479329914 |
| 1 | [6/6] | 2.64e-11 | 1.32e-11 |
| .1 | [6/6] | 1.36e-10 | 6.78e-11 |

The last two rows are not certified exact maxima. wCDM and LambdaCDM errors
are also much larger (see numerical JSON). Exact controls at one true density
will be checked against a uniform candidate upper bound in interval_ref.py.

The source's eq. (72) defines precisely these relative errors, and Fig.3 uses
Omega_phi0=.68, p=1. The adjacent text supplies p=.1 and approximate E errors.
Eq. (58a) has an inconsistent leading minus sign/prefactor; eq. (26b),
(58b,c), (81),(82), and the printed approximate w0=-.7519 determine the
consistent intended tracking formula. The claim explicitly uses that formula.
The source's numerical w0=-.7581, wa=.1080 are reproduced.

The extension raises the degree and replaces the paper's approximate T0 with
R(T0)=17/8. It preserves the physical present density and requires no fitted
trajectory values. It is therefore a different approximation to the same
physical quantity and orbit. The normalization-only control retains a clear
error, so normalization alone does not explain the degree-6 gain.

No dataset was split, and no unseen observational test is claimed. I read the
pre-construction plan/config as protocol evidence; their local timestamps are
not an independently attested historical record. This does not affect a
deterministic full-interval certificate.

Reproduce on mscr through the supplied helper:
`python3 transport.py push` launches referee.py; `python3 transport.py push interval_ref.py`
launches the interval audit. Poll with the helper and poll.sh, then
`python3 transport.py pull`. All science computation is on mscr, nice 10,
BLAS thread caps 1, with two interval workers for the two potentials.
Sources and exact receipts are copied under pod_results/.

Additional skeptical controls use the primary paper's footnote 6. Its printed
density [1/2] and [2/1] formulas were used both directly (normalizing density
at N=0 and obtaining E from dust conservation) and only to set T0 in the
source's [1/1] equation-of-state approximation. Their numerical Omega_m
errors are respectively 2.60%/3.36% and .0965%/.1404% for p=1;
.345%/.352% and .01641%/.01637% for p=.1. These are floating diagnostics.
None explains the degree-6 accuracy. The paper already discusses higher
degree, which is a relevant antecedent for the separate taste reviewer.

Relative to the paper, the deliverable supplies order-12 rational series,
degree-6 w Padés, self-consistent density normalization and a continuous
certificate for these two specified examples. The paper's footnote 6 and
Alho's public 2024 talk already discuss higher-degree Padé constructions.
The later review retains [1/1]. No novelty, priority or author-interest
judgment is made. Public-search scope and access gaps are in PRIOR_ART.md.

The scientific code ran only on mscr, at most two simultaneous CPU workers.
Startup free disk was 87.7 GB. Before cleanup, all 59 files in the pod's
SHA256SUMS.json manifest (4,799,262 bytes) were copied here and hash checked;
COPY_RECEIPT.json records this check. Public HTML/PDF/plot/API responses,
exact coefficients, code, logs and certificates are retained locally.
The final process/cleanup receipt is pod_results/process_check.json.
It confirms no active referee science workers and a remaining pod directory
size of 192,931 bytes (272 KB allocated), after removing the copied temporary
public downloads. Local evidence, including original source bodies, remains
under 5 MB. The work finished within the three-hour box.

Scope objection: only two fixed p values are certified. A concrete next
bar is a uniform certificate for every p in [0.1,1], with the same present
density and redshift interval. No observational fit or held-out-data
generalization is established by this deterministic calculation.
