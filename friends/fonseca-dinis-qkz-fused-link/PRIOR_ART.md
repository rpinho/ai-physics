# Independent referee prior-art record

Started 2026-11-03, before any referee code.

Primary baseline: Fonseca and Zinn-Justin, arXiv:1212.4672v2,
https://arxiv.org/html/1212.4672 . The claim identifies Appendix C.2's
triangular injectivity argument as the best public baseline; no numerical
leaderboard is identified. I have independently opened the primary paper
and its arXiv metadata (authors T. Fonseca and P. Zinn-Justin).
The claimed 34 is a generic multiplicity/image dimension, not a printed
special-root numerical score. This distinction will be audited before computation.

Relevant existing mathematics, independently opened:
https://arxiv.org/abs/2008.06038 (Flores–Peltola, higher-spin Schur–Weyl duality),
https://arxiv.org/abs/1910.12427 (Blanchet–De Renzi–Murakami, small quantum sl2).
The ordinary/divided-power distinction is prior art, not an innovation assumed here.

The submitter's PRIOR_ART.md was read as a lead, not accepted as evidence.
It reports no dedicated leaderboard/code, unsuccessful updated GitHub API
retrieval, and indexed audits of BakeLab/Epi-results, DeepMind's two AlphaEvolve
repositories, openai/math, EinsteinArena, plasma-ai/erdos, kisonecat/openai-math,
recent arXiv, and public community sources. Independent targeted checks follow.
This referee is testing correctness and interpretation; it does not claim novelty.

Baseline reproduction planned: reconstruct local matrices from (2.1), tensor
coproduct and fused singlets from Appendix C; compare generic q=2 with the root
and then impose regular divided powers as the sceptical control.

## Completed independent checks

Primary C.2 explicitly proves injectivity where the local projectors exist,
proves generic surjectivity, and states the special-root isomorphism conjecture.
Section 2.1 describes U1 using E1,F1,K1. The ordinary-generator interpretation
is therefore a defensible literal reading, but does not determine what integral
form or limiting invariant space the authors intended at the root.
Baseline q=2 and the projected-image dimension both independently reproduce 34.

Read 1910.12427v3, introduction and Sections 4–5:
https://arxiv.org/html/1910.12427v3 . It distinguishes the small quantum group
from the divided-power quantum group; the TL functor is not generally full
for the former and is extended by additional morphisms. This is directly relevant
prior mathematics. Read 2008.06038, pp.3–5, especially its discussion of extending
the algebra by divided powers in the nonsemisimple regime:
https://arxiv.org/pdf/2008.06038 . No priority/novelty inference is made.

Public code check: direct unauthenticated GitHub repository API query
`q="1212.4672"&sort=updated&per_page=5` succeeded and returned total_count=0;
raw response saved as github_updated_search.json. Web-tool retrieval of the same
API failed before the direct curl succeeded. Repository search does not search
all code. Indexed exact-id GitHub, valenced/TL awesome-list and 2025/2026 queries
found no relevant implementation or competing finite table. Lab-repository
queries covered BakeLab/Epi-results, google-deepmind/alphaevolve_results,
google-deepmind/alphaevolve_repository_of_problems, openai/math, EinsteinArena,
plasma-ai/erdos and kisonecat/openai-math. Unrelated hits were excluded. This
is indexed coverage, not a recursive audit of every repository or open issue.
Community queries covered the source id with X, Reddit, blog, Discord and
Telegram terms; no relevant result was located. No accounts or contacts used.
Final source/id/correction and repository checks did not identify a changed
baseline. There is still no identified dedicated leaderboard or relevant code
repository whose open PRs/issues could be inspected.

Identity check: source title-page author/CRM-to-LAPTh affiliation and Zinn-Justin
match the companion primary paper https://arxiv.org/html/1210.4527, whose author
contact explicitly contains the full Dinis da Fonseca name. This matches the
local identity audit; unrelated Tiago Fonseca publications were not used.
