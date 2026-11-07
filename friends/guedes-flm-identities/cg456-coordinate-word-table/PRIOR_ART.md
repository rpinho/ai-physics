# Prior-art check (2026-11-05)

Scope: independent audit of the three quantization maps in Guedes, Oriti and Raasakka, arXiv:1301.7750, Section 5.2; exact coordinate words of lengths 1–4. No search for improved bounds or novelty is intended.

Primary source to retrieve fresh: https://arxiv.org/abs/1301.7750 and https://arxiv.org/pdf/1301.7750 . Related prior machinery named by the claim: Kupriyanov–Vitale, https://arxiv.org/abs/1502.06544 , Eq. (6.13).

The source paper defines all orders; the claimed contribution is an explicit table, correcting two cubic displays. There is no numerical scoreboard identified in the claim. Public code, recent literature, agent-result repositories and community searches will be logged below before any independent implementation is written. The proposed reference baseline is direct inversion of the source-defined quantization maps; this audit will not import claimant code.

## Public sweep before implementation
- Fresh arXiv abstract confirms Carlos Guedes, Daniele Oriti and Matti Raasakka, JMP 54 (2013) 083508, v2 dated 2013-09-27. PDF and TeX source downloaded locally (about 0.55 MB combined).
- Best reference construction: the primary paper's all-order symmetrization, Duflo factor and FLM plane waves. No scalar performance record or official leaderboard applies.
- Related source: Kupriyanov–Vitale, arXiv:1502.06544, https://arxiv.org/abs/1502.06544 . Its abstract describes an all-order Weyl differential representation and Duflo-related gauge operator.
- GitHub repository searches for Guedes+Duflo and Duflo+2026, sorted updated, failed with cache miss; indexed GitHub searches for Guedes/Duflo/star-product supplied no relevant code. This is a search limitation, not proof of absence.
- Indexed searches named BakeLab/Epi-results, google-deepmind/alphaevolve_results, openai/math, EinsteinArena, kisonecat/openai-math and plasma-ai/erdos with Duflo. No topic match surfaced. AlphaEvolve's live README was checked: https://github.com/google-deepmind/alphaevolve_results . No relevant scoreboard was identified. This is a limited indexed sweep, not a full repository-content audit.
- Recent arXiv queries for Duflo/star products in 2025–2026 and Guedes/quantization/erratum did not identify a replacement table or correction. Queries often returned unrelated people named Guedes or Duflo; these were excluded.
- Public community query (X, Reddit, blogs) found no relevant correction. The indexed nLab research bibliography https://ncatlab.org/zoranskoda/show/ncFourier points back to the primary paper and Freidel–Majid (2008), hep-th/0601004. No account, contact or post was made.
- Read claimant REPORT.md and REPRODUCTION_FINDING.md as claims, and certificate JSON as data. No proposing implementation was read. Earlier referee verdict is background only; its code/results are not being reused.

Reproduction plan: independently implement forward symmetrization and polynomial-map inversion; reconstruct FLM forward map from its local plane wave. Separately derive a differential left-action for FLM from the source group law and check all 81 quartics. These are two mathematical routes, not a search for an improvement.
