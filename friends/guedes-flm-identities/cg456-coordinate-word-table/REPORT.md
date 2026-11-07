# Independent referee rebuild of guedes_CG456

The length 1–4 certificate holds: all 360 claimed inverse images agree term by term with an independently written exact rebuild. No disagreement was found. This conclusion covers precisely the named polynomial quantity in the paper, under [Xhat_i,Xhat_j]=2i epsilon_ijk Xhat_k; it does not cover the certificate's lengths 5–6.

## Source and interpretation

Fresh sources downloaded on 2026-11-05:
- https://arxiv.org/pdf/1301.7750 and https://arxiv.org/src/1301.7750 (v2).
- https://arxiv.org/abs/1301.7750 confirms Carlos Guedes, Daniele Oriti and Matti Raasakka, J. Math. Phys. 54, 083508 (2013).
- https://arxiv.org/src/1502.06544 supplies the related Kupriyanov–Vitale all-order Weyl/Duflo construction.

Paper Sec. 5, immediately before 5.1, explicitly identifies coordinate star words with Q^{-1}(Xhat_i1 ... Xhat_in); ordinary products on the polynomial side are commutative. Section 5.2 defines the three maps. Section 5.2.1 and 5.2.2 PDF pages 26–27 and the FLM example on PDF page 29 were also rendered and visually checked. These correspond to printed pages 25–26 and 28. Local logarithm/hemisphere projections are inactive at identity, as the paper explicitly says after Eq. (5.1). No finite-spin quotient or Casimir substitution is imposed.

## Independent first method

`referee_forward.py` implements PBW reduction directly using only the commutator, with ordered basis Xhat_1^a Xhat_2^b Xhat_3^c. It averages all distinct permutations to build S on each monomial, then inverts each forward map by its triangular leading term. Every reconstructed answer is quantized again and checked against the ordered target word.

Let Delta=sum_i d_i^2 and E=sum_i X_i d_i. On input polynomials of degree <=4 the source definitions give exactly:

- Q_S = S.
- Q_D = S o (1 + Delta/6 + Delta^2/120), from sqrt(j)=sinh(sqrt(Delta))/sqrt(Delta).
- Q_F = S o (1 - E Delta/6). This follows by extracting coefficients of exp(i A(p^2) p.X), A(p^2)=asin(|p|)/|p|=1+p^2/6+O(p^4). Terms in O(p^4) first contribute at total degree five, and are therefore absent here.

All coefficients use exact SymPy rationals and i; no floating point, numerical fit or approximate equality is used. All 360 forward round trips pass. The independent table is constructed before the script opens the claimant certificate. No claimant or previous-referee implementation is read/imported.

## Independent second method

`referee_flm_action.py` uses only Python standard-library Fraction arithmetic and a separate polynomial representation. It never imports the first script. Differentiating the source's FLM p-addition law in its first argument at zero gives

L_i f = X_i sqrt(1+Delta) f + i sum_jk epsilon_ijk X_k d_j f.

For input degree <=3, sqrt(1+Delta)=1+Delta/2-Delta^2/8 is exact (the Delta^2 term is zero at these degrees). Applying L_i1 ... L_in to 1 reconstructs ordered words independently of PBW or forward-map inversion. Its 120 FLM words, including all 81 quartics, agree exactly with both the first rebuild and the claim. Ninety commutator controls on all ordinary monomials of degree <=2 pass: [L_i,L_j]f=2i epsilon_ijk L_k f.

## Exact comparisons

| Map | Length 1 | Length 2 | Length 3 | Length 4 |
| --- | --- | --- | --- | --- |
| Symmetric | 3/3 | 9/9 | 27/27 | 81/81 |
| Duflo | 3/3 | 9/9 | 27/27 | 81/81 |
| FLM | 3/3 | 9/9 | 27/27 | 81/81 |

The script checks record coverage and rejects missing/duplicate word-map records. `comparison.json` records the claimant certificate SHA-256, counts and zero disagreements. `rebuilt_forward.json` retains every reconstructed polynomial. `flm_action_results.json` records the separate comparison, and `rebuilt_flm_action.json` retains its table. `manifest.json` hashes sources, scripts and certificates.

Against the actual printed displays: all 27 quadratic map/cases agree; symmetric cubics agree 18/27, Duflo 12/27 and FLM 27/27. The 24 printed disagreements are fully recorded in `comparison.json`. Rebuilt minus printed is -delta_ik X_j for symmetric and -delta_ik X_j - i epsilon_ijk/3 for Duflo. These are discrepancies in the paper's examples, not discrepancies with the claimed corrected table.

Decisive controls, fixed external index 1:
- Symmetric inverse of Xhat_1^3 is X_1^3; the printed cubic gives X_1^3+X_1.
- Duflo inverse of Xhat_1^3 is X_1^3-X_1; the printed cubic gives X_1^3.
- Quartic inverse images are X_1^4 (symmetric), X_1^4-2X_1^2+7/15 (Duflo), and X_1^4+4X_1^2 (FLM). The latter two also follow immediately from the one-axis source plane waves.

There is no published prediction score, gain, data split or hold-out here; SBS and ML baselines do not apply. The trivial pure-power control exposes the printed cubic discrepancy but does not invalidate the explicit table. Relative to the paper, the artifact supplies an explicit complete quartic list and corrected cubic evaluations; the maps themselves are already defined at all orders. Related prior machinery appears in Kupriyanov–Vitale (2015), including its all-order Duflo gauge factor. No improved published numerical benchmark or open-problem solution is asserted by this audit. Public-source search limits are recorded in PRIOR_ART.md.

## Reproduction

From this job directory, run sequentially:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 10 .venv/bin/python referee_forward.py > forward.log 2>&1
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 10 .venv/bin/python referee_flm_action.py > flm_action.log 2>&1
```

Both completed successfully in under one second each as reported by the execution tool. No pool, compiler, GPU, package installation or long-running worker was used. Total public downloads were about 0.56 MB; retained files are well below 50 MB. A first run's printed-comparison helper encountered SymPy's rejection of rational-times-Python-bool; converting the equality indicators to integers fixed it. This did not change the algebraic rebuild or its independent comparison. The initial log was replaced by the final successful run.

Strongest author objection: these are finite evaluations of established maps; errors in cubic displays may be typographical and do not refute the all-order construction. Agreed; the claim under review is the table's exact correctness.

NEXT BAR: extend the separate Fraction-only differential-action method to symmetric and Duflo and check all 81 quartics for each, providing independent second-method coverage for all three maps.
