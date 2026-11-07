# Prior-art audit for independent referee alho_O004

Started 2026-11-03. This is a referee audit, not a new-record search.

Primary baseline to verify: Alho–Calogero 1907.09970v2 §6.4 and
Alho–Calogero–Liljenberg 2104.11131v2 §3.4, Figure 8, question (a).
Claimed published evidence: numerical finite-radius Signorini balls for
central density ratio 2 at Poisson ratios -0.5 and 0.25; no certified radius
table. Generic Beig–Schmidt small-body existence predates the claim.

Required audit queue: primary definitions and author lists; live primary
paper/repository sources and issues; recent GitHub search; AI result repos
(BakeLab/Epi-results, DeepMind alphaevolve_results/repository_of_problems,
openai/math, EinsteinArena, plasma-ai/erdos, kisonecat/openai-math);
recent arXiv and primary references; public community results.
No general leaderboard is known for this existence question. URLs, receipts,
access limitations, and the baseline reproduction will be recorded below.

Independent code will be written from the primary definitions, without
importing the claimant's search or verifier code. Scientific computation
will run only under /workspace/ref_alho_O004 on the shared mscr pod.

## Completed independent checks (2026-11-03 UTC)

Raw public receipts and SHA256 hashes are preserved under
`pod_evidence/public_receipts.json`, `pod_evidence/recheck_receipts.json`,
and `pod_evidence/sources/`. Initial fetch: 15:51:19–20 UTC;
final source/repository recheck: 15:58:18 UTC. Both primary HTML hashes
and all seven result-repository index hashes were unchanged.

1. Primary sources: [2020 paper](https://arxiv.org/abs/1907.09970v2),
   PDF p.28 §6.4, explicitly leaves Signorini existence open. Its authors
   are A. Alho and S. Calogero. [2021 paper](https://arxiv.org/abs/2104.11131v2),
   PDF pp.17–18 §3.4, asks the exact all-above-natural-density question (a)
   and offers numerical support. Its authors are Artur Alho, Simone Calogero,
   Astrid Liljenberg; Alho's Instituto Superior Técnico affiliation matches.
   These are the primary target-specific baseline, not a numerical leaderboard.
   Figure 8 uses delta_c=2, nu=-0.5 and 0.25. No certified numerical radius
   is tabulated. I reproduced those equation/parameter cases independently;
   see ANALYSIS.md on the necessary radius scaling and inferred plot units.

2. [GitHub repository search](https://api.github.com/search/repositories?q=Signorini+elastic+balls&sort=updated&order=desc),
   sorted by recent update, returned 0 repositories. A separate query with
   Signorini, gravitation and 2026 returned 0. [Issue/PR search](https://api.github.com/search/issues?q=%22Signorini%22+%22Alho%22&sort=updated&order=desc)
   returned 0 results. [Code search](https://api.github.com/search/code?q=Signorini+Calogero&sort=indexed&order=desc)
   returned HTTP403, including at recheck; indexed GitHub searches did not
   locate a target implementation or awesome-list. These are incomplete
   searches, not a proof of absence. No login or credentials were used.

3. Fetched and rechecked the public README/CONTENTS indices of
   [BakeLab/Epi-results](https://github.com/BakeLab/Epi-results),
   [DeepMind alphaevolve_results](https://github.com/google-deepmind/alphaevolve_results),
   [DeepMind repository_of_problems](https://github.com/google-deepmind/alphaevolve_repository_of_problems),
   [openai/math](https://github.com/openai/math),
   [EinsteinArena-new-SOTA](https://github.com/togethercomputer/EinsteinArena-new-SOTA),
   [plasma-ai/erdos](https://github.com/plasma-ai/erdos), and
   [kisonecat/openai-math](https://github.com/kisonecat/openai-math).
   All accessible indices had zero Signorini mentions. Coverage is indices,
   not an exhaustive repository-code audit.

4. [Recent-first arXiv query](https://export.arxiv.org/api/query?search_query=all%3ASignorini+AND+%28all%3Agravitat+OR+all%3ACalogero%29&start=0&max_results=50&sortBy=submittedDate&sortOrder=descending)
   yielded the target paper, with no 2025–26 solution. Indexed searches
   specifically including 2024, 2025 and 2026 located no later proof.
   The primary [Beig–Schmidt theorem](https://arxiv.org/abs/gr-qc/0202024v2)
   gives sufficiently small-G/small-body existence near the natural state;
   it does not prescribe every delta_c>1. The primary
   [Calogero–Leonori variational paper](https://arxiv.org/abs/1208.1792v2)
   assumes coercivity/polyconvexity and does not supply this theorem with
   prescribed central density and strong regularity. Its Theorem 2 explicitly
   leaves interior/boundary regularity unresolved for its minimizers.
   [Calogero's polytropic paper](https://arxiv.org/abs/2104.11126) also appeared
   in searches; it discusses a different constitutive family. These papers
   and the 2020 Liljenberg thesis are prior related results, not a finding
   that this proposed theorem is first.

5. [The November 2019 Alho talk announcement](https://physik.univie.ac.at/en/events/events-detail/news/artur-alho-portugal-spherically-symmetric-steady-states-of-newtonian-self-gravitating-elastic-mat/)
   mentions Signorini existence. It was accessible through web search/open,
   but returned HTTP404 to the pod. It supplies no full proof or parameter
   statement. X search redirected to login, Reddit returned HTTP403, and
   indexed community searches found no relevant accessible discussion.
   No target public Discord/Telegram summary or live scoreboard was found.

What changes relative to the papers: a proposed all-parameter analytic
existence argument for question (a), with a parameter-dependent compact
barrier and explicit, loose virial radius bound. The existence behavior
was already numerically conjectured in 2020/2021. Generic small-body
existence was already proved in 2002/2003. Priority and taste are not
adjudicated by this audit; access gaps and the 2019 talk must remain visible.
