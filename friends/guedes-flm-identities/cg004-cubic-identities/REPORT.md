# Independent exact audit

The narrow claim holds: the displayed symmetric and Duflo cubic lists
conflict with the quantization maps defined in the same paper. The
counts and discrepancy tensors in CLAIM.md are reproduced exactly.
No conclusion about the rest of the paper follows from this audit.

Primary sources, independently downloaded on 2026-11-05:
[arXiv v2](https://arxiv.org/abs/1301.7750v2),
[journal version of record](https://pure.mpg.de/rest/items/item_1671208/component/file_1859595/content).
Visual transcription and page locations are in TRANSCRIPTION.md;
the PDFs and page images are retained. The title, authors, normalization,
operator-word interpretation, and both plane-wave definitions were checked.
Direct publisher access returned 403. Latest arXiv version is v2 (2013).

Reproduce from this directory, sequentially:

```sh
nice -n 10 .venv/bin/python referee_pbw.py
nice -n 10 .venv/bin/python referee_plane_waves.py
```

The first program constructs a 20-dimensional exact PBW basis through
degree three and the three forward quantization matrices. It inverts
these matrices over Q(i), checks every roundtrip in U(su(2)), and compares
every quadratic/cubic word with our transcription. The Duflo quadratic
factor is independently derived from tr(ad_X^2)/48. The forward FLM map
is extracted from its defining exponential, rather than a proposed table.

The second program imports none of the first program. It multiplies
explicit 2x2 SU(2) group exponentials in an exact ring where each independent
parameter squares to zero, recovers the local group coordinates, and
differentiates the three inverse plane waves. X remains a free commuting
polynomial variable; Pauli group coordinates do not quotient U(su(2))
by a spin-1/2 representation. All 108 map/word cases agree between programs.

All quadratics agree (9/9 per map). Cubic agreements are symmetric 18/27,
Duflo 12/27, FLM 27/27. The separately fitted discrepancy tensors are:
S: -delta_ik X_j; D: -delta_ik X_j - i epsilon_ijk/3; FLM: zero.
Detailed actual/printed/difference records: pbw_results.json and
plane_wave_results.json. There is no floating-point tolerance.

The decisive trivial control is a single repeated coordinate. S must
give X1^3, but the displayed cubic gives X1^3+X1. The Duflo inverse
factor 1-Delta/6 gives X1^3-X1, but the display gives X1^3. Direct
one-variable plane-wave Taylor coefficients separately check both.
There is also an associativity obstruction in the printed Duflo list:
its printed triples 123 minus 213 give 2i X3^2, whereas its own quadratic
and [X1,X2]=2i X3 require 2i(X3^2-1/3). This detects the missing scalar.

Reversing generator order or epsilon orientation cannot fix the repeated
coordinate witness. Rescaling structure constants cannot alter the
symmetrization of a pure power. Reinterpreting RHS juxtaposition as star
multiplication contradicts Eq. (28), Eq. (54), and the displayed quadratic.
The projection of plane waves is inactive near the identity, explicitly
noted after Eq. (54). These are unrestricted external indices, not a
stated distinct-index case. No convention actually used in the paper
rescues the two displayed lists.

Correction history and prior related work: PRIOR_ART.md. Fresh arXiv v1
also has the defective lists; no published correction was located in
the checked sources. No hold-out, fitted score, gain, or SBS applies.
The strongest author response is that only the examples contain typos;
the general construction may remain valid. This audit does not settle that.

NEXT BAR: publish the two corrected cubic identities, checked against
the defining maps for all 27 index triples.
