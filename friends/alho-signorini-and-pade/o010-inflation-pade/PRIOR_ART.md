# Prior-art audit — independent referee, 2026-11-03

Scope: verify an existing finite-n endpoint certificate, not construct a new record.
Primary target: Alho, Hell and Uggla, arXiv:1503.06994v2, Table 1 and equations 66–79.
The claim identifies the paper's Hubble [2/2] (76b), rather than the printed 31% row,
as its strongest tested public n=20 baseline (claimed error 0.386567606987%).
These statements are unverified at this initial checkpoint.

Planned public checks: primary paper and author metadata; recent related papers;
GitHub recent code, issues and public agent-result repositories; indexed community
references. There is no identified live competitive scoreboard for this problem.
No novelty or priority determination is part of this referee assignment.
The independent baseline will be derived directly from the primary equations on mscr.

Public checks completed before independent construction: arXiv abstract and publicly
redownloaded v2 PDF confirm Artur Alho, Juliette Hell, Claes Uggla as authors.
PDF SHA256 aa6db55dc999b20109e8a81bfee1c4ea6da27e70cefe0df0902598070130994b,
identical to the submitted source copy. Table 1 is a static comparison, no live
leaderboard/open benchmark PR found. GitHub repository API (sort=updated, exact ID)
was rate limited; indexed exact-ID GitHub and community X/Reddit queries returned
no matching result. Indexed searches including BakeLab/Epi, DeepMind alphaevolve_results
and repository_of_problems, openai/math, EinsteinArena, plasma-ai/erdos and
kisonecat/openai-math found no matching result. These are coverage limits, not
proof of absence. No awesome-list or dedicated monomial endpoint code found.
Recent-paper query: monomial Padé Alho 2025 2026; no matching improved endpoint table.

Relevant prior methods: the primary paper p23 explicitly recommends higher-order
Padé and nonlinear changes of variables; equations (70),(76) give Hubble expansions.
Alho–Uggla (2015), arXiv:1406.0438, is its quadratic predecessor.
Álvarez–Medina, arXiv:2304.05650v5 (JHEP10(2024)028), develops adapted slow-roll
expansions and Padé summation, including monomial potentials; examples are T-models.
This referee will reproduce (66),(68),(76) and test the elementary equal-degree
Hubble [4/4] and plain Taylor controls before interpreting the inverse-variable gain.

URLs: https://arxiv.org/abs/1503.06994 ; https://arxiv.org/pdf/1503.06994v2 ;
https://arxiv.org/abs/1406.0438 ; https://arxiv.org/abs/2304.05650 ;
https://api.github.com/search/repositories?q=1503.06994&sort=updated

Independent baseline reproduction completed on mscr: printed Table 1 integers
match tangency curves; literal eq66/68 give different, stronger numbers. Exact
Hubble [2/2] via eq72 gives 0.386567606987%, but eq81 with that same explicitly
printed Padé gives 0.0493857898153%, also beaten by the claimed certificate.
A routine degree extension of eq81 to Hubble [4/4] gives certified error below
0.000004789186%, beating the claim's inverse [4/4] at the same coefficient count.
These control numbers are new computations in this referee report, not asserted
previously published results. No novelty or priority verdict follows from them.

Final public recheck 2026-11-03 about 22:00 UTC: exact-ID + 2026 + Padé,
exact-ID GitHub agent repositories, and monomial/Hubble/Padé/n=20 queries produced
no additional matching table. GitHub API remains unauthenticated/rate limited.
The decisive control is derived from the already cited primary source, not from
an absence-of-search-results claim.
