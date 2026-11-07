# Prior-art audit — 2026-11-03

This is an independent referee audit, not a search for a new bound. Claimed baseline: arXiv:2107.13871, equation (5.53), 5.67049; claimed replacement 5.45808. These values and their comparability remain unverified.

Primary-source, public-code, recent-paper, public-community and agent-repository checks are pending below. No construction or computation has begun. The paper's own method will be the baseline, independently implemented on the authorized pod. No novelty or priority judgment is intended.

## Primary source and live checks
- https://arxiv.org/abs/2107.13871 and https://arxiv.org/html/2107.13871 (v2, 2022-11-04), inspected 2026-11-03. Printed 5.67049 is the bound on I-tilde_(2,0) at h=5/8, principal gap 8.53, not an empirical score. The exactly specified one-functional baseline is 6.43174. Eight original parameter pairs are not specified in the recovered primary TeX.
- A fresh primary PDF download on the pod matches the supplied public PDF: SHA256 18c00b5be78d4b2e289fafc36f5db6e04fa3e34ee8240946e7071c9a457e04d3.
- The primary author block identifies Matthijs Hogervorst, João Penedones and Kamran Salehi Vaziri, EPFL. SwissMAP's public publication record agrees: https://www.nccr-swissmap.ch/research/publications/towards-non-perturbative-cosmological-bootstrap.
- Web searches for exact 5.67049, 5.45808 and arXiv identifier, GitHub-specific searches, 2025/2026 numerical bootstrap follow-ups, agent-result names and public X/Reddit summaries found no replacement for this exact example. This limited search is not an exhaustive priority audit. A 2026 paper, https://doi.org/10.1007/JHEP06(2026)022, concerns scale-breaking cosmological boundary equations, a different problem.
- Public prior result encountered: Salehi Vaziri thesis https://infoscience.epfl.ch/record/295717/files/EPFL_TH9263.pdf repeats 6.43174 and 5.67049 in equations (5.54)-(5.55). Its appendix E may give more numerical-method detail; inspect before concluding the original eight inputs are unavailable.
- There is no identified official live leaderboard for this toy bound; the primary paper is the comparison source. The claimant's retained wider citation and repository searches are read-only supporting data, not independently exhaustive evidence.

## Baseline status
Independent code written directly from primary gamma/hypergeometric definitions, with no claimant module imports, reproduces 6.431737260572546574... and 2.386377515308742831... . All numerical evaluation runs on mscr. The four-term witness specifies an effective partial-wave weight; reconstructing the original crossing test requires a(z)=1/2 [z(1-z)]^(-1/4)P(z), rather than treating that effective weight as a(z).

## Completed independent recheck, 2026-11-03 20:54 UTC

- GitHub repository searches ordered by latest update returned HTTP 200. Exact `2107.13871` and `Penedones bootstrap 2026` searches returned zero repositories. The broader `cosmological bootstrap` search returned four repositories; the only directly related physics code concerns on-shell Mellin-momentum amplitudes, rather than this nonperturbative partial-wave bound. Exact-identifier open issue/PR search returned zero results. Raw responses and URLs are retained in `public_audit/` and the evidence archive.
- The arXiv last-twelve-month query returned five titles: 2610.42020, 2609.19252, 2607.18369, 2606.06282 and 2605.21581. This was a title/abstract screen, not a full-text exclusion. A final primary arXiv metadata fetch still identifies the same paper.
- Fresh public HEADs and decoded README screens completed for BakeLab/Epi-results, google-deepmind/alphaevolve_results, openai/math, plasma-ai/erdos, kisonecat/openai-math and togethercomputer/EinsteinArena-new-SOTA. No target identifier, exact old/new number, Penedones or cosmology hit occurs in those READMEs. Exact HEAD receipts are in `public_audit/readme_head_summary.json`. The guessed google-deepmind/repository_of_problems URL returned 404. These are HEAD/README screens, not full historical-content searches. The claimant's much broader retained citation/path screens were read but are not represented as my own exhaustive checks.
- Community web searches did not identify a same-problem replacement; this is incomplete coverage. No community absence or worldwide-record claim follows.
- The Salehi Vaziri thesis search excerpt repeats the printed 5.67049. A direct full-thesis download did not succeed, so I did not inspect all its appendices or exclude further data there. The original eight-functional inputs remain unrecovered from the primary paper archive actually inspected.
- Independent referee certificate completed: 61 closed compact-continuum charts, all even n=2,...,38, both tails (23 exact Casimir integrations by parts), and an upward-rounded 34113/6250 bound. This proves the new inequality under the paper's assumptions; it does not reproduce the original eight-functional historical run.
- New relative to the paper: a specific rational degree-7/four-Legendre-term witness and certified numerical bound, within the regularizing-functional linear-programming method already described by the authors. No judgment about novelty, priority or significance is made.

```rh-prior-art
{
 "schema": 1,
 "baseline": "5.67049 (arXiv 2107.13871 eq. 5.53)",
 "sources": {
  "github": {
   "status": "none",
   "query": "conformal bootstrap bounds",
   "searched_at": "2026-11-03T20:56:59+00:00",
   "hits": [],
   "note": "GitHub repository search, top 0 by best match."
  },
  "x": {
   "status": "none",
   "query": "conformal bootstrap bounds",
   "searched_at": "2026-11-03T14:42:26+00:00",
   "hits": [],
   "note": "Captured X search (browser, 2026-11-03T14:42:26+00:00) for the friend topic; 0 posts. Friend-level capture, not a per-target X search.",
   "capture_path": "friends_queue/x_capture/frozen/penedones_0786126ddc59.jsonl",
   "capture_sha256": "0786126ddc59861bc02b99bc19bdf0488f4d68953db3840566a4311d07ab5da6"
  },
  "papers": {
   "status": "hits",
   "query": "de Sitter bootstrap Hogervorst Penedones Salehi Vaziri functionals",
   "searched_at": "2026-11-03T20:56:59+00:00",
   "hits": [
    "https://doi.org/10.1007/jhep02(2023)162",
    "https://doi.org/10.1007/jhep02(2026)220",
    "https://doi.org/10.1007/jhep07(2026)208",
    "https://doi.org/10.1007/jhep08(2021)063",
    "https://doi.org/10.1007/jhep12(2023)159",
    "https://doi.org/10.1103/physrevd.111.045001"
   ],
   "note": "Crossref (OpenAlex daily quota exhausted) relevance search, top 6; the worker reads them before modelling."
  },
  "leaderboards": {
   "status": "none",
   "query": "conformal bootstrap bounds",
   "searched_at": "2026-11-03T20:56:59+00:00",
   "hits": [],
   "note": "Hugging Face spaces/datasets search and GitHub \"<q> benchmark\" repos."
  }
 }
}
```
