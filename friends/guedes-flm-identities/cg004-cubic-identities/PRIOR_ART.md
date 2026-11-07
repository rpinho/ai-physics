# Prior-source check (2026-11-05)

This is an independent check of a proposed erratum, not a record search.
There is no applicable leaderboard or best numerical score.

- Primary source: https://arxiv.org/abs/1301.7750 lists Carlos Guedes,
  Daniele Oriti and Matti Raasakka; v1 2013-01-31, v2 2013-09-27.
  Fresh v2 PDF downloaded from https://arxiv.org/pdf/1301.7750v2.
- Journal DOI: https://doi.org/10.1063/1.4818638 (publisher access blocked).
  Fresh journal PDF downloaded from the institutional repository:
  https://pure.mpg.de/rest/items/item_1671208/component/file_1859595/content.
- Public code: web searches for exact arXiv ID on GitHub, and Guedes/Duflo
  in BakeLab, DeepMind, OpenAI, kisonecat, plasma-ai and EinsteinArena
  returned no relevant correction or implementation. This is an indexed
  search, not an exhaustive GitHub code audit or authenticated recent-sort.
- Papers/corrections: exact-title and ID searches for erratum/corrigendum,
  plus Guedes/Oriti/Raasakka/083508, found no correction. Latest arXiv
  version shown is v2. Related later work encountered: Kupriyanov and
  Vitale, JHEP 08 (2015) 024, and JHEP 05 (2016) 146 on closed star
  products. These have not yet been checked for the specific cubic issue.
- Community: indexed ID searches including Reddit and X yielded no
  relevant correction. No accounts used and nobody contacted.

Baseline: reproduce the paper's definitions using PBW symmetrization,
the Duflo differential factor, and the FLM plane wave, with exact arithmetic.
Only CLAIM.md has been read from the proposing job so far; no proposer
search/verifier code is used. No claim of novelty will be made.

## Completion check

- Latest arXiv landing page still lists only v1/v2. Fresh v1 has the same
  two defective cubic lists; v2 did not fix them.
- Crossref DOI metadata, its title search with "Erratum", INSPIRE's
  arXiv-ID record, and additional exact-title/ID searches for correction,
  erratum, corrigendum, typo and incorrect found no specific correction.
  Raw Crossref/INSPIRE responses are retained locally. This does not prove
  that no correction/discussion exists. Direct publisher PDF returned 403;
  the journal evidence is its version of record in the MPG archive.
- Read the relevant passages of Kupriyanov--Vitale,
  https://arxiv.org/abs/1502.06544 (JHEP 08 (2015) 024), especially
  Eqs. (6.13)--(6.26). Their gauge factor is
  2*sinh(theta*sqrt(Delta)/2)/(theta*sqrt(Delta)), giving 1+Delta/6
  with theta=2 here. They cite the 2013 paper's plane-wave product;
  no explicit erratum or corrected triple-word list was located there.
- Prior reference encountered in both papers: Freidel--Majid,
  Class. Quant. Grav. 25 (2008) 045006, arXiv:hep-th/0601004.
  Its full text was not audited; do not infer priority from this report.
- No new bound, model or construction was produced. Relative to the
  printed paper the deliverable is correction of two example identities.
  After both independent implementations passed, the proposing job's
  REPRODUCTION_FINDING.md was read as data and agreed with our results.
  No proposing-job Python source was read or imported.
