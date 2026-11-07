# Referee source audit (2026-11-03)

Before independent code: primary benchmark is Figure 3 and equations (26),
(50)-(58), (80)-(83) of Alho and Uggla, arXiv:2407.14378v3,
https://arxiv.org/html/2407.14378v3 . The arXiv authors and version record
independently confirm Artur Alho and Claes Uggla (published PRD 111, 083549).
The abstract's ~0.1% is an approximate scale, not a precise table entry.
The claimant's reproduction reports p=1 Omega_m 0.2672536%, E 0.1338952%;
p=.1 Omega_m 0.0207265%, E 0.0103649%. These await my independent check.

The later review https://arxiv.org/html/2511.02727v1 is by Alho,
Bernholm and Uggla, submitted 2025-11-04, and retains the low-degree method.
Chiba https://arxiv.org/abs/0909.4365 is an earlier tracker expansion.
No dedicated leaderboard is identified; the paper's plots supply the benchmark.

I read the claimant's dated PRIOR_ART.md as untrusted audit data: GitHub
repository searches sorted updated, issues/PRs, named AI-lab result indexes,
last-year arXiv papers and eight citing papers found no like-for-like higher
tracking result. GitHub code search requires sign-in; X yielded an app shell
and Reddit denied access. These are coverage gaps, not absence evidence.
This referee makes no novelty/priority or global-best assertion. Independent
public searches and numerical reproduction will be recorded below.

## Independent follow-up

Primary Figure 3 PNGs were downloaded and visually read: horizontal axis is
0<=z<=6, vertical axes are relative fractions, and the thick dotted peaks
are consistent with 0.00267 (Omega_m) and 0.00134 (E), not 0.001 for both.
The baseline and printed numerical w0,wa have now been independently reproduced.

Important antecedent for the separate taste review: section 2.5, footnote 6
of the primary paper already PRINTS the density Padés [1/2] and [2/1] and
explains that their T0 normalization requires a quadratic equation. Thus the
paper already discusses higher degree and the complexity tradeoff. These
are density approximants, not the submitted degree-6 equation-of-state
formula or its interval certificate. Their normalization-only controls and
their direct-density formulas were run independently in source_controls.py.
Neither matches the degree-6 gain. In relative Omega_m fractions, the
normalization versions give 0.000965/0.001404 at p=1 and
0.0001641/0.0001637 at p=.1; direct density versions are worse. These extra
controls are floating diagnostics, not certified maximum values.

The public 2024 talk by Alho in collaboration with Uggla,
https://indico.cern.ch/event/1346918/contributions/6027658/attachments/2901398/5088191/AAlho_QuintApprox_22_07_2024.pdf ,
slides 14-16, already describes unstable-manifold expansions followed by
Padé construction as a general procedure. It displays the same gamma,beta
tracking coefficients, not a degree-6 tracking accuracy result.

Independent 21:31-21:32 UTC public fetches: exact arXiv ID and quintessence
Pade GitHub repository searches sorted updated, plus exact-ID issues search,
all returned zero items. BakeLab/Epi-results, both DeepMind result/problem
README indexes, openai/math CONTENTS, EinsteinArena, plasma-ai/erdos and
kisonecat/openai-math indexes were fetched. Initial DeepMind API requests
were rate-limited; raw README fallbacks succeeded. No target result was
identified in these indexes. X returned a generic app page; Reddit 403.
Web searches found the source talk and broad quintessence codes, not a
like-for-like higher tracking error number. No authentication or contact.
Exact responses, UTC timestamps and SHA-256 are under pod_results/sources/.
The claimant's more extensive citing-paper/past-year-arXiv audit remains
secondary context; I do not represent it as independently reproduced.

Final independent refresh at 21:47:00-21:47:03 UTC: primary paper/review,
the two repository searches and issues/PR search, and every named AI index
above all returned HTTP 200. Search counts remain zero; paper/review and
index body hashes match the earlier successful fetches. Exact replies are
retained in pod_results/sources/end/. No stronger like-for-like result was
identified; access/coverage limitations and the absence of a novelty judgment
remain unchanged.
