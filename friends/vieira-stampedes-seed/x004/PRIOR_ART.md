# Independent referee prior-art record — 2026-11-03

Written before referee code. Scope is correctness of the submitted formal light-cone seed, not novelty or priority.

Primary source: Olivucci and Pedro Vieira, Stampedes I, arXiv:2111.12131v2, JHEP07(2022)017. Authorship confirmed on the primary arXiv HTML. Its appendix E asks for resummation of the displayed seed. There is no identified official numerical leaderboard for this symbolic question.

Best public general baseline: Kostov–Petkova–Serban, The Octagon as a Determinant, https://arxiv.org/abs/1905.11467, all-loop arbitrary-bridge ladder determinant. Belitsky–Korchemsky https://arxiv.org/abs/2006.01831 gives the Bessel Fredholm determinant; https://arxiv.org/abs/2003.01121 gives the exact resolvent equations. These cover the octagon more generally than a finite coefficient table. Independent reproduction planned on mscr from source definitions.

Initial public searches: `"octagon" "single" "light-cone" "Kummer"`, `"Stampedes" "Toda" resummation`, `github octagon Toda Vieira 2026`, `"Stampedes I" Vieira Olivucci`. Located https://arxiv.org/abs/2205.04476 (Stampedes II, higher polygons and Toda equations). No seed competitor identified from this initial search; this is not an absence or novelty claim.

Public code, recently updated repository searches, lab-result repositories, last-year papers, and community sweep will be recorded below. The claimant's prior-art notes are read-only leads, not independent evidence. No contact or account creation.

## Completed independent sweep

All public responses and SHA256 receipts are archived under `evidence/sources/prior_sweep/`. Requests ran on mscr without credentials. GitHub repository API searches were sorted by updated descending: `octagon integrability`, `2111.12131`, `octagon Toda 2026`, `octagon awesome`. The first returned five unrelated MMA/API/watch repositories; the others returned zero. An issue/PR search for the paper ID returned no open matches. The unauthenticated code-search page was fetched, but no exhaustive code-search coverage is inferred.

Read public READMEs of BakeLab/Epi-results, google-deepmind/alphaevolve_results, openai/math, plasma-ai/erdos and kisonecat/openai-math. No relevant seed result was identified there. BakeLab's octagon hit concerns circle packing. The alphaevolve_results public tree had no path matching octagon, Toda, stampede or repository_of_problems. Guessed standalone google-deepmind/repository_of_problems and EinsteinArena/EinsteinArena README URLs returned 404; EinsteinArena's public website was fetched separately. These limitations remain explicit.

The arXiv API query for octagon AND (Toda OR light-cone), submitted 2025-11-03 through 2026-11-03, returned no entries. Additional public indexed searches for octagon/Kummer, octagon/confluent hypergeometric, Stampedes/Toda resummation, and 2025/2026 light-cone octagons identified no competing expression. Searches for Stampedes I on Reddit and Vieira/stampedes on X produced no relevant primary result; this is limited search visibility, not evidence of absence.

An additional primary paper encountered was Loebbert–Stawinski, https://arxiv.org/abs/2408.15331 (JHEP11(2024)092), on conformal integrals and Toda equations. Its octagon discussion recalls the previously known one-dimensional Bessel determinant and the two-dimensional single-scaling Toda observation, citing Stampedes I; it does not supply the submitted Kummer expression in that discussion. Stampedes II (2205.04476) concerns higher polygons.

The baseline reproduction succeeded: all 30 displayed coefficients, including 1 and 18/5 for c_(2,4) at bridges 1 and 0, from an independently transcribed public KPS formula. A different public Bessel determinant representation then independently confirmed the submitted seed through L^32 at four fresh parameter points. See `REPORT.md` and `DERIVATION.md`.

Final source/repository pass completed 2026-11-03 around 22:51 UTC. The factual addition relative to Stampedes I is a closed Kummer expression for its formal inverse-log seed. Arbitrary-bridge all-loop determinants, the null Gaussian, exact resolvent equations, and the stated Toda determinant were already public. No judgment of novelty, priority, or author interest is made.
