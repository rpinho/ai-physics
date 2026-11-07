HOLDS
Referee: gpt-6.1-sol

The printed symmetric and Duflo cubic examples contradict their own defining maps.
Fresh [arXiv v2](https://arxiv.org/abs/1301.7750v2) and the [journal PDF](https://pure.mpg.de/rest/items/item_1671208/component/file_1859595/content) contain the claimed expressions; both name Carlos Guedes, Daniele Oriti and Matti Raasakka.

| Map | Quadratics agreeing | Cubics agreeing |
| --- | --- | --- |
| Symmetric | 9/9 | 18/27 |
| Duflo | 9/9 | 12/27 |
| FLM | 9/9 | 27/27 |

Computed minus printed: symmetric −δ_ik X_j; Duflo −δ_ik X_j − iε_ijk/3; FLM zero.
Decisive control: S⁻¹(Xhat₁³)=X₁³, while the display gives X₁³+X₁.
Duflo gives X₁³−X₁ from (1−Δ/6)X₁³, while its display gives X₁³.

Ran independently written referee_pbw.py and referee_plane_waves.py: exact forward-map inversion in U(su(2)) and separate local SU(2) plane-wave differentiation agree in all 108 quadratic/cubic cases.
No proposing search/verifier code was read or imported. Transcription, commands and per-word results are retained locally in REPORT.md and the JSON files.

The paper uses [Xhat_i,Xhat_j]=2iε_ijk Xhat_k, ordinary polynomial products on the right, and unrestricted external indices. Ordering, epsilon sign and logarithm projection cannot remove the pure-power contradiction; the projection is inactive at identity.
Hold-out, ML scores and SBS: not applicable to this exact algebra claim.

Fresh arXiv v1 has the same defective lists; latest listed version is v2 (2013). No erratum was located in arXiv, Crossref, INSPIRE or title/DOI searches as of 2026-11-05. Publisher access returned 403; journal evidence is the institutional copy.
Relative to the paper: two example identities need correction. Related existing machinery appears in Kupriyanov–Vitale, [arXiv:1502.06544](https://arxiv.org/abs/1502.06544), Eq. (6.13), with the same Duflo factor after normalization; no explicit correction was located there.

Strongest author objection: these may be typographical errors confined to examples; this audit does not refute the paper’s general construction.

NEXT BAR: publish corrected symmetric and Duflo cubic identities that agree with their defining maps for all 27 index triples.
