![AI for Physics: certified bounds, exact seeds and bug reports on published physics software](assets/banner.png)

# ai-physics: the record

**AI for Physics.**

Physics results I've run with AI agents, in one place. Every item names the published paper it starts from, what was asked, what we found, how an independent referee checked it, and where it is still a candidate. All of it has been sent to the author it concerns.

What was easy, what was hard, and what is still open: [RETRO.md](RETRO.md).

Sister hubs: [AI for biology](https://github.com/rpinho/ai-biology) · [math](https://github.com/rpinho/math-certificates) · [astronomy](https://github.com/rpinho/planet-hunt)

## What this is, and what it isn't

A physicist I studied with put the objection plainly: a number alone isn't worth much without new physics or new intuition behind it. I think he's right, and most of what is below is a tightening, a closed form or a software defect rather than new physics. It is labelled that way.

Brian Armstrong's November 7 [post](https://x.com/brian_armstrong/status/2119150702446420027) is the format argument: every experiment as a repo, data and code versioned, replication rewarded.

**Referee verdicts** are the separate agent's words: HOLDS, HOLDS WITH CAVEATS, CONFIRMED, CONFIRMED-MINOR. Nothing here has been refereed by a journal, and no priority is claimed.

This file puts the record of every result in one place, for readers and reviewers who want it in a single document. Each section below is copied word for word from the result's own folder in this repository: the claim, the derivation or analysis, the independent referee's verdict, and the prior-art check. Some referenced evidence isn't included in this repository.

---

# João Penedones — de Sitter bootstrap bound

Folder: [friends/penedones-de-sitter-bootstrap](friends/penedones-de-sitter-bootstrap)

## Claim

_Source: [friends/penedones-de-sitter-bootstrap/CLAIM.md](friends/penedones-de-sitter-bootstrap/CLAIM.md)_

## penedones_NB01: board result to referee (11-03)

UNVERIFIED. This number came from the scoreboard job, not a target worker: de Sitter bootstrap bound (arXiv 2107.13871 eq. 5.53), 5.67049 to 5.45808, said to be certified by a separate interval verifier.

Evidence (read-only, in a private working copy, not in this repository): REPORT.md, FRIEND_NOTE.md, CHOICE.md, PROOF.md if present, and every verifier/search script and result file those reports name in that folder; pod copies on a rented compute pod.

Referee the exact claimed number: rebuild it from the primary paper with your own code, check the paper's printed number, its definition and normalization, run the trivial control, and check the verifier is independent of the search. End HOLDS, HOLDS WITH CAVEATS or FAILS.

## Derivation

_Source: [friends/penedones-de-sitter-bootstrap/DERIVATION.md](friends/penedones-de-sitter-bootstrap/DERIVATION.md)_

## Independent derivation and certification

Primary source: Hogervorst, Penedones and Salehi Vaziri, arXiv:2107.13871v2, sections 5.1, 5.3 and 5.4, especially equations (5.43)–(5.53). The journal/TeX numbering is used here; the arXiv HTML renumbers the equations consecutively. The PDF downloaded independently on the pod matches the claimant's public source byte for byte. No claimant Python module is imported by any referee evaluator.

### Quantity and functional

Set h=5/8 and nu*=853/100. Let P be the rational combination of shifted Legendre polynomials with coefficients 30113/125000, -188947/250000, 1, -2967/12500 at degrees 1,3,5,7. Its coefficients are reconstructed from the factorial formula, rather than taken from the witness's expanded arrays. Since P(1-z)=-P(z), applying the paper's crossing equation with the original test

    a(z) = (1/2) [z(1-z)]^(-1/4) P(z)

gives the effective partial-wave weight

    w(z) = (1-z)^(5/4)[a(z)-a(1-z)] = z^(-1/4)(1-z)P(z).

The witness's basis string describes w, not a. Treating w as the original crossing test changes the problem. Our first diagnostic did that, gave 5.53530, and was discarded before certification. This does not contradict the claimant's derivation, which correctly distinguishes them. The final defining-3F2 implementation expands a into (gamma,sigma)=(j-1/4,-1/4) with half the polynomial coefficients. Both endpoint exponents exceed -1, satisfying the paper's convergence criterion.

The identity contribution is D=integral(w)=-1058384983/16298734375. The spectral actions are F(nu)=integral(w Psi_(1/2+i nu,0)) and F_n=integral(w Psi_(n,0)). The exact reconstructed functional, paper normalization and prescribed gap are unchanged. Positivity of all these actions gives I-tilde_(2,0) <= -D/F_2. The fresh interval objective is 5.4580734714720031025256703361474007847041448079903959..., strictly below 34113/6250.

### Two independently implemented evaluation routes

1. `independent_check.py` evaluates the paper's gamma and 3F2 expressions in mpmath, at 45 decimal digits. It reproduces the fully specified baseline 6.431737260572546574... at h=5/8, and 2.386377515308742831... at h=3/8. It also reproduces the accepted objective and individual principal/discrete actions. These are diagnostics, not certificates.

2. `series_referee.py` uses python-flint Arb/Acb at 640 bits. It integrates two convergent endpoint series term by term, including rounding and explicit truncation bounds. It uses no quadrature rule, optimizer, stored spectral arrays, or claimant verifier code. Split z at 1/2 and write d=1/2+i nu. For the lower half, expand G_d=z^d sum_k (d)_k^2 z^k/[(2d)_k k!], with coefficient K_(1-d)=B(d,d)(1+sec(pi d)); add the shadow. The remaining tail after N=1024 terms is geometric because, for k>=N,

    |c_(k+1)/c_k|/2 <= (1+|d|/N)^2/2 < 1.

The z powers and (1-z) polynomial are integrated exactly with complex ball arithmetic. Absolute monomial coefficients bound the uncomputed remainder.

For the upper half put t=1-z and v(t)=(1-t)^b Psi(1-t), b=-1/4. The Casimir equation becomes

    t(1-t)^2 v'' + [1+(2b-2)t+(1-2b)t^2]v' + [b-lambda+b^2 t]v = 0.

Write v=sum_k (a_k log(t)+b_k)t^k. Its starting values are a_0=-2 and

    b_0=4 psi(1)-2 psi(d)-2 psi(1-d)+2 pi/sin(pi d).

For even discrete n, use d=n, lambda=n(n-1), b_0=-4 H_(n-1), and the single normalized block K_(1-n)=2 B(n,n). Substitution into the displayed differential equation gives the three-term recurrences in the source. All t powers and log(t) powers are integrated exactly against t P(1-t).

The analytic log and regular factors are bounded on |t|=3/4 using the zero-balanced hypergeometric expansion. For integer M>=|d|,|(1-d)|, the absolute hypergeometric coefficients are bounded by binom(k+M-1,M-1)^2, whose generating function at u is at most 4^(M-1)(1-u)^(1-2M). The regular factor's digamma terms grow at most linearly in k. A second radius 7/8 bounds the extra k factor. Explicit deliberately loose Cauchy bounds MA,MB appear in the code. Their tail integral is bounded by

    PA*(r/R)^N*r^2/[(N+2)(1-r/R)] * [MB+MA*(-log(r)+1/(N+2))],

where r=1/2, R=3/4, PA=sum_j |P_j|. This includes both omitted endpoint-series tails. At nu=39 the retained bound on this error is about 5.37e-41, well below the positive action 2.342e-7. The two evaluation routes agree.

### Compact continuum, exact tails and discrete modes

`certify_referee.py` uses 61 closed intervals covering [8.53,39]. On each, it evaluates 96 equally spaced circle points of radius 3/10 (49 computations suffice by conjugation symmetry), using only the new endpoint-series evaluator. The discrete Fourier transform encloses Taylor coefficients through degree 94. The outer analytic disk radius is 12/25. An Euler integral bounds the function there by

    M*=4 B(delta,delta) PA B(3/4+delta,1+delta), delta=1/100.

The two normalized block factors are bounded by 2 each because Re(nu)>1; both real parts of d and 1-d stay above delta. The integrated bound follows from |w|<=PA z^(-1/4)(1-z). Cauchy's estimate gives explicit Fourier alias and omitted Taylor errors. Interval Horner evaluation, subdividing real intervals if needed, proves positivity throughout every interval; the final code independently checks that the accepted leaves and charts form complete partitions. This is not a finite-grid inference.

For both infinite tails, set u=z^(7/4)(1-z)P. With C=z^2(1-z)d_z^2-z^2 d_z, integration by parts gives

    lambda F = 2u(1) + integral((C u) Psi dz/z^2).

All lower-end boundary terms vanish. The upper-end term uses Psi=-2 log(1-z)+O(1). Apply C z^s=s(s-1)z^s-s^2 z^(s+1) in exact Fraction arithmetic. The common bound |Psi|<=3 pi sqrt(z/(1-z)) holds for principal nu>=1 and every even discrete n>=2, using the paper's Euler block integral. Thus the remaining norm is bounded by 3 pi sum_j |c_j| B(s_j-1/2,1/2). Arb encloses the beta values and verifies an upward integer norm bound. At 23 integrations by parts, exact rational arithmetic proves the leading positive term dominates every correction for |lambda|>=6085/4. This covers principal nu>=39 and even n>=40. All remaining even n=2,4,...,38 pass the separate endpoint-series enclosure. The target n=2 also supplies the objective inequality.

No new physical assumptions are introduced beyond the paper's positivity, spectral gap and regularized crossing/growth framework. There is no statistical dataset or hold-out: the rational witness was frozen and then checked on the full continuous/discrete spectrum by independent code.

### Controls and limitations

The single degree-1 effective weight yields objective 10.8757188312, and the other three single terms fail positivity after normalizing the target positively. Dropping degree 5 gives the tempting objective 2.78965859952 but a strictly negative n=6 action. Dropping degree 7 also fails at n=6. Dropping degree 3 worsens the diagnostic objective to 17.63037. All controls are recorded as diagnostics, not alternate certified bounds. Removing the principal gap exposes negative action at nu=2.21 (about -0.28014747), so the witness must not be used as a bound without that assumption.

The exact eight pairs and coefficients underlying the printed 5.67049 are unavailable in the recovered primary archive. We reproduce the specified single-functional baseline and prove the new bound, but do not reproduce that historical eight-functional optimization. The paper already proposes linear programming over regularizing functionals; the addition here is a concrete rational witness, lower number and all-spectrum certification within that method. No optimality, novelty or priority judgment is made.

## Verdict

_Source: [friends/penedones-de-sitter-bootstrap/VERDICT.md](friends/penedones-de-sitter-bootstrap/VERDICT.md)_

HOLDS WITH CAVEATS
Referee: gpt-6.1-sol

The new bound survives: I-tilde_(2,0) <= 34113/6250 = 5.45808, with the paper's same normalization, external dimension 5/8 and principal-series gap 8.53.
[The primary paper](https://arxiv.org/abs/2107.13871), equation (5.53), really prints 5.67049. Its authors include João Penedones, EPFL, alongside Hogervorst and Salehi Vaziri.

I wrote two evaluators from the paper's definitions, importing neither claimant search nor verifier code. Direct gamma/3F2 evaluation reproduces the specified baseline 6.43173726057 and the new objective 5.4580734714720031025.
My separate Arb endpoint-series certificate proves positivity on all 61 closed intervals covering nu=8.53 through 39, every remaining even discrete mode, and both infinite tails. It also proves the upward rounding to 5.45808. See referee_certificate/VERIFIED.json, DERIVATION.md and REFEREE_EVIDENCE.tar.gz.

The trivial controls do not explain away the gain: the single linear term gives 10.87572; deleting degree 5 gives an apparent 2.78966 but fails positivity at n=6. Deleting degree 7 also fails there.
Removing the assumed gap exposes negative action near nu=2.21. This remains a bound conditional on that gap and the paper's regularized-crossing framework.
There is no statistical hold-out. The frozen rational witness was checked against the entire allowed spectrum, including modes beyond the search range.
The claimant verifier imports no search module; my certificate uses a different integration method and no claimant modules.

Relative to the paper, the addition is a concrete four-term rational functional, its smaller numerical bound and a complete spectrum certificate within the authors' existing linear-programming approach.
Prior result encountered: Salehi Vaziri's thesis also prints 5.67049. Literature coverage and access limits are recorded in PRIOR_ART.md; no worldwide-record conclusion is asserted.

Caveat / strongest author objection: I reproduced the fully specified one-functional baseline, but the eight pairs and coefficients behind the printed 5.67049 were unavailable in the recovered primary archive. The historical eight-functional calculation itself was not reproduced.

NEXT BAR: recover those eight pairs and coefficients and reproduce 5.67049 with the independent evaluator used here.

## Prior Art

_Source: [friends/penedones-de-sitter-bootstrap/PRIOR_ART.md](friends/penedones-de-sitter-bootstrap/PRIOR_ART.md)_

## Prior-art audit — 2026-11-03

This is an independent referee audit, not a search for a new bound. Claimed baseline: arXiv:2107.13871, equation (5.53), 5.67049; claimed replacement 5.45808. These values and their comparability remain unverified.

Primary-source, public-code, recent-paper, public-community and agent-repository checks are pending below. No construction or computation has begun. The paper's own method will be the baseline, independently implemented on the authorized pod. No novelty or priority judgment is intended.

### Primary source and live checks
- https://arxiv.org/abs/2107.13871 and https://arxiv.org/html/2107.13871 (v2, 2022-11-04), inspected 2026-11-03. Printed 5.67049 is the bound on I-tilde_(2,0) at h=5/8, principal gap 8.53, not an empirical score. The exactly specified one-functional baseline is 6.43174. Eight original parameter pairs are not specified in the recovered primary TeX.
- A fresh primary PDF download on the pod matches the supplied public PDF: SHA256 18c00b5be78d4b2e289fafc36f5db6e04fa3e34ee8240946e7071c9a457e04d3.
- The primary author block identifies Matthijs Hogervorst, João Penedones and Kamran Salehi Vaziri, EPFL. SwissMAP's public publication record agrees: https://www.nccr-swissmap.ch/research/publications/towards-non-perturbative-cosmological-bootstrap.
- Web searches for exact 5.67049, 5.45808 and arXiv identifier, GitHub-specific searches, 2025/2026 numerical bootstrap follow-ups, agent-result names and public X/Reddit summaries found no replacement for this exact example. This limited search is not an exhaustive priority audit. A 2026 paper, https://doi.org/10.1007/JHEP06(2026)022, concerns scale-breaking cosmological boundary equations, a different problem.
- Public prior result encountered: Salehi Vaziri thesis https://infoscience.epfl.ch/record/295717/files/EPFL_TH9263.pdf repeats 6.43174 and 5.67049 in equations (5.54)-(5.55). Its appendix E may give more numerical-method detail; inspect before concluding the original eight inputs are unavailable.
- There is no identified official live leaderboard for this toy bound; the primary paper is the comparison source. The claimant's retained wider citation and repository searches are read-only supporting data, not independently exhaustive evidence.

### Baseline status
Independent code written directly from primary gamma/hypergeometric definitions, with no claimant module imports, reproduces 6.431737260572546574... and 2.386377515308742831... . All numerical evaluation runs on a rented compute pod. The four-term witness specifies an effective partial-wave weight; reconstructing the original crossing test requires a(z)=1/2 [z(1-z)]^(-1/4)P(z), rather than treating that effective weight as a(z).

### Completed independent recheck, 2026-11-03 20:54 UTC

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
   "capture_path": "private capture, not in this repository",
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

---

# Pedro Vieira — a closed single-light-cone seed

Folder: [friends/vieira-stampedes-seed/x004](friends/vieira-stampedes-seed/x004)

## Claim

_Source: [friends/vieira-stampedes-seed/x004/CLAIM.md](friends/vieira-stampedes-seed/x004/CLAIM.md)_

## vieira_X004 — proposed closed single-light-cone Toda seed

Submitted 2026-11-03 for independent mechanical referee and separate taste review. Neither review has been performed by this worker. Only queue row X004 is owned by this worker.

### Published baseline and open item

Olivucci–Vieira, [Stampedes I,2111.12131v2](https://arxiv.org/abs/2111.12131v2), JHEP07(2022)017. The unnumbered table on printed page 13 in section4 gives30 entries for bridges 0,1,2 through six loops, including c^(1)_(2,4)=1 and c^(0)_(2,4)=18/5. All30 were reproduced first.

The best public general method is the exact all-loop arbitrary-bridge determinant of Kostov–Petkova–Serban,[1905.11467](https://arxiv.org/abs/1905.11467), equations1.38–1.40; its coverage already includes larger bridge rows. A1 independently confirmed those rows with the sl(2) Hamiltonian but did not improve that coverage. Immutable ATTEMPT1.md records the failure and SWEEP.md precedes A2.

A2 changes formulation to a stated open item in the same paper: section4 equation 4.10/page 14 reports an unresummed single-LCDS seed series through (L/B)^6; appendixE equation E.7/page 28 displays its corrections, and the paragraph after E.10/page 29 requests a closed resummation. The [published PDF](https://inspirehep.net/files/a85c2fd13096f2cdc4ad8195d2604431) was checked. In arXiv HTML these are equations93 and96. This claim replaces that unresummed seed, rather than asserting better numerical accuracy than an exact determinant.

### Proposed result

In the leading-power double-light-cone sector of appendixE, retaining all inverse-log corrections, write L=g^2*log(z), B=log(1/bar(z)) and g^2=-lambda as there. Then

    tau(L,B)=O1/O0
            =exp(i*pi*L)*1F1(1/2+i*B/(2*pi);1;-2*i*pi*L).

Equivalently,

    L*tau_LL+tau_L+(pi^2*L-B)*tau=0, tau(0,B)=1,
    a_0=1, a_-1=0, (n+1)^2*a_(n+1)=B*a_n-pi^2*a_(n-1).

This is an all-order formal identity, not a general-cross-ratio octagon formula. The source's equation E.8/94 then expresses every bridge ratio as its mixed-derivative determinant. No new all-order proof of that already stated Toda hierarchy is claimed.

PROOF.md supplies an all-order argument independent of coefficient fitting: the Bessel recurrence gives a rank-one relation between kernels K0 and K1. The determinant lemma identifiesD1/D0 with Q(0), where Q=(1-K0*chi)^(-1)J0(sqrt(x)). The exact published resolvent ODE ([Belitsky–Korchemsky,2003.01121](https://arxiv.org/abs/2003.01121), equations27,29,30) at x=0, with the known zero-bridge Gaussian, reduces to the displayed ODE. Kummer's equation gives the unique regular solution. The kernel definition for arbitrary bridge is [2006.01831](https://arxiv.org/abs/2006.01831), equations23–25.

### Verification and controls

All computation ran on a rented compute pod, nice 10, at most 8 cores, thread counts 1. The local machine performed editing and transport only.

- Baseline: 30/30 published coefficient entries; 108 baseline and 156 extension Hamiltonian matrix elements agree exactly with independently coded determinant coefficients. Extensions cover bridge 3 through loop 12 and bridge 4 through loop 14, with J=1..6. These finite J checks are not an all-spin theorem.
- A2: 650/650 independent exact rational seed coefficient checks through L^24 at B=0,...,25,pi^2=1. The public full determinant includes all contributing particle sectors and does not import the proposed ODE. The separate verifier uses only the frozen recurrence. Degree bounds and weighted homogeneity turn these evaluations into polynomial identities, not statistical validation.
- Supplemental: 3250/3250 higher-bridge comparisons for bridges 2..6 through L^24 at the same 26 B values. Seed mixed derivatives use a signed-subset determinant algorithm, separate from KPS Gaussian elimination. Five symbolic checks audit the kernel relation, boundary value, potential, Kummer substitution and cusp expansion. Zero failures throughout.
- Trivial controls: I0(2*sqrt(L*B)) differs in 587 seed coefficient entries. A1's single-ladder/binomial control misses 30 nontrivial multi-ladder extension cases.

Concrete multi-ladder certificate: bridge 3,J=2,loop 10 has full 15393/256 versus single-ladder 4641/256. The two-ladder bridge coefficients include c^(3)_(4,6)=1 and c^(4)_(5,7)=1, with higher terms in ATTEMPT1.md. These are supporting verified data, not the claimed frontier.

The first three displayed source corrections informed A2 and are explicitly fitting evidence. config_A2.json and the later supplemental scope were frozen before their respective computations. No statistical or sealed hold-out was used or opened. Finite checks alone are not offered as the all-order proof.

### Files and exact reproduction

Root: a private working copy; only some of these files are in this repository.

- `PROOF.md`, `REPORT.md`, `PLAN.md`, immutable `ATTEMPT1.md`, `ATTEMPT2.md`, `config_A1.json`, `config_A2.json`.
- A1 code: `determinant.py`, `hamiltonian.py`, `compare.py`.
- A2 code: `toda_determinant.py`, `toda_verify.py`, `proof_verify.py`, `bridge_verify.py`.
- Exact data: `pod_results/baseline_determinant.json`, `comparison_baseline.json`, `comparison_extension.json`, `toda_det_B*.json`, `toda_verification.json`, `bridge_B*.json`, `bridge_verification.json`, `proof_verification.json`, logs and source receipts.
- Prior art: `PRIOR_ART.md`, `SWEEP.md`, `FINAL_RECHECK.md`, `PDF_AUDIT.md`, and timestamped public-source receipts in `pod_results/`. `backup_manifest.json` records transported-file hashes.

Reproduction steps, run on the pod through the pod helper script: `pod_reproduce.sh`, then `pod_poll_reproduce.sh`. The pod scripts aren't bundled in this repository.

The payload starts a tracked nohup job on the pod, which also keeps the outputs and logs. Python dependencies: python-flint and SymPy. Do not run research computation on the local machine. The full command sequence is `reproduce_commands.sh`. Existing runs are complete; the reproduction payload is supplied for the separate referee.

### Worries and limits for the referee

1. Check the all-order source applicability and coefficientwise limit carefully. The claim projects out cross-ratio power corrections before specializing polynomial logarithms. B=0,...,25 are evaluation points of those formal coefficient polynomials, not actual finite-cross-ratio observations. No uniform finite-coupling remainder estimate is claimed.
2. Sign convention: sourceE.1–E.2/87 imply exp(-LB+pi^2*L^2/6), matching the full determinant in all 650 zero-bridge coefficient checks and the printed seed. The isolated single-LCDS Gaussian line prints a minus sign in both HTML and PDF. Our comparisons use the former convention; inspect PDF_AUDIT.md. No broader assertion about a physical-observable error is made.
3. Source 2003.01121 treats the simplest octagon; the asymptotic-octagon symbol differs by cross-ratio power corrections in this projected sector. Audit that projection and the exact rank-one identification, rather than relying on the finite match alone.
4. Prior-art coverage is limited by 403 GitHub code/tree responses and unreadable public X results. Current papers, source text, repository searches and AI-lab READMEs were rechecked 2026-11-03; no competing seed expression was identified. This does not establish novelty. Taste and author interest are for their designated review.
5. No claim of a new numerical record, full all-loop bootstrap, improved determinant accuracy, or additional biology result. No contact, post, email, PR or publication was made; no friend note was written.

## Derivation

_Source: [friends/vieira-stampedes-seed/x004/DERIVATION.md](friends/vieira-stampedes-seed/x004/DERIVATION.md)_

## Referee's source-based derivation and scope audit

The submitted identity survives as a formal identity of the leading-power double-light-cone coefficients. This statement does not identify that formal object with an exact finite-cross-ratio observable.

### Independent determinant construction

Use Belitsky–Korchemsky [2006.01831](https://arxiv.org/html/2006.01831v2), equations (29), (30), (35), (36), and (39). Expanding the two Bessel functions in the kernel on [0,1] gives a coefficient matrix C in the basis t^(ell/2+a). For k=ell+a+b+1,

    C_ab = (-1)^(a+b) g^(2k) q_k /
           [k a! b! (ell+a)! (ell+b)!],
    H_ab = integral_0^1 t^(ell+a+b) dt = 1/(ell+a+b+1),
    O_ell = det(1-C H).

The leading A^k coefficient of q_k, with A=log(z) on the source's null-log sheet, follows from the polylog formula (39) and the inversion polynomial in Stampedes I E.11. The code first evaluates the unsimplified finite sum from (39), then checks its simplification:

    [A^k] q_k = k! sum_{j=0}^{floor(k/2)} c_j B^(k-2j)/(k-2j)!,
    c_j = (2-2^(2-2j))*zeta(2j),  c_0=1.

Even zeta values are evaluated rationally with Bernoulli numbers; pi^2 is a formal rational parameter. This step uses no seed recurrence. The coupling scaling replaces g^(2k) A^k by L^k.

Cauchy–Binet expresses the r-particle sector as a sum over two increasing r-subsets a,b. Its L degree is r(ell+1)+sum(a)+sum(b). Thus r(r+ell)>N excludes an entire sector through degree N, and a bounded enumeration exhausts every term. The Gram minor has the exact Cauchy determinant

    det(H_b,a) = Vandermonde(a)*Vandermonde(b) /
                 product_{i,j}(ell+a_i+b_j+1).

The remaining small Hankel determinant has entries q_k/k. `ref_bessel.py` uses exact FLINT rational determinants of those minors, rather than the claimant's KPS matrix and power-series Gaussian elimination. Symmetry permits summing unordered subset pairs and doubling unequal pairs.

Fresh tests: N=32, ell=0,1,2,3, B=-3/2, 2/7, 31, 0, pi^2=7/3. Every one of the 528 coefficients agrees. These include five-particle contributions for ell=0 and ell=1. At each point, direct expansion of the proposed confluent hypergeometric function also agrees with its recurrence, including cancellation of all imaginary coefficients. The mixed derivative determinant is evaluated by permutations and exact series convolution. Four evaluation points alone do not certify polynomial equality for all B through degree 32; the all-order reasoning below is necessary.

The source's 30 table entries were separately reproduced from KPS (1.38)–(1.40), with symbolic ladders and the precise factorial normalization of Stampedes I (4.1). In particular c^(1)_(2,4)=1 and c^(0)_(2,4)=18/5. This tiny baseline audit is in `ref_source_audit.py`; it does not share the Bessel determinant implementation.

### All-order reasoning

Let D_nu=det(1-K_nu chi) for the Bessel kernel in 2006.01831 (23)–(25). The recurrence for J_(nu+2) gives, with r=sqrt(x), s=sqrt(y),

    (r/s) K_(nu+1)(x,y) = K_nu(x,y)
                         - J_nu(r) J_(nu+1)(s)/(2s).

This identity was also checked by exact symbolic substitution for arbitrary nu. Row and column factors cancel in each Fredholm minor, so unbounded analytic similarity at the origin need not be assumed. At nu=0 this is a rank-one perturbation. The determinant lemma and K_0(0,y)=J_1(sqrt(y))/(2 sqrt(y)) identify

    D_1/D_0 = Q(0),
    Q=(1-K_0 chi)^(-1) J_0(sqrt(x)).

This is precisely Q in [2003.01121](https://arxiv.org/html/2003.01121v4), equation (29). Its exact equation (30), rather than a strong-coupling approximation to that equation, is

    [(g partial_g + 2x partial_x)^2 + x + u-g partial_g u] Q = 0,
    u=-2g partial_g log(D_0).

The formal Bessel/moment expansion is regular at x=0. Consequently its x-derivative terms vanish there. For the common-symbol question, equations (20)–(21) of 2006.01831 show that the simplest/asymptotic numerator difference is suppressed by an inverse power of z in the relevant limit; it disappears under the stated projection.

The remaining delicate step is the coefficientwise scaling of D_0. Stampedes I E.1 and 2003.01121 (4)–(5) imply

    log D_0 -> -LB + pi^2 L^2/6.

At every weak-coupling order, the projected ladder coefficients are polynomials in both logarithms. Their products, formal inverses, and formal logarithms remain polynomial. A polynomial remainder vanishing as the null variable y tends to infinity for every fixed xi is the zero polynomial. This is why the null polynomial can be specialized to the single scaling without claiming a uniform analytic remainder at xi comparable to y. The leading-log projection preserves multiplication, and sends g partial_g to 2L partial_L. Terms with lower A degree vanish in this coefficientwise operation.

It follows that u=4LB-(4/3)pi^2 L^2 and u-2L u_L=-4LB+4pi^2 L^2. Substituting in the boundary equation gives

    L tau_LL + tau_L + (pi^2 L-B) tau=0.

The unit constant coefficient fixes the only regular formal solution: n^2 a_n=B a_(n-1)-pi^2 a_(n-2). The substitution tau=exp(i*pi*L) F(-2i*pi*L) turns this into Kummer's equation with parameter 1/2+iB/(2pi). This establishes the submitted expression within the stated projection. No new proof of the source's whole Toda hierarchy is required or supplied.

### Source sign and finite-B control

The published PDF page 28 really prints a minus sign in the standalone single-LCDS Gaussian. Page 27 E.1–E.2 instead gives the plus sign above: log(cosh(2pi g))/(8pi^2)=g^2/4-pi^2g^4/6+..., with an overall minus sign multiplying the squared logarithm. Independent Fredholm coefficients support the plus sign. In the fresh tests, the minus Gaussian disagrees in 101 of 132 coefficient entries. This is an internal source sign inconsistency, not an arithmetic failure of the submitted formula.

The full finite-B limit is a useful scope control. From the real Bessel symbol (20), at A -> infinity, L=g^2 A fixed, the symbol tends to

    chi(x) = (1+exp(-B))/(1+exp(x/(4L)-B)).

Its exact first moment gives

    [L] (D_1/D_0) = (1+exp(-B))*log(1+exp(B)),

whereas the submitted formal seed has [L] tau=B. At B=2 these are 2.414776415841358... and 2. Their difference is B exp(-B)+(1+exp(-B))*log(1+exp(-B)), invisible to every inverse-log order. Thus a literal finite-B interpretation would fail already at first order. CLAIM.md explicitly excludes these power corrections, and section 4 of the paper explicitly describes retaining the full inverse-log expansion. The control therefore limits interpretation without refuting the stated formal claim.

The trivial I0 control fails already at L^2: it gives B^2/4, while the verified seed gives (B^2-pi^2)/4. In the fresh tests it disagrees in 109 of 132 entries. The closed expression reorganizes an existing exact determinant; it does not improve its numerical accuracy or general coverage.

No statistical hold-out is claimed. The first displayed inverse-log corrections were fitting information. Configuration files document later exact comparisons, but their retrospective timestamps are not a sealed hold-out certificate, and no such certificate is needed or inferred for this formal identity.

## Verdict

_Source: [friends/vieira-stampedes-seed/x004/VERDICT.md](friends/vieira-stampedes-seed/x004/VERDICT.md)_

HOLDS WITH CAVEATS
Referee: gpt-6.1-sol

The Kummer expression matches the paper's formal seed with all inverse-log corrections. The boundary-resolvent argument yields its ODE to all orders within that projection; no counterexample to this stated claim was found.

The published numbers use the claimed normalization: my independent source-based code reproduced all 30 table entries, including c^(1)_(2,4)=1 and c^(0)_(2,4)=18/5. The paper is by Enrico Olivucci and Pedro Vieira.

I independently expanded the published Bessel integral operator, using Cauchy–Binet minors rather than the claimant's KPS elimination. All 528 rational coefficient comparisons through L^32 passed for bridges 0–3 at B=-3/2,2/7,31,0 and pi^2=7/3, including every contributing particle sector. Direct Kummer expansion and 99 symbolic comparisons with the first printed E.7 terms also passed. No claimant implementation was imported or executed.

The I0 control fails already at L^2: B^2/4 versus (B^2-pi^2)/4. It does not explain the corrections. This reformulates an existing exact determinant; it does not improve its accuracy or arbitrary-bridge coverage.

The published PDF contains a real sign conflict: its standalone Gaussian has minus pi^2 L^2/6, while E.1–E.2 and my determinant give plus. The claim openly uses the latter, consistent convention.

There was no statistical or sealed hold-out. The displayed corrections informed the candidate; later coefficient checks are algebraic corroboration, not evidence of predictive generalization.

Relative to Stampedes I, the addition is the closed Kummer form of E.7. Arbitrary-bridge determinants, the null Gaussian, resolvent equations and Toda representation were already public. A 2024 paper (arXiv:2408.15331) also recalls the single-scaling Toda observation; no novelty or priority judgment is made.

Strongest author objection: this is not the literal finite-B seed. The full Bessel-symbol limit has linear coefficient (1+exp(-B))*log(1+exp(B)), about 2.4147764 at B=2, whereas the proposed seed gives 2. Those cross-ratio power corrections are explicitly excluded by the claim and by its full inverse-log interpretation.

Evidence, source receipts, independent code and exact outputs are copied here; see REPORT.md and DERIVATION.md. Tracked pod workers exited, and temporary downloads were removed after verified backup.

NEXT BAR: give a finite-B Fredholm comparison with an explicit bound on the omitted cross-ratio power corrections.

## Prior Art

_Source: [friends/vieira-stampedes-seed/x004/PRIOR_ART.md](friends/vieira-stampedes-seed/x004/PRIOR_ART.md)_

## Independent referee prior-art record — 2026-11-03

Written before referee code. Scope is correctness of the submitted formal light-cone seed, not novelty or priority.

Primary source: Olivucci and Pedro Vieira, Stampedes I, arXiv:2111.12131v2, JHEP07(2022)017. Authorship confirmed on the primary arXiv HTML. Its appendix E asks for resummation of the displayed seed. There is no identified official numerical leaderboard for this symbolic question.

Best public general baseline: Kostov–Petkova–Serban, The Octagon as a Determinant, https://arxiv.org/abs/1905.11467, all-loop arbitrary-bridge ladder determinant. Belitsky–Korchemsky https://arxiv.org/abs/2006.01831 gives the Bessel Fredholm determinant; https://arxiv.org/abs/2003.01121 gives the exact resolvent equations. These cover the octagon more generally than a finite coefficient table. Independent reproduction planned on a rented compute pod from source definitions.

Initial public searches: `"octagon" "single" "light-cone" "Kummer"`, `"Stampedes" "Toda" resummation`, `github octagon Toda Vieira 2026`, `"Stampedes I" Vieira Olivucci`. Located https://arxiv.org/abs/2205.04476 (Stampedes II, higher polygons and Toda equations). No seed competitor identified from this initial search; this is not an absence or novelty claim.

Public code, recently updated repository searches, lab-result repositories, last-year papers, and community sweep will be recorded below. The claimant's prior-art notes are read-only leads, not independent evidence. No contact or account creation.

### Completed independent sweep

All public responses and SHA256 receipts are archived under `evidence/sources/prior_sweep/`. Requests ran on the pod without credentials. GitHub repository API searches were sorted by updated descending: `octagon integrability`, `2111.12131`, `octagon Toda 2026`, `octagon awesome`. The first returned five unrelated MMA/API/watch repositories; the others returned zero. An issue/PR search for the paper ID returned no open matches. The unauthenticated code-search page was fetched, but no exhaustive code-search coverage is inferred.

Read public READMEs of BakeLab/Epi-results, google-deepmind/alphaevolve_results, openai/math, plasma-ai/erdos and kisonecat/openai-math. No relevant seed result was identified there. BakeLab's octagon hit concerns circle packing. The alphaevolve_results public tree had no path matching octagon, Toda, stampede or repository_of_problems. Guessed standalone google-deepmind/repository_of_problems and EinsteinArena/EinsteinArena README URLs returned 404; EinsteinArena's public website was fetched separately. These limitations remain explicit.

The arXiv API query for octagon AND (Toda OR light-cone), submitted 2025-11-03 through 2026-11-03, returned no entries. Additional public indexed searches for octagon/Kummer, octagon/confluent hypergeometric, Stampedes/Toda resummation, and 2025/2026 light-cone octagons identified no competing expression. Searches for Stampedes I on Reddit and Vieira/stampedes on X produced no relevant primary result; this is limited search visibility, not evidence of absence.

An additional primary paper encountered was Loebbert–Stawinski, https://arxiv.org/abs/2408.15331 (JHEP11(2024)092), on conformal integrals and Toda equations. Its octagon discussion recalls the previously known one-dimensional Bessel determinant and the two-dimensional single-scaling Toda observation, citing Stampedes I; it does not supply the submitted Kummer expression in that discussion. Stampedes II (2205.04476) concerns higher polygons.

The baseline reproduction succeeded: all 30 displayed coefficients, including 1 and 18/5 for c_(2,4) at bridges 1 and 0, from an independently transcribed public KPS formula. A different public Bessel determinant representation then independently confirmed the submitted seed through L^32 at four fresh parameter points. See `REPORT.md` and `DERIVATION.md`.

Final source/repository pass completed 2026-11-03 around 22:51 UTC. The factual addition relative to Stampedes I is a closed Kummer expression for its formal inverse-log seed. Arbitrary-bridge all-loop determinants, the null Gaussian, exact resolvent equations, and the stated Toda determinant were already public. No judgment of novelty, priority, or author interest is made.

---

# Pedro Vieira — what the seed's ODE is (Coulomb follow-up)

Folder: [friends/vieira-stampedes-seed/coulomb-follow-up](friends/vieira-stampedes-seed/coulomb-follow-up)

## Derivation

_Source: [friends/vieira-stampedes-seed/coulomb-follow-up/DERIVATION.md](friends/vieira-stampedes-seed/coulomb-follow-up/DERIVATION.md)_

## What the differential equation means, and what it does not establish

All identities refer to the leading-power double-light-cone projection specified in X004, keeping every inverse logarithm. They are formal coefficientwise statements before resummation; the resulting entire Kummer function also has well-defined analytic consequences. Neither projection nor coefficient comparison supplies a uniform error estimate for the full octagon at fixed cross ratios or at large L.

### 1. Standard route: the bridge is a dressed boundary mode

Use the generalized Bessel kernels of [Belitsky–Korchemsky, 2006.01831, Eqs.(3.15)–(3.17)](https://arxiv.org/abs/2006.01831) and the zero-bridge kernel of [2003.01121, Eqs.(2.15)–(2.17)](https://arxiv.org/abs/2003.01121):

    K_nu(x,y) = [sqrt(x) J_(nu+1)(sqrt(x)) J_nu(sqrt(y))
                  - sqrt(y) J_nu(sqrt(x)) J_(nu+1)(sqrt(y))]/[2(x-y)].

The elementary recurrence J2(t)=2J1(t)/t-J0(t) gives exactly

    sqrt(x/y) K1(x,y) = K0(x,y) - J0(sqrt(x)) J1(sqrt(y))/(2 sqrt(y)).

This is a rank-one change after the multiplication conjugation. Write D_l=det(1-K_l chi) and Q=(1-K0 chi)^(-1)J0. The determinant lemma yields

    D1/D0 = 1 + integral_0^infty J1(sqrt(y))/(2 sqrt(y)) chi(y) Q(y) dy
          = Q(0),

because K0(0,y)=J1(sqrt(y))/(2 sqrt(y)) and J0(0)=1. The manipulation uses the conventional regularized Fredholm setting, or coefficientwise perturbation theory; it is not an unproved bounded similarity transformation on arbitrary weighted spaces. The corresponding finite-matrix/fermionic interpretation is already explicit in [Kostov–Petkova, 2102.05000, Eqs.(1.8), (2.34)–(2.41)](https://arxiv.org/abs/2102.05000): the bridge inserts fermions and the ratio is a resolvent entry. The physical content of this route is an auxiliary boundary wave, already present in the standard determinant formulation.

In 2003.01121 Eq.(2.24) (PDF p11, printed p10), the published auxiliary equation is

    [(g d_g + 2x d_x)^2 + x + u - g d_g u] Q(x) = 0,
    u = -2g d_g log D0.                         [Eq.(2.21)]

After the claimed coefficientwise projection, L=g^2 log z, B=log(1/zbar), so g d_g=2L d_L. At x=0 use

    log D0 = -LB + pi^2 L^2/6,
    u = 4LB - (4/3) pi^2 L^2,
    u - g d_g u = -4LB + 4pi^2 L^2.

Dividing by 4L gives L tau_LL+tau_L+(pi^2 L-B)tau=0. This explains why a linear wave equation arises: it is the existing determinant's auxiliary resolvent problem evaluated at its endpoint. The reduction still inherits X004's assumption that the simplest and asymptotic symbols agree after the specified leading-power projection. This job does not newly prove that projection, nor the Toda hierarchy's microscopic origin.

There is a source sign inconsistency already recorded in X004: the standalone single-LCDS Gaussian in Stampedes I prints a minus sign on pi^2 L^2/6, whereas its preceding expansion and the printed seed coefficients require plus. Using the standalone minus sign instead produces L tau_LL+tau_L+(-pi^2 L-B)tau=0, with coefficient (B^2+pi^2)/4 at L^2, contradicting the printed seed. We use the convention consistent with that seed, not a newly asserted correction to a full observable.

`code/resolvent_check.py` verifies the kernel identity, the endpoint, the potential and both Gaussian signs symbolically. This is a short derivation from published machinery, not a new numerical standard.

### 2. Exact radial and Kummer dictionaries

In units hbar^2/(2m)=1, the zero-angular-momentum radial Laplacian in d dimensions is d_L^2+(d-1)L^(-1)d_L. Its coefficient here fixes d=2. Thus

    H_B = -d_L^2 - L^(-1)d_L + B/L,
    H_B tau = pi^2 tau.

The natural radial measure is L dL. Requiring a finite, no-log solution at the origin fixes tau(0)=1 and tau_L(0)=B. Removing that measure gives

    u=sqrt(L)tau,
    -u_LL + [B/L - 1/(4L^2)]u = pi^2 u.

The no-log boundary excludes sqrt(L) log L; simply imposing u(0)=0 would not select it. It is the regular/Friedrichs radial boundary, not a choice of additional contact interaction at the origin. The potential is 1/r restricted to a plane; strictly 2D electrostatics has a different potential. With rho=pi L and eta=B/(2pi),

    u_rhorho + [1 - 2eta/rho + 1/(4rho^2)]u = 0.

This is the Coulomb equation with formal angular index ell=-1/2, analytically continued from the usual integer-index convention. Equivalently the Whittaker index is mu=0, kappa=-i eta, argument -2i rho. Direct substitution tau=e^(i pi L)v(-2i pi L) gives

    z v_zz + (1-z)v_z - (1/2+i eta)v = 0.

[DLMF 33.2.4–5](https://dlmf.nist.gov/33.2#ii) then gives

    tau = F_(-1/2)(eta,rho)/(C_(-1/2)(eta) sqrt(rho)),
    C_(-1/2)^2 = pi/(1+exp(B)).

The latter follows from Gamma(1/2+i eta)Gamma(1/2-i eta)=pi/cosh(pi eta). Here B is charge at fixed scattering energy. Treating B instead as a spectral parameter of -(L d_L)' - pi^2 L is another valid Sturm–Liouville rewriting, with position-dependent kinetic coefficient; it is not the conventional constant-mass hydrogen Hamiltonian. For positive B this is repulsive scattering, not a bound-state spectrum. No map from a new SYM particle's physical position to L was derived.

### 3. Consequences and comparison with the paper

At fixed real B the usual Coulomb phase is rho-eta log(2rho)+pi/4+arg Gamma(1/2+i eta). It gives the expansion in PHYSICS.md with additive O_B(L^(-3/2)) error. Use a continuous branch for the Gamma phase. At B=0 the exact answer is J0(pi L), recovering its phase and amplitude. This B=0 substitution evaluates formal coefficient polynomials; it is not itself the physical large-B light-cone limit.

For the strict double scaling set x=LB and tau=f(x), at fixed B. Exactly,

    x f_xx + f_x - f + (pi^2/B^2) x f = 0.

Taking B to infinity at fixed x gives I0(2sqrt(x)), the seed in Stampedes II. More explicitly, with s=sqrt(LB), the first three inverse-log families printed in Stampedes I Eq.(93) are

    I0(2s)
    + pi^2 L/(6B) [I2(2s)-2s I1(2s)]
    + pi^4 (L/B)^2/360 [(20s^2+7)I4(2s)+32s I3(2s)] + ... .

Substituting the ODE recurrence

    (n+1)^2 a_(n+1) = B a_n - pi^2 a_(n-1), a_0=1, a_-1=0

reproduces each of those three families through L^20 exactly. In particular

    tau=1+BL+(B^2-pi^2)L^2/4+(B^3-5Bpi^2)L^3/36+... .

The referee separately starts with the exponential/Kummer Cauchy product, transcribes the printed Bessel families, and finds the same coefficients. These are exact algebra comparisons; there is no trained predictor, split, predictive score, or accuracy-improvement claim requiring SBS. The standard determinant remains exact and more general.

For the positive zeros, differentiate (L tau')'+(pi^2L-B)tau=0 in B, with v=partial_B tau. Then

    [L(tau v'-tau'v)]' = tau^2.

The origin Wronskian vanishes. At a simple zero r_n, tau'(r_n) is nonzero by uniqueness of the regular ODE away from zero. Integration and implicit differentiation give

    r_n'(B) = integral_0^(r_n) tau^2 dL / [r_n tau'(r_n)^2] > 0.

Oscillation theory or Coulomb asymptotics supplies infinitely many positive simple zeros for every fixed real B. For example the first zero at B=0 and 2 is 0.76547974956201235684 and 1.13298306096691880155 in both implementations. These are calculated values of the projected function. The source does not print large-L zero data; this job has not tested those zeros against an independent finite-cross-ratio octagon or new observed data.

### 4. Other candidate interpretations

| Candidate | Exact test | Outcome |
|---|---|---|
| Ordinary 3D hydrogen s wave, B an energy | Radial measure removal leaves -1/(4L^2); B multiplies 1/L | Rejected in that form. Keep the 2D scattering dictionary above. |
| Direct Fokker–Planck evolution/probability tau | D=L d_L^2+d_L is the backward generator of dX=dt+sqrt(2X)dW, but the full equation is (D+pi^2 L)tau=B tau; tau at B=0 is sign-changing J0 | Reject tau as a normalized transition probability on the whole half-line. A weighted spectral/Feynman–Kac representation is algebraically possible, but no microscopic stampede identification was found. |
| Microscopic spin-chain transfer matrix | The source's actual SL(2) Hamiltonian evolves in first-order logarithmic time; no explicit conjugation or scaling map to H_B has been derived | Existing stampede language remains valid; a two-component rewrite of this ODE alone would not explain its microscopic Hamiltonian. Keep only the published fermionic boundary-resolvent interpretation. |
| Toda/Painlevé | T_l=det[partial_L^(i-1)partial_B^(j-1)tau] obeys the published Toda identity by the determinant identity; q=L partial_L log tau obeys L q'=BL-pi^2L^2-q^2 | Keep Toda as existing determinant structure and the exact Riccati reduction. No specific new Painlevé parameter map or microscopic Toda mechanism was established, so none is claimed. |

The strict radial Bessel Toda reduction cannot simply be reused at finite B: tau depends independently on LB and the inverse-log correction. Already (L partial_L-B partial_B)tau=-pi^2 L^2/2+... is nonzero, so it is not just a function of LB. This prevents promoting Stampedes II's one-variable seed to the corrected answer by renaming its argument.

### 5. Reproduction and novelty

Run these from this directory, one at a time (Python dependencies: SymPy 1.14.0 and mpmath 1.3.0):

    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 10 .venv/bin/python code/physics_check.py
    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 10 .venv/bin/python code/resolvent_check.py
    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 10 .venv/bin/python code/referee_check.py

The corresponding JSON outputs are in data/. Main and referee code were written independently; neither imports the earlier X004 implementation. The referee additionally evaluates an angular Euler integral and the zero-derivative Wronskian integral. No cluster, remote computation or person was contacted. Research computations used one core per process, thread counts 1 and nice 10, with at most two simultaneous computations on one local machine.

NEW: no for a new physical-result claim from this follow-up. The closed-form seed is the pre-existing X004 result. This job explains it and states standard consequences of its special function. It neither beats a printed number nor tests a physical prediction on new data, nor resolves the missing microscopic Toda/stochastic explanation. The narrow prior-art conclusion in PRIOR_ART.md does not turn this explanatory reformulation into a new discovery.

## Physics

_Source: [friends/vieira-stampedes-seed/coulomb-follow-up/PHYSICS.md](friends/vieira-stampedes-seed/coulomb-follow-up/PHYSICS.md)_

The seed is an origin-normalized radial Coulomb scattering wave in two dimensions. This is an exact auxiliary Schrödinger interpretation, with checkable consequences; a microscopic Coulomb particle in the gauge theory has not been derived.

For real $L>0$, divide the equation by $L$:
\[
\left[-\partial_L^2-L^{-1}\partial_L+\frac{B}{L}\right]\tau=\pi^2\tau.
\]
The first two terms are the two-dimensional radial Laplacian in the zero-angular-momentum sector. In units \(\hbar^2/(2m)=1\), \(L\) is radius, \(B\) is Coulomb strength, and energy is fixed at \(\pi^2\). Positive \(B\) is repulsive. This is the usual planar \(1/r\) potential, not the logarithmic electrostatic potential of strictly two-dimensional electromagnetism. The regular origin condition gives \(\tau(0)=1,\ \tau'(0)=B\). Equivalently, \(u=\sqrt L\tau\) obeys
\[
-u''+\left(\frac B L-\frac1{4L^2}\right)u=\pi^2u;
\]
the inverse-square term cannot be discarded to call this three-dimensional hydrogen.

There is also a direct octagon meaning: a bridge insertion is a fermionic boundary insertion, and \(O_1/O_0\) is a dressed Bessel boundary mode. The published Fredholm-resolvent equation reduces at that boundary to this ODE. Thus the scattering wave describes an auxiliary mode of the existing determinant, not an independently postulated microscopic Hamiltonian. See [the derivation](friends/vieira-stampedes-seed/coulomb-follow-up/DERIVATION.md) and [Kostov–Petkova, Eqs.(1.8), (2.34)–(2.41)](https://arxiv.org/abs/2102.05000).

The intuition is useful. Increasing the repulsion delays oscillations. If \(r_n(B)\) is a positive zero, exact differentiation gives
\[
\frac{dr_n}{dB}=\frac{\int_0^{r_n}\tau(L,B)^2\,dL}{r_n\tau_L(r_n,B)^2}>0.
\]
For fixed \(B\), put \(\eta=B/(2\pi)\). Standard [Coulomb asymptotics](https://dlmf.nist.gov/33.11), continued to angular index \(-1/2\), give
\[
\tau=\frac{\sqrt{1+e^B}}{\pi\sqrt L}
\sin\!\left[\pi L-\eta\log(2\pi L)+\frac\pi4+\arg\Gamma(\tfrac12+i\eta)\right]
+O_B(L^{-3/2}).
\]
The logarithm is the Coulomb phase shift. The Fermi-looking amplitude follows from Gamma normalization; it does not establish a thermal stampede.

Why did Stampedes II find a Bessel function? At fixed \(x=LB\), sending \(B\to\infty\) changes the equation to \(xf''+f'-f+(\pi^2/B^2)xf=0\), hence \(f\to I_0(2\sqrt x)\). The energy correction disappears. Retaining it reproduces the printed \(\pi^2\) and \(\pi^4\) corrections in Stampedes I Eq.(93)/published Eq.(E.7), independently checked here. Those printed coefficients confirm the local expansion; the papers contain no large-\(L\) zero data. The zeros and asymptotics are consequences of the projected seed, not established zeros or asymptotics of the full finite-cross-ratio octagon. A direct probability interpretation fails because this wave changes sign. No microscopic spin-chain or new Painlevé explanation was established.

## Referee

_Source: [friends/vieira-stampedes-seed/coulomb-follow-up/REFEREE.md](friends/vieira-stampedes-seed/coulomb-follow-up/REFEREE.md)_

## Independent referee of the seed's physical interpretation

**Verdict: the radial Coulomb interpretation and its stated mathematical consequences hold, within the projected sector. No independently established new physical phenomenon.** This check was written separately from the main computation, without importing its implementation or the earlier X004 worker/referee code.

### Direct answer and exact mapping

For real L>0 and B, divide the proposed ODE by L. It is exactly the m=0 radial equation of the two-dimensional operator

    H_B = -d_L^2 - L^(-1) d_L + B/L,    H_B tau = pi^2 tau.

Here L is radius, B is Coulomb coupling, and the energy is the fixed number pi^2, in units hbar^2/(2m)=1. The potential is repulsive for B>0. It is not the usual three-dimensional hydrogen s wave, nor a bound-state spectrum with B as energy. The origin condition selects the regular, no-log branch: tau(0)=1 and tau'(0)=B. Removing the radial measure, u=sqrt(L)tau satisfies

    -u'' + [B/L - 1/(4L^2)]u = pi^2 u.

The extra critical inverse-square term is essential. The usual regular boundary excludes sqrt(L)log(L). Setting rho=pi L and eta=B/(2pi) gives the Coulomb equation of formal angular momentum ell=-1/2. Continuing the [DLMF regular normalization, Eqs.33.2.4–5](https://dlmf.nist.gov/33.2#ii), to ell=-1/2,

    tau(L,B) = F_{-1/2}(eta,rho)/(C_{-1/2}(eta)sqrt(rho)),
    C_{-1/2}(eta)^2 = pi/(1+exp(B)).

This is an exact special-function/Schrodinger dictionary, not a derived microscopic Hamiltonian for a new particle in SYM. In particular, the literal two-dimensional electrostatic potential of an isolated point charge would be logarithmic; the operator here is the mathematically standard 1/r Coulomb potential restricted to a plane.

### Consequences derived independently

At fixed real B, the [DLMF large-rho Coulomb expansion](https://dlmf.nist.gov/33.11), continued to ell=-1/2, gives

    tau ~ sqrt(1+exp(B))/(pi sqrt(L)) sin[pi L - eta log(2pi L)
                                                    + pi/4 + arg Gamma(1/2+i eta)],

with additive O(L^(-3/2)) corrections for fixed B (and continuous Gamma phase). At B=0 it reduces exactly to J0(pi L), including the Bessel phase and amplitude. The factor 1+exp(B) comes from the Gamma reflection identity, not an independent identification of a thermal stampede.

Every positive zero is simple and moves strictly to larger L as B increases. If r_n(B) is such a zero,

    dr_n/dB = integral_0^{r_n} tau(L,B)^2 dL / [r_n tau_L(r_n,B)^2] > 0.

Proof: write (L tau')'+(pi^2 L-B)tau=0, differentiate in B, and set v=partial_B tau. Then [L(tau v'-tau'v)]'=tau^2. The regular origin contributes zero boundary Wronskian. At a zero, differentiating tau(r_n(B),B)=0 gives the formula. For example the first zeros at B=0,2,5 are respectively 0.76547974956201235684, 1.13298306096691880155, and 1.62076904982393453201.

For the strict double-scaling limit x=LB fixed, L tends to zero and B to infinity. The equation becomes x f''+f'-f+(pi^2/B^2)xf=0. Dropping the vanishing energy correction gives f=I0(2sqrt(x)), precisely Stampedes II's seed. This explains why its strict limit loses the term that distinguishes the present equation.

### What was recomputed

Run `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 10 .venv/bin/python code/referee_check.py`. Output is `data/referee_check.json`.

The code starts from the defining exponential and Kummer power series, using their finite Cauchy product. It independently transcribes the Bessel formula in Stampedes I arXiv v2 Eq.(93), Appendix E, PDF p32/printed p31. Its pi^0, pi^2 and pi^4 families give 39 exact rational symbolic coefficient identities through L^14. These all hold. Fourteen coefficients obey the proposed ODE. Exact generic substitutions verify Kummer's equation, the radial reduction, and the moving-zero Wronskian identity.

As a distinct numerical representation, Euler's beta integral gives

    tau = cosh(pi eta)/pi integral_0^pi
                    cos[rho cos(theta)-2 eta log(cot(theta/2))] dtheta.

Direct quadrature agrees with Kummer evaluation at (L,B)=(1/8,2),(5/4,2),(7/2,-1), to over 40 decimal places. At twelve zeros (first three at B=-2,0,2,5), implicit differentiation agrees with the positive Wronskian integral. Large-L examples at L=20.25,100.25,1000.25 illustrate the stated Coulomb phase/amplitude. These are mathematical corroboration, not comparisons to new observed octagon data. No predictive accuracy score or trained predictor is involved.

### Other proposed pictures

A direct nonnegative-probability interpretation of tau on all L>0 fails: even B=0 gives J0(pi L), which changes sign. The differential part D=L d_L^2+d_L is a valid squared-Bessel backward diffusion generator (dX=dt+sqrt(2X)dW), but the complete equation is (D+pi^2 L)tau=B tau. It is a spectral equation with a growth/weight term, not a normalized Fokker-Planck evolution equation. This does not forbid more elaborate weighted stochastic representations; none establishes the stampede's microscopic randomness here.

A first-order two-component system can always be built from this scalar ODE. Calling that a transfer matrix does not identify it with the spin-chain Hamiltonian or an existing physical transfer matrix. Similarly the seed together with the already published mixed-derivative determinant generates the Toda hierarchy, but this ODE alone neither derives the Toda structure nor proves a new Painleve reduction. Those additional physical explanations have not been established by this check.

### Independent full-text reading relevant to equivalents

I read Stampedes I Appendix E and all nine pages of [Stampedes II](https://arxiv.org/abs/2205.04476), plus the following full papers including appendices and references:

- [Spinning Hexagons, 2207.08931](https://arxiv.org/abs/2207.08931), 41 PDF pages. Eq.(42) gives two Pfaffians for asymptotic three-spinning structure constants. Eqs.(56)-(57), PDF p32/printed p31, relate their large-spin limit to Wilson-loop/pentagon observables; explicitly evaluating that limit is future work. No seed-equivalent differential equation or Kummer answer occurs.
- [Complex Spin: The Missing Zeroes and Newton's Dark Magic, 2211.13754](https://arxiv.org/abs/2211.13754), 14 PDF pages. Appendix F, PDF p13, already uses the hydrogen/Coulomb scattering analogy for Regge trajectories. Its f_S(E)=Gamma(1+S-eta)/Gamma(1+S+eta), eta=1/sqrt(-E), and Eq.(F1) residue zeros concern three-dimensional orbital spin and missing bound states. They are not this octagon's two-log seed or zeros versus L. Do not claim the first Coulomb analogy in Vieira's work.
- [Light-Ray Wave Functions and Integrability, 2409.02160](https://arxiv.org/abs/2409.02160), 52 PDF pages. Its tau(u) in Eqs.(21)-(25) is a polynomial transfer-matrix eigenvalue in spectral rapidity u; Eq.(24) is third-order in the angular parton coordinate theta and depends on spin S and charge q. Fourier recursion (27) has cubic-in-mode coefficients. Appendix C, Eqs.(111)-(118), constructs Baxter Q integrals and recovers Janik's twist-two function. These are not the second-order two-log seed, even though tau, hypergeometric functions, and differential equations appear.
- [The Loom for General Fishnet CFTs, 2212.09732](https://arxiv.org/abs/2212.09732), 42 PDF pages. Conclusions, PDF p36/printed p35, fourth bullet, asks how to count stampedes on M-Loom diagrams. It gives no seed-equivalent octagon formula or Coulomb radial equation. The classification of chiral integrable graphs and tT spectral reality is distinct from the present seed.

Stampedes II, first page, Eq.(2) and following paragraph, expressly has seed I0(2s) and leading-log cusp scaling, not all inverse-log corrections. Its random walks in Weyl chambers, Appendix E Eq.(25), concern this stricter Bessel-determinant limit. These do not supply the corrected Kummer seed. This reading supports a narrow absence statement for these papers, not exhaustive literature novelty.

### Novelty assessment

The exact radial dictionary, Coulomb phase, and zero-delay identity are useful explanatory consequences of the seed. They are standard consequences of the already identified confluent hypergeometric function. None of the checks here tests a new physical prediction on new data, beats a printed numerical target, or derives the missing microscopic Toda/spin-chain mechanism. I recommend `NEW: no` for a new physical-result claim from this check alone. The parent should separately judge whether the existing seed resummation still settles the stated printed open problem after its full prior-art search. An absence in the selected papers does not prove priority. Large-L zeros of a resummed leading-power projection must not be presented as zeros of the literal finite-cross-ratio octagon without a uniform control of the discarded terms.

### Additional author-scope cross-check (requested separately)

I retrieved and read both remaining papers in full, including supplements and references. Their PDFs and extracted full text are in `sources/2210.04923.pdf`, `sources/2210.04923.referee.txt`, `sources/2404.10812.pdf`, and `sources/2404.10812.referee.txt`.

- [Structure Constants in N=4 SYM and Separation of Variables, 2210.04923](https://arxiv.org/abs/2210.04923), 14 PDF pages: Eqs.(2)–(6) are finite-dimensional SoV overlaps of Baxter functions for three-point functions, with one-particle measure proportional to sech²(pi u). Appendix B Eq.(B1) gives Hahn 3F2 polynomials, and Eqs.(9)–(10)/(B5) are finite-difference Baxter equations in spectral rapidity u. These are not the Kummer 1F1 two-log octagon seed. The discussion on PDF p7 specifically proposes recasting Coronado's four-point octagon in this SoV language as future work, possibly using its existing determinant; the large-spin/Wilson-loop connection is likewise prospective. No equivalent Coulomb radial equation or resummation of the Appendix E inverse-log seed appears. The overlap ratios concern individual OPE structure constants, not the summed four-point bridge ratio O1/O0.
- [Multiparticle Flux Tube S-matrix Bootstrap, 2404.10812](https://arxiv.org/abs/2404.10812), 18 PDF pages: this studies collinear Goldstone/branon jets on the confining flux tube of primarily three-dimensional Yang-Mills theories. Eqs.(3)–(5) define jet states; Eq.(7) defines finite-energy S-matrix observables at s=i; Eq.(11) is a conformal-map scattering-amplitude ansatz. Supplement S4 concerns a Nambu–Goto effective string, with tau(x)=x(1-x)(1-x+x²) in Eq.(S4.7) just a jet energy-fraction polynomial. None is an N=4 null-polygon/light-cone octagon seed, and no Kummer, Whittaker or Coulomb equivalent occurs. The shared phrase 'flux tube' refers to a different physical problem and supplies no missing microscopic interpretation for the Stampedes seed.

## Prior Art

_Source: [friends/vieira-stampedes-seed/coulomb-follow-up/PRIOR_ART.md](friends/vieira-stampedes-seed/coulomb-follow-up/PRIOR_ART.md)_

Partly there. Stampedes II does not contain the corrected Kummer seed or its scalar ODE. It contains its stricter Bessel limit. The full determinant, a bridge-as-fermion/resolvent interpretation, and the auxiliary differential equation from which the seed follows were already published. I did not find an explicit equivalent closed seed in the author papers and forward citations examined. That limited absence statement is not a proof of priority.

Checked locally on 2026-11-05. Public sources were read without contacting authors, creating an account/key, or uploading this work. PDFs and complete extracted texts are retained in sources/. Page references below distinguish PDF page and printed page where they differ.

### Pedro's second paper: a direct answer

[Olivucci–Vieira, arXiv:2205.04476](https://arxiv.org/abs/2205.04476) is titled **Stampedes II: Null Polygons in Conformal Gauge Theory** on the arXiv PDF; the journal title is **Null Polygons in Conformal Gauge Theory**, [PRL 129, 221601 (2022)](https://doi.org/10.1103/PhysRevLett.129.221601). The complete nine-page arXiv paper, including appendices, was read independently by both workers.

- **Page 1, Eq.(1):** its cusp scaling fixes products of two large logarithms times g^2, while g tends to zero. This retains the highest logarithms, not all inverse-log corrections.
- **Page 1, Eq.(2) and its following paragraph:** the square is exp(-s^2) tau_l(s), tau_0=1, and the one-bridge seed is described as “a modified Bessel function I0(2s).” It generates Bessel determinants. Under s^2=LB, this is the B to infinity, L to zero limit of X004. At finite independent L,B the L^2 coefficient would be B^2/4 for this Bessel seed, versus (B^2-pi^2)/4 for X004. They are not the same answer in different variables.
- **Page 4, Eqs.(14)–(15):** the function phi(x,y,z) is a three-cusp pentagon seed with a triple sum and nested determinants, not the square seed corrected to every inverse logarithm.
- **Page 6, Appendix B, Eq.(21):** the broader single-light-cone regime is discussed as requiring a refined spin-chain treatment. No corrected closed square seed is supplied there.
- **Page 8, Appendix E, Eqs.(25)–(28):** generalized Bessel determinants and matrix integrals; the random walks concern the stricter Bessel limit. None supplies this two-log Kummer function or its equivalent Coulomb/Whittaker scalar equation.

Thus the answer to “is it already in our second paper?” is **no for the corrected closed seed and ODE; yes for their strict Bessel limit and associated Toda structures**.

### What was already available outside Stampedes II

| Primary source | Location and content | Relation to X004 |
|---|---|---|
| [Stampedes I, 2111.12131v2](https://arxiv.org/abs/2111.12131v2) | Section 4, Eqs.(42)–(44), printed pp15–16; Appendix E, Eqs.(93)–(96), PDF p32/printed p31; following paragraph PDF p33/printed p32 | The corrected seed is a Bessel expansion, with mixed-derivative Toda determinants. It asks for a “simple closed expression for τ” and to understand “why a Toda equation still governs this limit.” A closed seed addresses the former; it does not derive the latter mechanism. Published numbering calls the seed Eq.(E.7). |
| [Belitsky–Korchemsky, Octagon at finite coupling, 2003.01121](https://arxiv.org/abs/2003.01121) | Eqs.(2.15)–(2.24), PDF pp9–11/printed pp8–10 | Modified Bessel Fredholm determinant; Q=(1-K chi)^(-1)J0; u=-2g partial_g log O; [(g partial_g+2x partial_x)^2+x+u-g partial_g u]Q=0. This is the existing linear auxiliary wave problem, not an explicit Kummer answer for the two-log ratio. Its boundary reduction, together with the rank-one bridge identity and projected zero-bridge Gaussian, gives the ODE. |
| [Belitsky–Korchemsky, Crossing bridges with strong Szegő limit theorem, 2006.01831](https://arxiv.org/abs/2006.01831) | Section 3.2, Eqs.(3.15)–(3.17), PDF p12/printed p11; Eq.(3.12) gives the distinct simplest/asymptotic symbols | The exact arbitrary-bridge Bessel kernel is already known. Its two consecutive orders have the rank-one relation used in DERIVATION.md. This is an exact general representation containing the answer implicitly. |
| [Kostov–Petkova, Octagon with finite bridge, 2102.05000](https://arxiv.org/abs/2102.05000) | Eqs.(1.6)–(1.8), PDF p5/printed p4; Eqs.(2.34)–(2.41), PDF pp10–11; Section 5, Eqs.(5.1)–(5.3), printed p20 | O1/O0=1+R^ee_00 and the bridge as a fermion insertion are explicit. Thus a resolvent/fermion answer is already there. Its explicitly solved light-cone scaling seed is Bessel, with full 2D Toda in two scaling coordinates; no corrected Kummer evaluation of that resolvent entry is given. The paper was read in full. |
| [Belitsky, Null octagon from Deift–Zhou steepest descent, 2012.10446](https://arxiv.org/abs/2012.10446) | Eqs.(3)–(9), printed pp1–2; Eq.(4) has the Fermi distribution; Eqs.(59)–(60), printed pp9–10 | Finite-temperature Bessel determinant and null Gaussian asymptotics are prior art. The complete paper does not evaluate this one-bridge, two-log seed as a Kummer function. A Fermi-looking factor in Coulomb normalization alone is therefore no new thermal explanation. |
| [Loebbert–Stawinski, 2408.15331](https://arxiv.org/abs/2408.15331) | Section 3.4, Eqs.(3.54)–(3.55) and next two paragraphs, PDF p34/printed p33 | Recalls the Bessel determinant and explicitly attributes the single-scaling 2D Toda observation to Stampedes I. It gives no closed corrected seed. Its future-work statement concerns a similar equation for the **full octagon**; it must not be quoted as saying that the known single-scaling Toda equation itself was left to future investigation. |

These distinctions are why “partly there” is more accurate than an unqualified claim that the result had no precedent. In particular, an equivalent *unevaluated* boundary resolvent was already public. I found no published evaluation of that resolvent into this Kummer answer in the reviewed sources.

### Other Olivucci or Vieira papers: full-text reading and false equivalents

INSPIRE author identities P.Vieira.1 and E.Olivucci.1 were queried for 2021–2026, rather than relying on ambiguous surname matches. The returned portfolios have 21 and 11 records respectively (including papers published in 2021 with earlier arXiv identifiers). Their titles/abstracts were screened for the requested subjects. Relevant works and adjacent apparent equivalents were read in full, including appendices; the independent reader's details are in REFEREE.md.

| Paper | Full-text finding |
|---|---|
| [Light-Cone Bootstrap of Higher Point Functions and Wilson Loop Duality, 2008.10407](https://arxiv.org/abs/2008.10407), published 2021, 9 PDF pages | Light-cone multipoint OPE and Wilson-loop recoil, Eqs.(12), (17), (21)–(23). Kummer 1F1 occurs in Eq.(3)/Appendix A as a descendant operator with parameters conformal spin; it is not the two-log bridge-ratio seed. |
| [The Wilson Loop—Large Spin OPE Dictionary, 2110.04364](https://arxiv.org/abs/2110.04364), 35 pages | Eq.(23) is the normalized structure-constant/Wilson-loop map; Appendix E contains Casimir differential equations and Appendix F harmonic-number/binomial sums. No closed bridge-ratio seed or equivalent scalar equation. |
| [Spinning Hexagons, 2207.08931](https://arxiv.org/abs/2207.08931), 41 pages | Eq.(42) has Pfaffians for three-spinning structure constants. Eqs.(56)–(57), PDF p32, concern a further large-spin Wilson-loop limit. Neither the same determinant nor the same seed. |
| [Structure constants in N=4 SYM and separation of variables, 2210.04923](https://arxiv.org/abs/2210.04923), 14 pages | Baxter/SoV overlaps, Eqs.(2)–(6), and Hahn 3F2 in Appendix B; octagon reformulation through SoV is future work on PDF p7. No two-log Kummer seed. |
| [Complex Spin / Multitwist Trajectories and Decoupling Zeros, 2211.13754](https://arxiv.org/abs/2211.13754), 14 pages | **A Coulomb/hydrogen analogy is already in Vieira's work:** Appendix F, PDF p13, Eq.(F1). Its Gamma-ratio partial-wave amplitude and residue zeros concern orbital spin and missing bound states in 3D. They are not this 2D radial wave or its zeros versus L. No first-Coulomb-analogy claim is justified. |
| [The Loom for General Fishnet CFTs, 2212.09732](https://arxiv.org/abs/2212.09732), 42 pages | Conclusions, PDF p36/printed p35, fourth bullet asks about counting stampedes on M-Loom diagrams. No corrected octagon seed or radial equation. |
| [Hexagonalization of Fishnet integrals II, 2306.04503v3](https://arxiv.org/abs/2306.04503v3), 47 pages | SoV tile/overlap formulae, Sections 4–6; the light-cone polygon limit appears as an outlook in Section 7, PDF p31/printed p30. It does not carry out that limit or evaluate the seed. |
| [Multipoint fishnet Feynman diagrams: sequential splitting, 2307.12984](https://arxiv.org/abs/2307.12984), 27 pages including supplement | Main Eqs.(15)–(19), supplement Section VI Eqs.(89)–(123), give fishnet stampedes and a vertex model for leading-log coefficient functions. This is genuine later stampede work, but its chiral fishnet vertex weights and finite-diagram maximal logs are not the corrected N=4 octagon bridge ratio. |
| [Light-ray wave functions and integrability, 2409.02160](https://arxiv.org/abs/2409.02160), 52 pages | Its tau(u), Eqs.(21)–(25), is a polynomial transfer eigenvalue in rapidity; Eq.(24) is a third-order angular wave equation, and Eq.(27) has cubic mode coefficients. Appendix C's Baxter/Hahn functions do not identify this second-order L,B seed. |
| [Multiparticle Flux-Tube S-matrix Bootstrap, 2404.10812](https://arxiv.org/abs/2404.10812), 18 pages | Screened because of its title, then fully read: confining Yang-Mills/branon scattering, rather than N=4 null-polygon light-cone OPE. Its tau(x) is an energy-fraction polynomial, not the octagon function. |

Stampedes I/II were also read in full. The 2021 mirror-excitation methods paper 2107.13035 was downloaded and text-screened as background, not claimed as another full reading of a light-cone-limit result. The remaining portfolio records concern other subjects (spectra of generalized fishnets, huge/heavy operators, scattering bootstrap, gravity or quantum sampling); none was used as evidence of absence from an unread full paper. No additional 2025–2026 authored paper on the requested limit was identified in these disambiguated portfolios. These author-index and full-text limits are explicit; this is not a claim to have read every paper by either author.

### Forward citations: what was actually checked

1. A local citation helper, `cited-by '10.1007/JHEP07(2022)017'`, was run normally. Its OpenAlex citing-work request failed after its built-in retries with **HTTP 429**; data/cited_by.txt preserves the error. No account or key was created and no positive result is attributed to this tool.
2. [INSPIRE Stampedes I record 1975636](https://inspirehep.net/literature/1975636) and the API query `refersto:recid:1975636` returned **16 citing records**, all on one page, saved in data/inspire_citations.json. All titles and abstracts were inspected; available full texts were screened for equivalent special functions and relevant passages. The closest papers were read at the locations below. This is not a claim of full reading of every citing thesis or 120-page paper.
3. [Crossref's DOI record](https://api.crossref.org/works/10.1007/JHEP07(2022)017) reports **12** incoming references. It supplies no reverse citing-title list in this record; its outgoing reference list is not a forward-citation check. data/crossref_stampedesI.json preserves the response. The difference from INSPIRE reflects index coverage, not four proven missing papers.

| INSPIRE citing paper | Examination/result |
|---|---|
| 2205.04476, Stampedes II | Full reading above; strict Bessel seed only. |
| 2307.12984, Multipoint fishnet diagrams | Full reading above; different maximal-log vertex model. |
| 2212.09732, Loom | Full reading above; extension posed, not this answer. |
| 2408.15331, Conformal four-point integrals | Section 3.4 and source context above; Toda attribution, no evaluated seed. |
| 2211.15056, Light-cone limits of large rectangular fishnets | Sections 1–2 and null-limit discussion: thermodynamic rectangular fishnets and Coulomb **gas** of matrix-model eigenvalues, not a one-body Coulomb wave for O1/O0. |
| 2401.06099, Two-loop five-point integrals | Stampedes subsection, Eqs.(74)–(79): leading-log decagon constraints and bootstrap; no corrected all-loop square seed. |
| 2512.19780, Higher-point correlators: ten-dimensional null polygons | Section 6.3, Eqs.(6.17)–(6.21), PDF pp29–30: highest-log cusp scaling and existing Toda equations. The Coulomb **branch** language is moduli-space physics, not this radial equation. |
| 2606.24018, Null limit of large-charge correlators | Conclusion contrasts the empty-polygon anomalous-dimension proposal with Stampedes cusp scaling; not the nonzero-bridge corrected seed. |
| 2510.16471, Five W-boson amplitude / near-null decagon | Abstract and full-text screening: massive amplitude/decagon duality, no Kummer/Whittaker evaluation of this ratio. |
| 2307.03076, Arctic curves of the four-vertex model | Abstract and full-text screening: Hahn log-gas/arctic curves of finite rectangular lattices, no corrected octagon seed. |
| 2303.08852, A large twist limit for any operator | Abstract and full-text screening: graph-building spectra in twisted theory, not this octagon ratio. |
| 2202.12296, Feynman polytopes and tropical geometry | Abstract/metadata: leading IR fishnet divergences, no candidate seed identified. Full text not used to assert absence. |
| 2503.15593, Four-point correlator at twelve loops | Abstract and full-text screening: integrands/Catalan combinatorics, not this light-cone resummation. |
| 2512.22996, Spectrum of two-dimensional fishnet CFT | Abstract and full-text screening: Baxter spectrum and quantization conditions, not the octagon seed. |
| 2306.00929, Large-charge 't Hooft limit | Abstract and full-text screening: HHLL correlators and a Wishart–Laguerre matrix model. Those Laguerre polynomials are not an evaluated fixed-bridge Kummer seed in this sector. |
| 10.18452/25602, Conformal Feynman Integrals and Correlation Functions in Fishnet Theory (thesis) | Metadata/abstract inspected: box analytic continuation, Basso–Dixon Ward identities, eclectic Jordan blocks. Full thesis was not read; no blanket claim of absence from it is made. |

The additional 2026 paper [Walking Sudakov: From Cusp to Octagon, 2605.16034](https://arxiv.org/abs/2605.16034), flagged by the earlier X004 review, was downloaded and its relevant Coulomb-branch/scaling discussion and text screened. It discusses form factors and amplitudes with interpolating anomalous dimensions, not a fixed one-bridge seed; it is not in the returned INSPIRE citing list. DLMF [13.7](https://dlmf.nist.gov/13.7), [33.2](https://dlmf.nist.gov/33.2) and [33.11](https://dlmf.nist.gov/33.11) establish that the Kummer/Coulomb dictionary and phase asymptotics themselves are standard mathematics.

### Consequence for the follow-up claim

The existing X004 seed still appears to answer the explicit resummation request in Stampedes I, rather than duplicating Stampedes II. Its short derivation uses already published machinery; no numerical superiority over the exact determinant is implied. This follow-up adds a clear auxiliary Coulomb interpretation and exact consequences, but no independently established new physical mechanism or prediction tested on new data. Accordingly this job's claim is **NEW: no**. Pedro's interest is for Pedro to judge; nothing was sent to him.

---

# Artur Alho — Signorini balls

Folder: [friends/alho-signorini-and-pade/o004-signorini-balls](friends/alho-signorini-and-pade/o004-signorini-balls)

## Claim

_Source: [friends/alho-signorini-and-pade/o004-signorini-balls/CLAIM.md](friends/alho-signorini-and-pade/o004-signorini-balls/CLAIM.md)_

## alho O004 — proposed full above-natural-density Signorini existence theorem

**Status: claimed for external referee and taste; no self-adjudication of novelty.**

### Published number and exact location

Alho–Calogero, [1907.09970v2 §6.4](https://arxiv.org/abs/1907.09970v2), printed p.28, leaves quasi-linear Signorini regular-ball existence outside its theorem (exponents a=b=−2,c=1). Best located target-specific public method is Alho–Calogero–Liljenberg [2104.11131v2 §3.4/Figure8](https://arxiv.org/abs/2104.11131v2), printed pp.17–18: numerical finite-radius balls at δc=2, ν=−0.5 and0.25, numerical success for tested δc>1 and −1<ν<1/2, and explicit question(a) about existence. There is no tabulated certified radius. Do not describe the baseline as zero general existence results: Beig–Schmidt already gives a generic small-body theorem.

### Proposed result

For **every** −1<ν<1/2 and **every prescribed** δc>1, prove a strongly regular static quasi-linear Signorini ball with finite radius, positive density and positive interior principal pressures. At its surface radial pressure is zero while density and tangential pressure remain positive. Thus the claimed movement is numerical evidence → an analytic existence theorem for the entire parameter range of question(a), not a faster shooting solver.

Explicit certificate: α=2+8ν, B=3/[2(α+6)], Z=δc^(2/3), ε=(6−α)/[2(7Z²+6Z)], N=9B(Z+1)². Until a first pressure zero, 1<x≤δc^(1/3), ε<y<1, P_y≥2B(6−α). A virial inequality forces R_s²≤5N/(3ε). Exact example ν=1/4,δc=8: ε=1/136,N=135/4,R_s²≤7650. Dimensionless s=r√[4πGK²/(3κ)]. The radius upper bound is not tight.

### Local code and evidence

Root: a private working copy; only some of these files are in this repository.

- `PROOF.md`: complete center, barrier, tangential pressure, continuation and finite-radius proof.
- `derive_barriers.py`: SymPy producer; `verify_signorini.py`: independent stdlib Fraction Laurent-polynomial verifier, reconstructed from literal source stored energy; `verify_instance.py`: exact rational example.
- `pod_results/exact_verification.json`: PASS26 checks; `pod_results/barrier_certificate.json`; `pod_results/rational_instance.json`; producer/verifier logs and copied source code.
- `baseline.py`, `pod_results/baseline.json`: Figure8 parameters reproduced first at two tolerances. Surface s=1.23262325218866 and1.07701968265372 for ν=−0.5 and0.25; surface δ=1.73087188579510 and1.24380776644345. Those digits are our reproduction, not numbers tabulated in the source. Baselines are uncertified floating point and do not support the theorem by themselves.
- `PRIOR_ART.md`, `SWEEP.md`, `pod_results/prior/`: primary sources, dated audit, raw public-source receipts and final recheck. `REPORT.md`: exact pod reproduction commands. `PLAN.md`, immutable `config_A1.json` and `ATTEMPT1.md`: frozen method/kill-line and outcome. `BACKUP_RECEIPT.json`, `pod_results/process_audit.json`: backup and worker-lifecycle evidence.

All scientific computation was on a rented compute pod, nice10, capped threads, under8 cores; the protected source outputs and work/input PDFs stayed on the pod. Local work was editing/transport only. No sealed data or biological work.

### Verification and controls

A separately written exact rational polynomial engine differentiates the 2020 stored energy, reconstructs both pressures, and checks26 source identities, positive-sign decompositions, local unstable eigenvector, radial balance and negative controls. It imports nothing from the SymPy producer. `PROOF.md` supplies the standard unstable-manifold and ODE continuation arguments; those analytic theorems are not formalized by the checker. This is an exact algebraic certificate plus a human-readable analytic proof, pending external review.

Controls include reproduction at printed Figure8 parameters, the natural zero-pressure state, rejection of a wrong initial pressure constant (bad run explicitly retained/labelled and rerun before construction), rejection of a universal fixed2/3 barrier near ν=1/2, exclusion of the fluid endpoint where ε=0, and the no-gravity constant-pressure infinite branch. The Beig–Schmidt small-body result is an older perturbative control; the proposed theorem prescribes all δc>1.

### Worries and scope

The referee should scrutinize local unstable-fiber existence/regularity and the compact first-exit/continuation step, beyond checking polynomial identities. No machine-formalized proof, interval trajectory, pressure transversality, fluid-endpoint, low-density-branch or stability claim is made. Priority coverage is incomplete: GitHub code search was unauthorized/rate-limited, X required login, Reddit403, and repository trees were rate-limited. A public2019 Alho talk explicitly mentions Signorini existence, although the later paper poses this question and no complete proof was located. Generic variational/perturbative results may affect priority; the external taste stage must decide. No “first” claim is made.

The requested task file was absent. RULES/current Alho board specification and common portfolio claim requirements were read; this package includes the published/result/code/verification/control/worry fields. Only O004 was edited. A1 cleared its frozen kill line; no failed-attempt close or artificial A2 is being submitted. No contact or publication occurred.

## Analysis

_Source: [friends/alho-signorini-and-pade/o004-signorini-balls/ANALYSIS.md](friends/alho-signorini-and-pade/o004-signorini-balls/ANALYSIS.md)_

## Independent mathematical audit

The verdict concerns the theorem in CLAIM.md, not an optimal numerical radius,
priority, uniqueness, or dynamical stability. `reviewed_PROOF.md` preserves the
proof reviewed. No claimant implementation was imported or executed.

### Agreement with the primary problem

I independently transcribed the energy in 2104.11131v2 (2.12), with tau=0,
and differentiated using (1.2). A separate transcription of the energy in
1907.09970v2 §6.4 agrees exactly after lambda=3nu/(1+nu),
mu=3(1-2nu)/(2(1+nu)), kappa=1. These formulas permit negative lambda;
no extra assumption nu>=0 is made. SymPy's symbolic identities are rational
identities valid throughout -1<nu<1/2.

Writing eta=x^3 and delta=x^3 y, the physical mass equation implies
s x'=x(y-1), and the force equation gives
P'=2(Q-P)/s-s x^6 y for
s=r sqrt(4 pi G K^2/(3 kappa)). The dimensional factor is correct.
The density-variable solver uses the paper's (1.3), with independently
derived a=partial_delta P and b=2(Q-P)/(eta-delta)+3 partial_eta P.
Its RHS is different from the claimant's shooting formulation.

I also inspected the actual PDF Figure 8, rendered on the pod (retained as
figure8_page18.png). Its horizontal axis is labelled Radius, with apparent
surfaces near 0.60 and 0.53, not the dimensionless s radii 1.23 and 1.08.
Setting G=K=kappa=1 gives r=s sqrt(3/(4 pi)), which visually matches those
plots. The nearby paper text does not state the numerical unit convention,
so this unit choice is an inference. It does not justify attributing the
claimant's many-digit s values to the paper. The constitutive equations,
parameters, and exact physical scaling agree; no printed numerical record
is being improved. See figure_units.json for the conversion.

The primary 2020 definition of a strongly regular ball requires positive
interior principal pressures, vanishing radial surface pressure, isotropic
center, C1 interior fields up to the center and surface, and zero center
derivatives. It permits positive one-sided surface density and tangential
pressure followed by vacuum. The claim uses exactly this meaning.

### Singular center: checked beyond the polynomial certificate

Put h=1-y, v=s^2 and time tau=log s. Direct source differentiation gives
the smooth vector field

    xdot=-xh, hdot=-L(x,h)h+v C(x,h), vdot=2v,

where L=(x P_x+2(Q-P)/(1-y))/P_y, C=x^6(1-h)/P_y,
and L(x,0)=3. The apparent quotient is polynomial after cancelling 1-y.
At xc>1, P_y=2B xc^2(10 xc^2-alpha)>0 and Cc>0.
The exact Jacobian has eigenvalues 0,-3,2 and outgoing eigenvector
(-xc Cc/10,Cc/5,1). The zero eigenvalue is tangent to the equilibrium line,
not an extra growing direction. A compact local segment of that line has
uniform transverse spectral gaps, so the strong unstable fiber at the
specified equilibrium applies. Its v>0 branch is a graph over v near zero,
because the unstable tangent has nonzero v component. Translation in tau
does not introduce an unspecified physical parameter: v=s^2 fixes it.
The fiber is smooth as an individual curve, giving
h=Cc s^2/5+O(s^4), x=xc-xc Cc s^2/10+O(s^4).
All required center derivatives therefore vanish. Also Q-P=O(s^2),
which gives a C1 Cartesian stress at the center.

As an independent check on the use of the fiber theorem, one can write
the local branch as a contraction problem in the norm sup|h(v)|/v:

    x[h](v)=xc exp(-1/2 integral_0^v h(w)/w dw),
    h(v)=v^(-3/2)/2 integral_0^v w^(1/2)
          [-(L(x[h](w),h(w))-3)h(w)+w C(x[h](w),h(w))] dw.

Here L-3=O(h) uniformly near xc; the first term in brackets is O(w^2),
and the second is w Cc+O(w^2). On |h|<=M v, for M>Cc/5,
the map preserves this ball on a sufficiently short interval and has
Lipschitz constant O(v_max). Thus the required outgoing branch is not
being inferred from a numerical start near the singular point.

### First exit and finite radius

Let z=x^2, u=y^2, m0=6-alpha>0, Z=xc^2 and H=7Z^2+6Z.
The source pressure F=P/B satisfies, on z in [1,Z], u in [0,1],

    F(z,0)=-(2z-3)^2-m0(2z-1)<=-m0,
    F(z,u)=F(z,0)+u[z(4z-alpha)+3z^2u],
    z(4z-alpha)+3z^2u <= H.

The last inequality follows by expanding its slack into
7(Z^2-z^2)+6(Z-z)+(alpha+6)z+3z^2(1-u), all nonnegative.
For epsilon=m0/(2H)<1, y<=epsilon implies F<=-m0/2.
At x=1, F=(u-1)(3u+7-alpha)<0 for y<1.
At y=1, y'=-s x^6/P_y<0. Hence neither lower face nor the upper y face
can be the first positive-pressure exit; x decreases whenever y<1.

The potentially circular step is denominator loss. It is resolved by

    y P_y/(2B)-F=3z^2u^2-F(z,0)>=m0.

As long as F>=0, this proves P_y>=2B m0/y>=2B m0.
At a hypothetical finite endpoint s*>0 the derivatives are bounded,
the solution has a limit in the compact rectangle, and the smooth vector
field extends around that limit. If P>0 there, none of the exit faces is
allowed. If P=0 there, it is already the required finite surface.
Even the corner x=y=1 is excluded by the strict negative y' there.
No continuation through negative pressure and no transversal zero are
needed. Thus the proof does not use the 2020 global theorem's failed
Signorini exponent hypothesis.

For tangential pressure put t=z(2+u)>=2, b=alpha-2t. Exact algebra gives

    F=-(t-3)^2-m0(t-1)-2zu b.

If b>=0 the RHS is strictly negative. Therefore F>=0 forces b<0,
and Q-P=2Bz(1-u)(2t-alpha)>0 for positive s before and at the surface.
This establishes strict Q>0, including at a merely tangent first zero.

Finally (P+2Q)/B=t^2+alpha t-3alpha-9<(t+3)^2,
so P+2Q<=N=9B(Z+1)^2. The force equation implies

    (s^3 P)'=s^2(P+2Q)-s^4 x^6y <= N s^2-epsilon s^4.

Regularity at zero removes the integration constant. Consequently
P<=N/3-epsilon s^2/5; the alternative of positive pressure for every s
is impossible. R_s^2<=5N/(3epsilon). At the surface x>1,
y>epsilon, y<1 and P_y>0, giving positive density and regular one-sided
fields. Zero radial traction is exactly the vacuum boundary condition;
positive tangential stress does not create a nonzero surface traction.

For nu=1/4, delta_c=8 the exact certificate has epsilon=1/136,
N=135/4 and R_s^2<=7650. This is an upper bound, not a measured radius.
The proof establishes each fixed pair in the open parameter range;
it does not assert uniform bounds at nu=-1, nu=1/2, or delta_c=1.

### Numerical attacks and limitations

All 36 rational symbolic identities passed. Four independent numerical
baseline runs agree with the claimant's computed radii to about 5e-13;
those radii are not tabulated published values. Forty-two stress cases
spanning nu=-0.9999 to 0.4999 and delta_c=1.0001 to 10000 found finite
first pressure zeros with positive sampled denominators. These are
diagnostics, not quantified or interval-certified trajectories.

The original stress table is deliberately retained with its failure flag:
at nu=-0.9999, delta_c=1.0001, five-step double-precision dense output
reported min Q=-0.0003077. This is not silently counted as a pass.
Three step-limited density integrations gave positive sampled Q; two
70-digit RK4 refinements in x,h also gave min Q about 0.0001249975
and surface radius about 0.02499678. The original apparent contradiction
was a numerical interpolation/cancellation problem near a stiff material
endpoint. The exact signs and analytic proof, rather than numerical
positivity in that table, support the verdict. See flag_replay.json.

The natural zero-pressure state, an altered constant, the false universal
y=2/3 barrier and the fluid endpoint were checked as negative controls.
With gravity switched off, both density solvers remain constant and
produce no surface. Gravity is essential to the virial contradiction.

There is no dataset or hold-out. The frozen plan explicitly declares this,
and the claimed result is an exact all-parameter statement. The published
Figure 8 examples are public calibration cases, not held-out validation.
Their reuse cannot explain away the analytic result.

I found no mathematical obstruction to the stated theorem. This is a
human review of the analytic steps supported by exact algebra, not a
machine-formalized theorem or proof of novelty. Prior generic small-body
and variational results, plus the 2019 talk mentioning Signorini existence,
are recorded separately in PRIOR_ART.md for the taste reviewer.

## Verdict

_Source: [friends/alho-signorini-and-pade/o004-signorini-balls/VERDICT.md](friends/alho-signorini-and-pade/o004-signorini-balls/VERDICT.md)_

HOLDS
Referee: gpt-6.1-sol

I found no failure in the claimed existence theorem for every -1<nu<1/2
and every prescribed delta_c>1. The energy, pressures, gravity scaling,
and meaning of strongly regular ball match the primary papers.
The singular-center construction and compact first-exit argument survive
inspection; the positive-pressure denominator bound prevents premature
breakdown, and the virial inequality forces a finite surface.

I wrote independent code from the paper's energy and density equations,
importing no claimant code: 36 exact symbolic checks passed, including
epsilon=1/136 and R_s^2<=7650 at nu=1/4, delta_c=8.
Four baseline runs reproduced R_s=1.232623252189 and 1.077019682654.
These are computed dimensionless radii, not numbers tabulated in Figure 8;
unit conversion gives approximately 0.6023 and 0.5262, consistent with its plots.
The plot's unit convention is inferred; the physical scaling is exact.
Forty-two stress cases and no-gravity controls were also run on the rented compute pod.
One coarse numerical negative-pressure flag disappeared under tighter and
70-digit replay; the original flag and all evidence are retained locally.

There is no dataset or hold-out; Figure 8 is public calibration data.
Both papers identify Artur Alho (Instituto Superior Tecnico) as an author.
Relative to [the 2021 paper, question (a)](https://arxiv.org/abs/2104.11131v2),
the addition is an all-parameter analytic proof and loose radius bound;
the existence behavior was already supported numerically there.
Beig-Schmidt's earlier small-body theorem and a 2019 Alho talk mentioning
Signorini existence remain relevant prior facts. Search coverage is incomplete;
PRIOR_ART.md records access gaps without adjudicating priority or taste.

Strongest objection: exact algebra and shooting alone cannot certify the
singular center or global continuation. I checked those analytic hypotheses
by hand and supplied an independent center integral formulation in ANALYSIS.md;
this remains a mathematical review, not a machine-formalized theorem.

NEXT BAR: turn that center integral formulation into a self-contained
local-existence lemma with explicit contraction hypotheses in the manuscript.

## Prior Art

_Source: [friends/alho-signorini-and-pade/o004-signorini-balls/PRIOR_ART.md](friends/alho-signorini-and-pade/o004-signorini-balls/PRIOR_ART.md)_

## Prior-art audit for independent referee alho_O004

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
will run only on a rented compute pod.

### Completed independent checks (2026-11-03 UTC)

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

---

# Artur Alho — certified Padé approximation, inflation

Folder: [friends/alho-signorini-and-pade/o010-inflation-pade](friends/alho-signorini-and-pade/o010-inflation-pade)

## Claim

_Source: [friends/alho-signorini-and-pade/o010-inflation-pade/CLAIM.md](friends/alho-signorini-and-pade/o010-inflation-pade/CLAIM.md)_

## alho O010 — certified extension of the monomial inflation endpoint table

Claim status: ready for independent referee. The worker does not supply a novelty or taste verdict.

Published target: Artur Alho, Juliette Hell and Claes Uggla, *Global dynamics and asymptotics for monomial scalar field potentials and perfect fluids*, arXiv:1503.06994v2 (2015), Table 1 on PDF page 28, equations (66),(68),(70),(72),(76),(79). Public source: https://arxiv.org/pdf/1503.06994 . The printed n=20 best row is [1/1]Sigma, 31% relative Hubble error at first q=0; theta is 81%, slow roll 97%.

Our result: the n=20 [4/4] Padé approximant in the inverse center-manifold variable f(z) has certified relative Hubble error **<0.000067% at the same first q=0 endpoint**. Its exact rational percent-error upper bound is

    33116497335187782100667131 / 500000000000000000000000000000.

Also added n=30,50,100 rows, with certified upper bounds <0.000074%, <0.000095%, and <0.000037%, respectively. n=2 and 3 extensions pass as well. No data fitting or empirical hold-out was used; this is a deterministic exact-equation certificate.

Baseline reproduction and stronger controls: all requested n=2,3,20 printed integer percentages are reproduced using source slow roll and the first-order tangency angle/Sigma curves, with rounding checked by interval assertions. The literal higher-order (66),(68) give stronger approximations than the printed table. At n=20 their verified errors are approximately 0.654853089624% and 3.855396638078%. The source Hubble [2/2] formula (76b), independently rebuilt from (70), is stronger still at **0.386567606987%**. It is the best explicitly tested public n=20 formula and is also beaten. We do not use 31% as though it were the strongest formula available in the paper. All six added rows beat slow roll and the tested source formulas (66),(68),(76a,b).

Method and verification: let r=-Sigma/X^n, z=r² and f=n*tildeT*(1+r²)^((n+1)/(2n))/(3r). Then q=0 is exactly z=1/2. Construct P/Q from exact formal ODE coefficients, order 24. A separate standard-library Fraction verifier checks the series and Padé identities and proves strict polynomial residual signs over the whole [0,1/2] by rational Bernstein bounds. Upper/lower differential barriers, with an explicit singular-origin comparison argument, enclose the true attractor endpoint without a numerical initial condition. The approximant's monotonicity is separately certified. The Hubble error bound is rational. Arb at 256 bits encloses public-method roots and errors; exact polynomial checks exclude poles and multiple first endpoints. Two independent numerical integrations agree but are diagnostics only.

Paths, in a private working copy (only some of these files are in this repository):

- Report: `REPORT.md`
- Proof: `PROOF.md`
- Constructor: `construct.py`
- Separate verifier: `verify.py`
- Additional public controls: `extra_controls.py`
- Source and complete raw evidence: `pod_results/`
- Exact coefficients and certificates: `pod_results/certificate.json`, `certificate_n20.json` and other per-n files
- Source-control receipts: `pod_results/public_certificate_n*.json`, `extra_controls.json`, `baseline.json`, `crosscheck.json`
- Rebuild log and audit: `pod_results/reproduction.log`, `FINAL_AUDIT.json`
- Prior art: `PRIOR_ART.md`
- Frozen attempt: `config_A1.json` and immutable `ATTEMPT1.md`

Pod copies are protected on the rented compute pod. The full small result set was pulled through the pod helper script (not published) and every file SHA-256 checked against `pod_results/MANIFEST.json` (55 files, about 3.5 MB uncompressed).

Reproduction steps, run on the pod through the pod helper script: `reproduce.sh`, then `poll_reproduction.sh`. The pod scripts aren't bundled in this repository.

The first step starts a tracked nohup run. It computes only on the pod, nice 10, one thread per worker and at most six independent workers. The completed full rerun ended `O010_REPRODUCTION_PASS`; all tracked PIDs were confirmed exited. The code and certificates were copied back to the local machine after this rerun. No GPU or additional cores were needed.

What we worry about: the referee should audit the change of variables, admissible-domain argument and comparison at the singular r=0 endpoint; these are mathematical proof obligations beyond polynomial sign arithmetic. The printed table and literal formula comparisons must remain distinguished. The bound concerns the first q=0 endpoint and finitely many n, not an entire trajectory-error guarantee or a uniform convergence theorem. Higher-order Padé approximation and variable transformations were proposed in the source, and Medina–Álvarez (2024) already treat adapted monomial Hamilton–Jacobi expansions generally. The taste step must decide whether this certified table extension is useful. GitHub code API was rate-limited and X coverage was indexed/unauthenticated; no exhaustive novelty claim is made. No contact, commit, push, PR or external message occurred.

## Verdict

_Source: [friends/alho-signorini-and-pade/o010-inflation-pade/VERDICT.md](friends/alho-signorini-and-pade/o010-inflation-pade/VERDICT.md)_

HOLDS WITH CAVEATS
Referee: gpt-6.1-sol
The n=20 <0.000067% bound is correct for the paper's relative Hubble error
at the same first q=0 endpoint on the pure-scalar attractor. All six rows pass.
The primary PDF confirms Artur Alho, Juliette Hell and Claes Uggla as authors.

I derived the transformed ODE from the paper, rebuilt the series and selected
Padé coefficients, checked all 279 accepted curves with exact rational Bernstein
bounds, and audited comparison at the singular origin. Original-variable
integrations provide a separate diagnostic. No submitted executable was imported.
Code, exact results, logs and the public source are retained here; see AUDIT.md.

The printed 31% matches a tangency curve, not the literal formula cited by
Table 1. Literal source controls are stronger and are still beaten.
I also checked the omitted source (81)+(76b): n=20 error is <0.049385789816%,
stronger than the claim's tested 0.386567606987% source control.

The decisive trivial control is source (81) with ordinary Hubble [4/4]:
its certified error is <0.000004789186%, about 14 times better than the claimed
inverse [4/4], with eight coefficients in each series. These are my control
calculations, not a previously printed numerical result. See source81_controls.json.

There is no empirical hold-out. Degrees were selected using certified endpoint
errors; coefficients match the ODE exactly. Added exponents are constructed cases,
not untouched validation. No trajectory-wide or uniform-in-n result was checked.

Relative to the paper, the contribution is an inverse-variable parametrization,
finite-n endpoint rows and exact differential-barrier certificates. Higher-degree
Padé and variable changes are already proposed there; Álvarez–Medina (2024),
arXiv:2304.05650, also covers adapted monomial expansions and Padé summation.

Strongest author objection: the paper deliberately displayed simple low-order
curves; extending its own prescription already surpasses this endpoint accuracy.
The certificate survives; it does not establish an advantage over higher-order source controls.

NEXT BAR: give a certified error-versus-degree/cost table for inverse Padé and
both source Hubble prescriptions, including equation (81) with [4/4], on all six n.

## Prior Art

_Source: [friends/alho-signorini-and-pade/o010-inflation-pade/PRIOR_ART.md](friends/alho-signorini-and-pade/o010-inflation-pade/PRIOR_ART.md)_

## Prior-art audit — independent referee, 2026-11-03

Scope: verify an existing finite-n endpoint certificate, not construct a new record.
Primary target: Alho, Hell and Uggla, arXiv:1503.06994v2, Table 1 and equations 66–79.
The claim identifies the paper's Hubble [2/2] (76b), rather than the printed 31% row,
as its strongest tested public n=20 baseline (claimed error 0.386567606987%).
These statements are unverified at this initial checkpoint.

Planned public checks: primary paper and author metadata; recent related papers;
GitHub recent code, issues and public agent-result repositories; indexed community
references. There is no identified live competitive scoreboard for this problem.
No novelty or priority determination is part of this referee assignment.
The independent baseline will be derived directly from the primary equations on a rented compute pod.

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

Independent baseline reproduction completed on the pod: printed Table 1 integers
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

---

# Artur Alho — certified Padé approximation, quintessence

Folder: [friends/alho-signorini-and-pade/o011-quintessence-pade](friends/alho-signorini-and-pade/o011-quintessence-pade)

## Claim

_Source: [friends/alho-signorini-and-pade/o011-quintessence-pade/CLAIM.md](friends/alho-signorini-and-pade/o011-quintessence-pade/CLAIM.md)_

## alho O011: certified higher-degree tracking Padé bounds

Submitted 2026-11-03T21:19:38.327526+00:00. State requested: claimed, awaiting independent referee and taste review. This worker makes no novelty or author-interest verdict.

### Published baseline and location

Best directly comparable public method located: Alho–Uggla, *New simple and accurate quintessence approximations*, arXiv:2407.14378v3, tracking [1/1]wDE from (26b),(58b,c),(81),(82). Figure 3 uses V=V0 phi^-p, p=1, Omega_phi0=.68 and 0<=z<=6. The immediately preceding discussion reports E error ~0.1% for p=1 and ~0.01% for p=.1. Source: https://arxiv.org/html/2407.14378v3 . The queue's ~0.1% Omega_m is a rough summary, not an exact table value. The 2511.02727v1 review §4 retains [1/1]. See local PRIOR_ART.md for dated audit and end refresh; community/code-search coverage has explicit gaps.

The published method was reproduced first on the pod. Floating maxima (percent, **UNVERIFIED as exact maxima**): p=1 Omega_m 0.2672536124%, E 0.1338952460%; p=.1 Omega_m 0.02072648818%, E 0.01036485532%. Source w0 and wa are reproduced to their printed digits. No claim that the authors made an error follows from the queue's rough number.

### Result and frozen problem

Same original tracker branch, both p=1 and p=1/10, Omega_phi0=17/25, dust plus scalar with no radiation, full closed interval 0<=z<=6. PLAN.md froze these before search. There is no statistical dataset or hold-out.

Analytically generated w(T) [6/6] Padé, exact rational series through order 12, no trajectory fit. Density follows R(T)=T exp(integral_0^T (w(s)/w_inf-1)/s ds), with R(T0)=17/8. This is a disclosed self-consistent normalization change from the source; it is controlled separately below.

| p | certified uniform Omega_m relative error | certified uniform E relative error |
|---|---:|---:|
| 1 | <1.326e-5 (<0.001326%) | <6.63e-6 (<0.000663%) |
| 1/10 | <1.209e-5 (<0.001209%) | <6.05e-6 (<0.000605%) |

Common safe limits: **Omega_m <0.0014%, E <0.0007%**. These are conservative supremum upper bounds, not claimed exact maxima. Smaller float errors remain unverified. Degree [2/2] also passed independently; degrees 3–5 are not certified claims.

### Verification and controls

Independently written verify_uniform.py never imports the search code. It checks all three source ODE coefficient identities and Padé matching over exact rationals. An independent Omega-variable auxiliary rational reference is verified by an inward contracting tube (radius 1e-6, 1024 intervals). Arb/Acb at 160 bits validates time-map quadrature and every continuous error cell: 3034 for p=1, 4557 for p=.1. It returned PASS for both p values, including a full pipeline rerun completed 2026-11-03T21:17:02Z. PROOF.md is the mathematical justification; this is not a proof-assistant formalization.

At exact true Omega_phi=2/5, inside the frozen redshift interval, the checker proves each control error positive and larger than the candidate's uniform upper, for both metrics. For the published [1/1], conservative relative lower bounds are p=1 Omega_m >.0026710, E >.0013382; p=.1 Omega_m >.00019708, E >.00009855. Controls also include [1/1] with the candidate's density-consistent normalization (stronger than the published formula), constant wCDM at w=-2/(p+2), and LambdaCDM. Thus each candidate has lower worst-case error; pointwise superiority at every z is not asserted. Exact control inequalities are in uniform_certificate*.json.

### Local code, data and reproduction

Directory: a private working copy; only some of these files are in this repository.

- Code: baseline.py, attempt1.py, enclosure_reference.py, verify_uniform.py, run_science.sh.
- Exact coefficients: pod_results/attempt1_p1.0.json and attempt1_p0.1.json; auxiliary reference enclosure_p*.json.
- Certificates: pod_results/uniform_certificate.json and uniform_certificate_p*.json; logs, environment.json, SCIENCE_COMPLETE, process_check.json and SHA256SUMS.json accompany them.
- Data/source receipts: pod_results/baseline.json and pod_results/sources/ (original HTML, public API replies, timestamps and hashes).
- Protocol: PLAN.md, immutable config_A1.json and ATTEMPT1.md; config SHA-256 2feaf1fea82f6b1f8ec61268a4c7828af93c90c5a8172d568fdf6abcdefa615f.
- Argument and instructions: PROOF.md, REPORT.md, PRIOR_ART.md. REPORT.md has the exact transport/launch/poll/pull commands; all scientific work runs on a rented compute pod, nice 10, thread caps 1, at most two simultaneous potential workers.

A protected copy and the active code directory stay on the pod. Small-file archive and SHA-256 verification receipt are kept locally. No large inputs or external/private data are required. No own scientific workers remain running.

### Worries for the referee and taste stage

Check the source-to-ODE transformation, singular-past tracker tube argument, interval quadrature semantics and full-domain error derivative, rather than relying only on PASS. The exact baseline suprema are only numerical reproductions; strict improvement instead follows from rigorous control point lower bounds. The bounds are loose compared with floating diagnostics. Normalization and degree both change, hence the normalization-only control. Longer rational formulas and quadrature sacrifice simplicity; no claim about other p, radiation, data fitting or cosmological inference is made. Prior-art searches cannot establish exhaustive absence, and taste/novelty are explicitly left to the designated separate stage.

## Independent Proof

_Source: [friends/alho-signorini-and-pade/o011-quintessence-pade/INDEPENDENT_PROOF.md](friends/alho-signorini-and-pade/o011-quintessence-pade/INDEPENDENT_PROOF.md)_

## What the independent interval audit establishes

The mathematical target is the positive tracker of the source's dust/scalar
system, with p=1 or 1/10 and x=Omega_phi=17/25 at N=0. All finite-start
integrations are diagnostics; none initializes the rigorous enclosure.

Eliminating H from the source equations in REPORT.md gives
x_N=3(1-q A^2)x(1-x). With t=log(x), the two remaining equations are

f(A,B,x)=(2-q A^2)(B-A)/(2(1-q A^2)(1-x)),
g(A,B,x)=B/2-(q/p)AB^2/((1-q A^2)(1-x)).

The tracker tends to (A,B,x)=(1,1,0) in the past. Its existence and unique
positive branch also follow locally from the hyperbolic saddle: x has
positive eigenvalue k=6/(p+2); the A,B block has negative trace and positive
determinant. The source identifies this branch as its tracker orbit.

`interval_ref.py` reads the auxiliary rational a(x),b(x) as proposed data.
It asserts exactly a(0)=b(0)=1, builds r=(x a'-f(a,b,x),x b'-g(a,b,x)) with
exact rational polynomial arithmetic, and tests a box of radius delta=2e-7
on each of 2048 intervals covering 0<=x<=17/25. It checks positivity of A,B,
W=1-qA^2, and A<1.1; ||r||_2 < .1*delta; and negativity of the symmetric
Jacobian plus .1 times the identity (both diagonals negative, determinant
positive). Polynomial translation about interval midpoints is evaluated
with Arb enclosures, not floating estimates.

For e=(A-a,B-b), these inequalities give d||e||/dt <= -.1||e||+||r||.
The Euclidean delta sphere is strictly inward pointing. As x->0 both the
true tracker and auxiliary curve tend to (1,1), so e tends to zero. Starting
arbitrarily early inside the sphere proves the tube for every x>0 up to
17/25. This also extends the branch across this interval: its state remains
in a compact regular region and W stays positive.

For y=log((17/25)/x), integrate the auxiliary time map directly in x:
N_c(x)=integral_(17/25)^x [3(1-q a(s)^2)s(1-s)]^-1 ds.
This callback is rational and meromorphic. With Wmin=1-q*(1.1)^2,
D=q*delta*(2.2+delta), the true time lies within
y*D/[3*Wmin^2*(1-17/25)] of N_c(x).

The candidate's exact Padé P/Q is independently reproduced by referee.py.
All Q coefficients are positive and all P coefficients negative. Thus no
positive-axis pole exists, w/w_inf>0, and its R(T) is strictly increasing.
Validated bisection encloses the unique root R(T0)=17/8 in (1,3).
The rational removable singularity in (w/w_inf-1)/T is cancelled exactly.

Both time and log R quadratures use Acb at 192 bits. Integrators receive
exact dyadic endpoint midpoints. For an uncertain endpoint, an additional
real interval integrand bound times its radius encloses the displacement.
Callbacks contain no branch-dependent log, sqrt or absolute-value operation.
The callbacks are meromorphic; any interval containing a pole returns a
nonfinite value. Nonfinite or insufficiently narrow quadratures abort.

Each y cell has width 1/2048. A rigorous center value and a whole-cell
bound on |dN/dy| enclose the true time over the cell. Continuity gives
dlogR/dN=-3w, which encloses candidate density over the entire cell.
For L=log(Omega_m,candidate(N_true(y))/(1-x(y))), exact differentiation gives
L_y=(-w_candidate*Omega_phi,candidate/W_true-x)/(1-x).
The audit bounds |L| by its interval center magnitude plus half the cell
width times a whole-cell |L_y| bound. It continues until the entire last
time enclosure is earlier than -log(7). Monotonicity and adjoining cells
then cover every z in the closed target interval [0,6].

If the resulting uniform log bound is M, exp(M)-1 bounds the relative
Omega_m error and exp(M/2)-1 bounds the E error. The latter follows exactly
from dust conservation E^2=(8/25)exp(-3N)/Omega_m, with common present H0.
Arb inequalities compare these bounds directly with the claim's p-specific
limits. The audit also encloses published [1/1], normalization-only [1/1],
wCDM and LambdaCDM errors at the exact true x=2/5, proves that point lies
inside the redshift interval, and compares the control lower bounds with
the degree-6 uniform upper bounds.

This is an independently programmed rational/ball certificate with a written
ODE argument, not a proof-assistant formalization. It assumes the stated
dust/scalar equations. Exact arithmetic and the validated integration backend
are provided by python-flint 0.9.0; versions and reproduction files are retained.

## Verdict

_Source: [friends/alho-signorini-and-pade/o011-quintessence-pade/VERDICT.md](friends/alho-signorini-and-pade/o011-quintessence-pade/VERDICT.md)_

HOLDS
Referee: gpt-6.1-sol

The stated uniform error improvement survives an independent reconstruction for both p=1 and p=0.1, Omega_phi0=0.68, dust plus scalar, and the entire closed interval 0<=z<=6. Omega_m and E=H/H0 are the same quantities used in the paper.

I wrote and ran independent rational-series, Padé, Friedmann/Klein–Gordon and Arb verification code on a rented compute pod; no claimant search or verifier code was imported. Exact order-12 coefficients matched. The 192-bit continuous audit passed 6067/9112 error cells and two 2048-cell tracker tubes.

My certified relative upper bounds (fractions, not percentages) are: p=1, Omega_m<3.294e-6 and E<1.647e-6; p=0.1, Omega_m<3.010e-6 and E<1.505e-6. These imply every submitted limit. The much smaller floating maxima remain numerical diagnostics.

The [primary paper](https://arxiv.org/html/2407.14378v3) is by Artur Alho and Claes Uggla. I reproduced its intended baseline: p=1 errors 0.267254%/0.133895% for Omega_m/E; p=0.1, 0.0207265%/0.0103649%. Its “~0.1%” is approximate wording. Equation (58a)'s inconsistent prefactor is resolved by (26b), (58b,c) and its printed w0; the claim uses that consistent formula.

No statistical hold-out exists or is claimed. The coefficients follow from the ODE recurrence; normalization uses the fixed present density, without fitting a numerical trajectory.

The normalization change alone does not explain the gain. Published [1/1], consistently normalized [1/1], wCDM and LambdaCDM all have rigorously larger errors at an interior witness than the candidate's uniform bound. Additional numerical controls using the paper's footnote-6 density Padés, directly and for normalization, also remain worse.

Relative to the paper, this submission supplies order-12 coefficients, degree-six w Padés, self-consistent normalization and uniform certification for these examples, with longer formulas and quadrature. Prior result seen: footnote 6 already prints [1/2] and [2/1] density Padés; the [later review](https://arxiv.org/html/2511.02727v1) retains [1/1]. No novelty or priority judgment is made.

Evidence: REPORT.md, INDEPENDENT_PROOF.md, independent code and pod_results/interval_*.json. All 59 manifest files were copied back and hash checked. No referee workers remain; the cleaned pod directory is under 0.3 MB.

Strongest author objection: two fixed p values do not establish a uniform guarantee as the inverse-power exponent varies.

NEXT BAR: Certify the same claimed error limits uniformly for every p in [0.1,1], keeping Omega_phi0=0.68 and 0<=z<=6.

## Prior Art

_Source: [friends/alho-signorini-and-pade/o011-quintessence-pade/PRIOR_ART.md](friends/alho-signorini-and-pade/o011-quintessence-pade/PRIOR_ART.md)_

## Referee source audit (2026-11-03)

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

### Independent follow-up

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

---

# Tiago Fonseca (with Paul Zinn-Justin) — a fused-link obstruction

Folder: [friends/fonseca-dinis-qkz-fused-link](friends/fonseca-dinis-qkz-fused-link)

## Claim

_Source: [friends/fonseca-dinis-qkz-fused-link/CLAIM.md](friends/fonseca-dinis-qkz-fused-link/CLAIM.md)_

## dinis W011 — exact ordinary-invariant obstruction, pending referee and taste

Submitted 2026-11-03 America/New_York (2026-11-04 UTC). Scope is arXiv:1212.4672 Appendix C.2, with the algebra form stated explicitly. This worker makes no novelty or author-interest judgment.

### Published baseline and source

Tiago Fonseca and Paul Zinn-Justin, Higher spin polynomial solutions of quantum Knizhnik–Zamolodchikov equation, arXiv:1212.4672v2 (17 October 2013), Comm. Math. Phys. 328 (2014), 1079–1115, DOI 10.1007/s00220-014-1963-7. Primary text: https://arxiv.org/html/1212.4672 . Section 2.1 gives the horizontal generators and (2.1) their local matrices. Section 4.3.2 and Appendix C.2 prove injectivity of the fused-link map whenever [2]...[ell] are nonzero, including q=-exp(-i*pi/(ell+2)), and generic-q surjectivity. C.2 conjectures special-q isomorphism.

There is no printed numerical special-q dimension frontier to improve. At ell=3,L=6 the published generic characterization and full image rank specialize to the link count 34. We reproduce dimension 34 at generic q=2 exactly. The best public method is the source's triangular projection proof; checking rank 34 alone would only reproduce its theorem. PRIOR_ART.md documents later literature and final repository/source checks.

### Our number and statement

For ell=3,L=6 and q=-exp(-i*pi/5), ordinary invariants mean E v=F v=0 and K v=v in the tensor representation of (2.1). The independently certified numbers are:

| Quantity | Exact dimension |
|---|---:|
| Fused-link image | 34 |
| Ordinary invariants with strict integer weight zero | 35 |
| Ordinary invariants over all K=1 sectors | 37 |
| E,F,E^(5) common kernel within strict weight zero | 34 |
| Generic q=2 invariant control at the same ell,L | 34 |

An explicit strict-weight-zero invariant w_9 satisfies E^(5)w_9=2w_14 !=0; all link columns are annihilated by E^(5). Thus it lies outside the image. PROOF.md gives an explicit symbolic obstruction for every odd ell>=3 at L=ell+3: putting p=ell+2, m=(ell+1)/2 and s=ell*L/2=mp-1, its vector w_s is ordinary invariant and E^(p)w_s=m w_(s+p)!=0, while E^(p) annihilates the image. This family is a written proof for referee audit; the finite ell=3 instance has the separate exact machine certificate. An ell=1,L=10 cross-check gives image/strict-zero/full dimensions 42/43/45.

**Algebra-form caveat:** this is an obstruction for the ordinary Chevalley-generated algebra. It is not a counterexample if the conjectured codomain requires Lusztig divided-power invariance. Indeed the witness explicitly fails that requirement. The small-versus-divided-power distinction is established prior art (2008.06038, 1910.12427). The referee must audit which interpretation is warranted; the taste step must decide whether the explicit values/family add anything author-relevant. No author error is asserted.

### Code and data

Directory: a private working copy; only some of these files are in this repository.

- REPORT.md: reproduction instructions, result/controls/limitations.
- PROOF.md: algebra convention, explicit family and finite lower/upper argument.
- PRIOR_ART.md: baseline and final literature/repository recheck, including coverage limits.
- config_A1.json and ATTEMPT1.md: frozen attempt and final immutable outcome.
- a1_rank.py, a1_witness.py: search and exact witness construction.
- verify_a1.py: independent exact verifier; imports no search/construction module.
- verify_projection.py, baseline_target.py: actual Jones–Wenzl recursion and same-size rational generic control.
- REPRODUCE.sh: pod-only nohup entrypoint. Run through the pod helper script (not published) as detailed in REPORT.md; poll the protected reproduce.log.
- pod_backup/a1_witness_ell3_L6.json: exact explicit coefficients and tensor basis states.
- pod_backup/verified_patterns_ell3_L6.json: complete 34-pattern list.
- pod_backup/verification_ell3_L6.json, verification_ell1_L10.json, verification_projection.json, baseline_target_ell3_L6.json: PASS receipts.
- pod_backup/exact_pipeline.log and baseline_target.log: completed verification logs.
- W011_results.tar.gz, BACKUP_RECEIPT.json and pod_backup/SHA256_MANIFEST.json: checksummed backup.

The protected originals are on the pod. Small artifacts are well below 50 MB; no bulky datasets are needed.

### Verification

The independent verifier implements Z[q]/Phi_5(q) arithmetic directly, builds the local tensor E/F matrices separately, enumerates noncrossing singlet orientations and reconstructs fused columns. It checks exact E/F invariance of all columns and witnesses, and direct regular divided-power action, without dividing by vanishing [5]. It independently checks all 34 columns are killed by E^(5), while E^(5)w_9=2w_14 is nonzero. Actual Jones–Wenzl recursion is separately checked against the compact projection normalization over Q and Q(zeta_5).

Modular column rank 34, and rank 35 after adding w_9, is checked at prime 1000081 with embeddings q=188136 and q=287744. The prime is separately checked by trial division. Independent E/F row assembly gives ranks 119,545,119 in the three K=1 sectors of sizes 120,580,120. Modular reduction supplies upper bounds 1,35,1 on characteristic-zero kernel dimensions; exact columns plus three witnesses attain them. This is an exact lower/upper certificate, not an assumption that modular nullity equals characteristic-zero nullity. The generic baseline uses exact rational annihilation plus matching modular lower/upper ranks. Main verification ends ALL PASS. Earlier launch/API errors remain in historical logs and are explicitly identified in REPORT.md.

### Controls and worries

Controls: source injectivity/full column rank; generic-q isomorphism reproduced before the root search on small cases and at the claimed size afterward; strict integer weight zero; direct divided-power separation; actual projector recursion; independent ell=1 cross-check. No predictive hold-out or sealed data is involved. All computation ran on a rented compute pod, nice 10, at most 8 processes and thread counts 1. Final process receipt confirms no worker remains.

Worries: the intended algebra form may make this an illustration of known representation theory rather than movement of the authors' intended conjecture. Later papers already establish the general categorical distinction. No matching finite table was found, which does not establish novelty; GitHub sorted-update API and unauthenticated code search/X retrieval had access limits, documented in PRIOR_ART.md. Other exploratory panel nullities are UNVERIFIED over characteristic zero and excluded from this claim. Neither VERDICT.md nor TASTE.md is supplied by this worker. Nothing was contacted or published externally.

## Proof Audit

_Source: [friends/fonseca-dinis-qkz-fused-link/PROOF_AUDIT.md](friends/fonseca-dinis-qkz-fused-link/PROOF_AUDIT.md)_

## Independent audit of the stated family

Write [n]=(q^n-q^-n)/(q-q^-1). I used the local matrices in source (2.1)
and coproduct E=E⊗1+K⊗E, F=F⊗K^-1+1⊗F. This gives the source's
two-site singlet v10-q v01. Tensor reversal relates the opposite convention.

For a source basis state b and increments a with sum a=r and
0<=a_i<=ell-b_i, expansion of the q-commuting coproduct summands gives

E^(r) v_b = sum_a q^(sum_{i<j} a_i a_j +
                           sum_i a_i sum_{j<i}(2b_j-ell))
                 product_i [ell-b_i choose a_i] v_(b+a).

This is regular at the specified root because all local denominators have
index <=ell<p=ell+2. The referee code implements this tensor expansion,
with its normalization also checked against repeated ordinary action for
the nonvanishing local factorials. It does not evaluate E^p/[p]! at the root.

Applying the expansion to the lowest tensor reproduces exactly the claimed
w_t coefficients. Generic quantum-binomial identities then give
E w_t=[t+1]w_(t+1), F w_t=[N-t+1]w_(t-1), K w_t=q^(2t-N)w_t.
These identities specialize because their individual coefficients are regular.

For odd ell>=3, p=ell+2 is odd, q=-exp(-i*pi/p) has exact order p,
m=(ell+1)/2>=2, N=ell(ell+3), and s=N/2=mp-1.
Both raising/lowering coefficients at s are [mp]=0; the integer weight is zero.
All coefficients defining w_s are nonzero: their quantum integers have indices
strictly below p. Thus this is a nonzero ordinary invariant for composite p too.

The generic divided-power product identity gives
E^(p)w_s=[s+p choose p]w_(s+p). Separate the unique vanishing numerator
factor [mp] and denominator [p]. Their ratio tends to m by differentiation.
Each remaining ratio [mp+j]/[j], 1<=j<p, tends to 1. Therefore the scalar
is m. Also s+p<=N and w_(s+p) is nonzero.

Every generically invariant fused column is killed by E^(p) generically.
Both that operator and the Jones–Wenzl projected columns are regular at this
root; consequently their product remains zero after specialization. This
separates w_s from the entire image. The proof does not assert a failure of
divided-power invariance, or of flat continuation of the generic invariant space.

Finite independent certification is in evidence/referee_results.json. Exact
annihilation supplies lower bounds; two finite-field ranks give matching upper
bounds over the number field. No modular nullity is assumed equal to a
characteristic-zero nullity without those exact lower bounds.

## Verdict

_Source: [friends/fonseca-dinis-qkz-fused-link/VERDICT.md](friends/fonseca-dinis-qkz-fused-link/VERDICT.md)_

HOLDS WITH CAVEATS
Referee: gpt-6.1-sol

The explicitly ordinary-generator claim survives independent reconstruction.
At ell=3,L=6 I obtain image dimension 34, strict-weight-zero ordinary
invariants 35, and all K=1 ordinary invariants 37, exactly as claimed.
E^(5)w_9=2w_14 is nonzero; every reconstructed link column is killed by E^(5).
The stated odd-ell>=3 obstruction proof also checks out (PROOF_AUDIT.md).

The paper prints no special-root numerical frontier. Its generic multiplicity
and already-proved injectivity give 34. Its definition of U1 using E,F,K
supports this literal ordinary-invariant reading of Appendix C.2.
Source: [Fonseca–Zinn-Justin](https://arxiv.org/html/1212.4672#A3.SS2).

I independently coded (2.1), tensor coproducts, the actual Jones–Wenzl recursion,
noncrossing projected singlets and regular divided powers; no claimant code
was imported. Exact witnesses plus matching ranks at primes 101 and 151
certify the dimensions. Generic q=2 gives 34; ell=1,L=10 gives 42/43/45.
All evidence is copied back in evidence/; REPORT.md gives reproduction commands.
No predictive hold-out applies to this deterministic algebra calculation.

Strongest author objection: the intended codomain uses Lusztig divided powers
or continuation of generic singlets. The sceptic's control confirms this matters:
requiring divided-power invariance restores strict-zero dimension 34 exactly.
Therefore this does not refute that interpretation of the conjecture.

Relative to the paper: explicit ordinary-kernel dimensions and an obstruction
family, rather than an improved image rank. The general small/divided-power
distinction and need for extra morphisms are prior results in
[Blanchet–De Renzi–Murakami](https://arxiv.org/html/1910.12427v3).
Identity checks pass: the source's Tiago Fonseca matches the Dinis da Fonseca
name and CRM/LAPTh affiliation in [his companion paper](https://arxiv.org/html/1210.4527).

NEXT BAR: Prove an all-L image characterization with the root-of-unity algebra
and specialization convention explicitly fixed, resolving the codomain ambiguity.

## Prior Art

_Source: [friends/fonseca-dinis-qkz-fused-link/PRIOR_ART.md](friends/fonseca-dinis-qkz-fused-link/PRIOR_ART.md)_

## Independent referee prior-art record

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

### Completed independent checks

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

---

# Aires Ferreira — KITE

Folder: [friends/ferreira-kite](friends/ferreira-kite)

The repro, evidence, dependency and upstream folders named below aren't bundled in this repository.

## Verdicts

_Source: [friends/ferreira-kite/VERDICTS.md](friends/ferreira-kite/VERDICTS.md)_

## Independent KITE referee verdicts

Refereed locally on 2026-11-06 against fresh clone commit `a1e1f7ce6e48505ce2655315c2565446315a67e0`. Only the hunter's claim document and report were read; none of their scripts, patches, fixtures or output files was run, imported or copied. The suspected list was excluded.

| ID | Verdict | My repro path | Effect on users' results |
|---|---|---|---|
| KITE-CFG-001 | **CONFIRMED** | repro/config/run.py, result | Nonzero energy shift invents interorbital couplings, even for diagonal onsite matrices, changing the exported Hamiltonian and spectrum. Exporter-only execution; pybinding limitation below. |
| KITE-CFG-002 | **INTENDED** | repro/config/run.py, default, explicit complex | Imaginary onsite entries are lost in documented real-only mode; setting `is_complex=True` preserves them. Incomplete automatic detection is a safeguard inconsistency, not a demonstrated violation of the documented mode contract. |
| KITE-TOOLS-001 | **CONFIRMED** | repro/optical/run.py, scalar reference, results | File temperature is printed but ignored in both optical calculation branches, so finite-temperature spectra use the default cold occupations. |
| KITE-TOOLS-002 | **CONFIRMED** | repro/ldos/run.py, results | The documented Green LDOS kernel returns spectral density too large by a factor of pi. |
| KITE-TOOLS-003 | **CONFIRMED** | repro/ldos/run.py, results | A non-divisible moment count silently loses its remainder on multiple threads, making Jackson LDOS depend on decomposition. Divisible counts are unaffected in the control. |

### Ranked findings

1. **TOOLS-001: ignored optical temperature.** Affects the ordinary file-driven workflow and both calculation branches, while displaying the requested temperature. Explicit CLI `-T` avoids it. The numerical effect is substantial in the independent molecule below.
2. **CFG-001: onsite energy rescaling changes the physical model.** Affects valid multi-orbital matrices whenever the energy shift is nonzero; even zero off-diagonal entries become couplings. Manual asymmetric bounds are explicitly documented. Zero shift and single-orbital inputs passed the controls.
3. **TOOLS-002: absolute Green LDOS normalization.** Every tested energy on the supported `green` path has the same factor-of-pi error. This changes local spectral weight and state counts. The default Jackson path does not execute the faulty expression.
4. **TOOLS-003: lost threaded moments.** A supported `-M` override can change results solely through the decomposition. Lower priority because it requires a non-divisible count; usual divisible counts avoid this failure.

CFG-002 is excluded from this correctness-bug ranking. Nothing has been sent to the author or anyone else. These are proposed communication priorities based on demonstrated numerical effects and documented paths; Ricardo reads first and the friend decides whether they care.

### Executed inputs and independent answers

#### CFG-001 — diagonal onsite matrix acquires coupling

The cited kite.py:1261 subtracts a scalar from the entire onsite matrix. For my input `H = diag(1,3)` eV and bounds `[-1,5]`, the scale is 3 and shift is 2. The correct scaled matrix is `diag(-1/3,1/3)`; its off-diagonal entries stay zero.

Decoding the actual exported HDF5 hopping datasets and undoing rescaling instead gives physical `[[1,-2],[-2,3]]` eV. Its eigenvalues are `2 ± sqrt(5)` = `[-0.2360679775,4.2360679775]` eV; the input's exact eigenvalues are `[1,3]`. This demonstrates corruption even without an original interorbital coupling. The same diagonal input with bounds `[-5,5]` and a shifted scalar onsite input both export correctly.

User reachability: settings.md, Spectrum Range encourages manual energy bounds; tb_model.md, Adding lattice sites routes lattice input through pybinding. Its independently downloaded 0.9.5 matrix overload accepts onsite matrices and stores their Hermitian form; Python binding exposes `energy` as the onsite matrix. Both my diagonal matrix and the CFG-002 Hermitian matrix satisfy that representation.

#### CFG-002 — observed loss, but documented real mode

The claimed detection loop kite.py:1187 inspects hopping families only. My Hermitian onsite matrix is `[[0.4,0.6i],[-0.6i,-0.4]]` eV with symmetric bounds `[-2,2]`, avoiding the shift bug. Default real mode exports `diag(0.4,-0.4)` and eigenvalues `[-0.4,0.4]`, whereas the supplied matrix has eigenvalues `±sqrt(0.52)` = `±0.7211102551`. With `is_complex=True`, the same unmodified exporter preserves the entire matrix and its eigenvalues.

However, settings.md:85–88 reserves complex storage for `is_complex=True` and says `is_complex=False` should be used for real symmetric Hamiltonians. The Configuration docstring also describes the flag as reflecting the Hamiltonian's type. Thus the triggering combination supplies a complex Hamiltonian to documented real mode. The automatic promotion for complex intersite hoppings is an inconsistent convenience; I found no documented promise of comprehensive automatic detection. I would describe this as possible input checking/hardening, not send it as a correctness bug in supported complex-mode use. No hardening change was made.

#### TOOLS-001 — temperature supplied by file never updates beta

The temperature read at line 180 leaves beta at its default, while the CLI override updates it. Both `calculate` and `calculateBlocks` consume beta.

My input is an array of disconnected two-site molecules with hopping 0.35 eV and sites separated by 0.8 nm, unit cell area 1 nm², energy scale 1 and shift 0. I supply exact normalized trace moments, 128 moments, 2049 Simpson points, Fermi energy 0 and broadening 0.12 eV. In the independent scalar reference, the two eigenvalues are ±0.35; Jackson spectral projectors and exact scalar resolvents enter the eigenbasis Kubo trace. That reference never uses KITE or the supplied Gamma matrix. Its finite Jackson expansion and integration grid match the requested numerical definition; the Green resolvent is evaluated exactly.

At omega = 0.7 eV, requested `kBT=0.3` eV:

| Calculation | Conductivity, e²/h |
|---|---:|
| Independent hot reference | `3.00226715596 + 0.253847984606i` |
| Unpatched, temperature from file | `5.73209 + 0.532202i` |
| Independent cold reference, kBT=0.001 | `5.73209055841 + 0.532202465137i` |
| Unpatched, explicit CLI `-T 0.3` | `3.00227 + 0.253848i` |

The hot-file and cold-file outputs are identical at all three frequencies, and both regular and block branches show the same result. Explicit CLI temperature agrees with the independent hot reference at saved-text precision. Both hot runs print `Temperature: 0.3`.

User reachability: default usage says the file alone suffices; calculation.md:66–67 defines the temperature of the Fermi distribution; FAQ specifies energy units. This is not an intended default override, and is not a Kelvin-conversion claim.

The first NumPy reference contraction emitted BLAS floating-point warnings despite finite numbers. I replaced that contraction with ordinary scalar math, recomputed it, and reran the optical fixture without warnings. The initial log is retained as console-initial.txt.

#### TOOLS-002 — Green LDOS normalization

The cited ldos.cpp:277 accumulates minus the imaginary Green coefficient without division by pi. My exact input is a single local level at 0.25 eV, 256 moments, one thread and broadening eta = 0.15 eV. The independently correct density is the normalized Lorentzian `eta / (pi * ((E-0.25)^2 + eta^2))`.

| Energy, eV | Unpatched LDOS, 1/eV | Correct LDOS, 1/eV |
|---:|---:|---:|
| -0.25 | 0.550459 | 0.175216451110 |
| 0.25 | 6.66667 | 2.122065907892 |
| 0.50 | 1.76471 | 0.561723328560 |

The discrepancy is pi to saved-text precision, and not a finite-expansion effect. One thread isolates this claim from the excluded suspected Green indexing issue. User reachability: both tools help and API documentation explicitly offer `--LDOS -K green eta`; LDOS denotes a spectral density, and the default Jackson expression already includes its pi normalization.

#### TOOLS-003 — a supported override loses a nonzero last moment

At ldos.cpp:245, each thread takes `floor(M/P)` terms with no remainder assignment. My stored input contains 32 exact moments for a zero-energy local level, `mu_n = cos(n*pi/2)`. Both lattice sizes and decomposition obey the documented TILE=8 constraint. I request seven moments with the documented `--LDOS -M 7` override.

At E=0, the complete finite Jackson sum is `1.007200458900` 1/eV. The unpatched result is `1.0072` on one thread and `0.983893` on two threads. The missing n=6 term is nonzero. A six-moment control produces `0.872882` on both thread counts. This tests the post-processor override, without asking the core to generate an odd number of moments.

User reachability: tools API and help expose the override without a thread-divisibility restriction; the code checks that it does not exceed stored moments, but imposes no divisibility rule. Decomposition documentation recommends multiple partitions. Reusing moments with different post-processing parameters is an explicit advertised workflow.

### Upstream status

Read-only `gh api` requests fetched all 36 issue/PR entries, 28 PR records, 19 issue comments, one review comment, releases, branch heads and commit history. Snapshots and extracted text are in evidence/. There were no open issues or PRs at fetch time. Reviewed numerical/build PR diffs include #4, #5, #6, #9, and recent #35–37. None of the four surviving failure mechanisms appeared in the reviewed discussions or diffs. Issue #17 concerns server-dependent DOS/DC NaNs and supplies no matching optical/LDOS/exporter diagnosis; it is not evidence that these specific bugs are known.

Latest release is [1.1](https://github.com/quantum-kite/kite/releases/tag/1.1), published 2025-04-29, commit `078c23511bf63b6478af39f6a44d6e03828ec09a`. Master still points to the tested pin. `kite-develop` is `304d127c7f3e6d6fed530fd14dd2e90ebc9f5250`; `test-h` is `2b55aa088c09997ea7d5d956c0e1132a73f43218`. The affected three source files are byte-identical in all four versions, as recorded in source-versions.json; all core and tools source also has no diff from release 1.1 to the pin. `gh-pages` contains the generated documentation site. No current fix was found. This is a public-history check, not a claim about private reports or forks.

### Build limits and replay

KITEx failed two honest attempts: missing dependencies first, then Apple libc++ lacking `std::cyl_bessel_j` at `SimulationGaussianWavePacket.cpp:154`. The core was not modified or retried after that. KITE-tools built from the unchanged pin using locally built HDF5 1.14.6, Eigen 3.4.0, and the installed Homebrew libomp; an explicit libomp link was needed. Build/configuration logs, dependency hashes and Python versions are under evidence/.

Pybinding 0.9.5 installation failed, finally on its bundled Eigen's `Transpositions.h:387`. Therefore CFG-001/002 execute the actual unmodified `kite.config_system` with a minimal lattice data interface verified against pybinding's source and an empty import-only `pybinding` placeholder. No pybinding function runs, no bounds are mocked, and explicit energy bounds avoid pybinding's automatic scaling entirely. These are exporter verdicts, not end-to-end pybinding/KITEx verdicts. The three TOOLS claims use the real compiled executable and independent exact supplied moments. No core recursion or stochastic-moment calculation was tested; none of the five allegations was left entirely unexercised.

From this working directory, with the retained local venv and binary:

```sh
env OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 OMP_NUM_THREADS=2 nice -n 10 .venv/bin/python repro/config/run.py --interface-only
env OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 OMP_NUM_THREADS=2 nice -n 10 .venv/bin/python repro/ldos/run.py build/local/KITE-tools
env OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 OMP_NUM_THREADS=2 nice -n 10 .venv/bin/python repro/optical/run.py build/local/KITE-tools
```

No hunter fix was applied or evaluated. No issues, PRs, comments, forks, messages or contacts were made. **NEW: no.** This is independent referee adjudication of existing software claims; no novel scientific result or predictive score is claimed. Predictive baselines and SBS do not apply.

## Bugs: pre-referee report; final dispositions above

_Source: [friends/ferreira-kite/BUGS.md](friends/ferreira-kite/BUGS.md)_

## KITE correctness bugs (four confirmed; CFG-002 excluded as intended behaviour)

Pinned upstream: **a1e1f7ce6e48505ce2655315c2565446315a67e0**, default `master`, shallow clone in `upstream/kite/`.
Latest release: **1.1**, published 2025-04-29, tag commit `078c23511bf63b6478af39f6a44d6e03828ec09a` (`sources/releases.json`, `sources/tags.json`).
Aires Ferreira is named under **Project founders** in the pinned README, and is an author of [João et al., KITE, R. Soc. Open Sci. 7, 191809 (2020)](https://arxiv.org/abs/1910.05194), whose PDF is retained in `sources/kite-paper.pdf`.

These five reports were not found in the reviewed public issue/PR history. This is a local software repair result, **not a novel scientific result: NEW: no**. No paper number was improved, stated scientific open problem settled, or new-data prediction tested. No predictive model or predictive score is reported; trivial/simple/model baselines and SBS are inapplicable.

Each section links a runnable repro with pinned output, independently computed correct output, repaired output, a minimal root-relative git patch, and a normal-input regression comparison. Independent numerical checks are separately written Python/NumPy implementations, not a second person or an external referee. Nothing was sent or published.

### KITE-CFG-001 — energy shift changes off-diagonal onsite terms

- **Location:** `kite.py:1261`.
- **Wrong:** subtracting the scalar energy shift broadcasts it to every element of a multi-orbital onsite matrix. Rescaling requires subtraction of shift × identity.
- **Before → correct/after:** onsite H=`[[1,.25],[.25,2]]` eV, bounds [-1,5]; exported physical eigenvalues `[-0.3200274723,3.3200274723]` → `[0.9409830056,2.0590169944]` eV.
- **Effect:** nonzero shifts silently change hybridization, splittings and the resulting spectral/transport problem; automatic asymmetric bounds can also produce nonzero shifts, although that route was not exercised.
- **Evidence:** repro and reasoning, before, after, patch (`repro/KITE-CFG-001/`).
- **Independent check/control:** decode the actual HDF5 hopping representation, invert rescaling and diagonalize in plain NumPy. Zero-shift and one-orbital controls retain identical dataset values.
- **Confidence:** high for the exporter with explicit bounds. Pybinding itself was not installed; its import is stubbed, no API calls are made, and the fixture uses upstream `lattice.py` with the same matrix representation as pybinding's retained source.
- **Reason:** [KITE Eq. (2.14)](https://arxiv.org/abs/1910.05194); [Weiße et al. (2006), Eq. (24)](https://arxiv.org/abs/cond-mat/0504627).

### KITE-CFG-002 — imaginary onsite couplings disappear with default real configuration

- **Location:** `kite.py:1187–1192`, with loss during real hopping export at lines 1309 and 1435.
- **Wrong:** automatic complex detection checks intersite hoppings but ignores onsite matrices. Default `is_complex=False` silently drops imaginary onsite entries.
- **Before → correct/after:** Hermitian H=`[[0,-i],[i,0]]` eV yields eigenvalues `[0,0]` → `[-1,1]` eV; Tr(H²) `0` → `2` eV². `IS_COMPLEX` becomes 1.
- **Effect:** onsite spin/orbital terms can be removed, changing the Hamiltonian rather than its numerical precision. Explicit `is_complex=True` avoids this bug.
- **Evidence:** repro and reasoning, before, after, patch (`repro/KITE-CFG-002/`).
- **Independent check/control:** independent HDF5 decoding, NumPy eigvalsh and the identity sigma_y²=I. Explicit-complex and ordinary real controls have identical HDF5 dataset values before/after.
- **Confidence:** high for the explicit-bounds exporter; same import-only pybinding limitation as CFG-001.
- **Reason:** Hermitian-matrix spectral decomposition; [KITE Sec. 2(a)](https://arxiv.org/abs/1910.05194).

### KITE-TOOLS-001 — optical conductivity uses stale inverse temperature

- **Location:** `tools/Src/OptCond_1order/conductivity_optical.cpp:180`; beta consumed at lines 391 and 623.
- **Wrong:** reading the HDF5 temperature does not refresh beta=1/temperature. Without CLI `-T`, both optical calculation branches use the default k_B*T=0.001 eV, regardless of the stored value.
- **Before → correct/after:** two-site molecule at omega=0.6 eV and requested k_B*T=0.2 eV: sigma `4.78760 + 0.782720i` → `3.02977 + 0.480812i` in e²/h. Independent result `3.0297736361 + 0.4808121743i`.
- **Effect:** temperature dependence and thermal occupation of optical transitions are wrong while the program prints the requested temperature. No Kelvin-conversion bug is claimed: temperature is k_B*T in energy units, per the pinned FAQ.
- **Evidence:** repro and parameters, pinned spectrum, repaired spectrum, independent numbers, patch (`repro/KITE-TOOLS-001/`).
- **Independent check/control:** exact NumPy eigensystem, finite Jackson spectral projectors and direct scalar resolvents in the Kubo trace; matched moment count, grid and broadening. Default-temperature control is byte-identical.
- **Confidence:** high. Real compiled post-processor, no mocks. The independent calculation agrees at all three frequencies within the precision of saved text.
- **Reason:** Fermi occupation definition and [KITE Eq. (2.23)](https://arxiv.org/abs/1910.05194).

### KITE-TOOLS-002 — Green-function LDOS omits 1/pi

- **Location:** `tools/Src/Spectral/ldos.cpp:277`.
- **Wrong:** Green LDOS uses −Im(G), rather than −Im(G)/pi; total DOS already contains the factor.
- **Before → correct/after:** zero-energy isolated level, eta=0.2 eV: rho(0) `5` → `1.59155` 1/eV; exact `1.591549430918953`. The other tested energies show the same factor of pi.
- **Effect:** absolute local spectral weight and integrated state counts are too large by pi for the `green` kernel. This is distinct from Lorentz damping coefficients.
- **Evidence:** repro and definition, before, after, patch (`repro/KITE-TOOLS-002/`).
- **Independent check/control:** NumPy spectral decomposition and the defining resolvent/Lorentzian. One thread, 128 moments; truncation is negligible at this broadening. Jackson-kernel files are byte-identical.
- **Confidence:** high; actual compiled post-processor, agreement at all three energies.
- **Reason:** spectral-density definition; [KITE Eqs. (2.19)–(2.20), Fig. 1(a)](https://arxiv.org/abs/1910.05194).

### KITE-TOOLS-003 — threaded LDOS silently loses remainder moments

- **Location:** `tools/Src/Spectral/ldos.cpp:245–265`.
- **Wrong:** P threads each receive floor(M/P) moments; remaining moments are discarded. No divisibility restriction is enforced for the supported `-M` override.
- **Before → correct/after:** five-moment Jackson LDOS of an isolated zero-energy level: one thread `0.742723`, two threads `0.689671` → both `0.742723` 1/eV; independent `0.7427230677621784`.
- **Effect:** changing decomposition/thread count changes spectral results; if threads outnumber moments, all contributions can be lost. The demonstrated case uses only two threads.
- **Evidence:** repro and reasoning, before, after, patch (`repro/KITE-TOOLS-003/`).
- **Independent check/control:** NumPy eigensystem and complete finite Jackson expansion. Input contains 128 moments, with a legal `-M 5` post-processing override, avoiding any untested odd-moment core calculation. Four-moment two-thread output is byte-identical.
- **Confidence:** high for Jackson LDOS, actual compiled post-processor. Separate Green indexing concern below remains outside this fix.
- **Reason:** finite Chebyshev/Jackson expansion, [Weiße et al., Eqs. (71)–(72)](https://arxiv.org/abs/cond-mat/0504627).

### Suspected — not confirmed and not included as fixes

1. **Green LDOS moment index across threads:** `tools/Src/Spectral/ldos.cpp:277` passes local `m` to `green`, while the Jackson path uses the global index. Not independently isolated here. TOOLS-003 fixes partition sizes/offsets but does not claim to resolve this separate issue.
2. **Odd requested core moment counts:** `Src/Simulation/SimulationLMU.cpp:98–110` and `Src/Tools/Gamma1D.cpp:67–77` process pairs and write the n+1 entry without an obvious odd-tail guard. No runnable KITEx binary, so no memory-error or incorrect-output claim.
3. **Custom potential with nonzero energy shift:** `Src/Hamiltonian/Hamiltonian.cpp:387` subtracts Eshift from an additive local potential, while base onsite terms were already shifted. Additive use appears in `Src/Vector/KPM_Vector2D.cpp:475–478`. This needs a running core and a documented potential-definition check; no confirmed double-shift claim.

### Known issues excluded and upstream history reviewed

Read all 36 public issue/PR entries, all 28 PR bodies, all 19 issue comments and the one review comment before reporting; there were no open issues or PRs. Raw API snapshots are under `sources/` (`issues.json`, `pulls.json`, `all-issue-comments.json`, `all-review-comments.json`). Numerical cleanup PRs #4, #5, #6, #9 and recent #35–37 have retained diffs/comments. None contains the five fixes above. In particular:

- [#1](https://github.com/quantum-kite/kite/pull/1), [#2](https://github.com/quantum-kite/kite/pull/2), [#7](https://github.com/quantum-kite/kite/issues/7), [#8](https://github.com/quantum-kite/kite/issues/8), [#11](https://github.com/quantum-kite/kite/pull/11), [#13](https://github.com/quantum-kite/kite/issues/13): build/install/packaging and missing/old dependencies. Local build failures are recorded as limitations, not new bugs.
- [#14](https://github.com/quantum-kite/kite/issues/14): missing release 1.1 tag, restored; excluded.
- [#15](https://github.com/quantum-kite/kite/issues/15): TILE=8 size restrictions and large unit cells; excluded. Tiny post-processing fixtures do not claim KITEx can run prohibited lattice sizes.
- [#17](https://github.com/quantum-kite/kite/issues/17): server-dependent DOS/DC NaNs without a minimal input; no claim to diagnose it or report it again.
- [#5](https://github.com/quantum-kite/kite/pull/5), [#6](https://github.com/quantum-kite/kite/pull/6): second-order Gamma2 frequency argument already questioned in upstream comments; excluded.
- [#35–37](https://github.com/quantum-kite/kite/pull/37): the new `lattice.py` alternative; not itself reported as a bug. The latest four commits, all dated 2026-10-14, concern only this addition and merges. `sources/commits-six-months.json` covers 2026-05-06 onward; `sources/branches.json` also records development heads.

### Scope and use

Use [combined.patch](friends/ferreira-kite/combined.patch) to apply all five repairs together; the two standalone LDOS patches overlap, so avoid concatenating their diffs. The combined patch applies cleanly to the pin and its compiled post-processing plus both config repros agree with the isolated repairs (`checks/combined/check-output.txt`).

The normal chain, square-lattice and graphene DOS checks use independent exact spectra and a matched 64-moment Jackson expansion (`checks/dos_closed_forms.py`, `checks/dos/results.json`). The zero-current atomic optical check returns zero (`checks/zero_current/optcond.dat`). These validate the post-processing layer with exact supplied moments; they do **not** validate stochastic moments or the KITEx recursion.

KITEx failed two honest attempts: missing Eigen/OpenMP headers first; then Apple libc++ lacks std::cyl_bessel_j in the wavepacket translation unit. Core build work stopped. KITE-tools compiled, then linked successfully with explicit installed libomp. Dependencies were built/installed only inside this working directory, apart from reuse of already-installed Homebrew libomp. Python exporter tests do not call pybinding. Source remains unchanged at the pin; all changes are local diff artifacts and patched test copies. No issue, PR, fork, comment, or contact was made.

---

# Carlos Guedes — cubic identities

Folder: [friends/guedes-flm-identities/cg004-cubic-identities](friends/guedes-flm-identities/cg004-cubic-identities)

## Claim

_Source: [friends/guedes-flm-identities/cg004-cubic-identities/CLAIM.md](friends/guedes-flm-identities/cg004-cubic-identities/CLAIM.md)_

## guedes_CG004: printed cubic coordinate words do not follow from the paper's own definitions (11-05)

UNVERIFIED reproduction finding from the Guedes board job (computed 11-03 on a pod, before the 11-05 incident). Not an improvement claim; a possible erratum.

Paper: Guedes, Oriti and Raasakka, "Quantization maps, algebra representation and non-commutative Fourier transform for Lie groups", J. Math. Phys. 54, 083508 (2013), arXiv:1301.7750. Section 5.2 (5.2.1 symmetric map, 5.2.2 Duflo map, 5.2.3 Freidel-Livine-Majid map) displays coordinate-word expansions up to cubic order, journal pp. 083508-23 and -24 (arXiv pp. 25-26). Normalization: [X_i, X_j] = 2 i epsilon_ijk X_k.

Claim: the quadratic words agree in all three maps and the FLM cubics agree in all 27 cases, but the displayed symmetric cubics disagree with the map's own definition in 9 of 27 cases and the Duflo cubics in 15 of 27. Calculated minus displayed: symmetric -delta_ik X_j; Duflo -delta_ik X_j - (i/3) epsilon_ijk. Simplest witness, i=j=k=1 (no epsilon terms): symmetric displayed X1^3+X1 vs S^-1(Xhat1^3)=X1^3 by definition; Duflo displayed X1^3 vs X1^3 - X1 from D = S o j^(1/2)(d), j^(1/2) = 1 + Delta/6 + ..., Delta X1^3 = 6 X1 (also from the plane wave (t/sin t) exp(i t X1)); FLM displayed X1^3+X1 matches exp(i sin(t) X1).

Evidence (read-only, in a private working copy, not in this repository): REPRODUCTION_FINDING.md, its artifacts/ (baseline_verification.json, word_verification.json, control_verification.json, rendered journal/arXiv page images, source_manifest.json), search_words.py and verify_words.py.

Referee the exact claim: download the paper fresh (arXiv and, if reachable, the journal version), transcribe the displayed quadratic and cubic lists yourself, and recompute each from the paper's definitions with your own exact code (no import of the board's scripts). Check the normalization and conventions the paper actually uses (ordering, factors of i, the meaning of the displayed polynomial symbols), and whether any convention makes the displayed cubics correct. Report per map how many of the 27 cubics agree. Also check whether a published erratum or later version already corrects them. End HOLDS (the displayed cubics are wrong under the paper's own definitions), HOLDS WITH CAVEATS, or FAILS (they are right under the paper's conventions).

## Transcription

_Source: [friends/guedes-flm-identities/cg004-cubic-identities/TRANSCRIPTION.md](friends/guedes-flm-identities/cg004-cubic-identities/TRANSCRIPTION.md)_

## Independent transcription from fresh PDFs

Viewed rendered journal PDF pages 24--26 (journal labels 083508-23--25).
The FLM cubic is on journal page 25, one page beyond CLAIM.md's page range.
Fresh arXiv v2 shows the same formulas (PDF pages 26, 27, 29).

Write `x=(X1,X2,X3)`, `e(i,j,k)=epsilon_ijk`, `d(i,j)=delta_ij`,
`A_ij = i sum_m e(i,j,m) x_m` and
`B_ijk = i sum_m [e(i,j,m)x_k+e(i,k,m)x_j+e(j,k,m)x_i]x_m`.
Repeated `m` is summed; external `i,j,k` are arbitrary fixed indices.
Juxtaposition on the right means ordinary commuting polynomial product.

Displayed lists:

| Map | Quadratic | Cubic |
| --- | --- | --- |
| Symmetric | x_i x_j + A_ij | x_i x_j x_k + B_ijk + (2/3)d(j,k)x_i - (1/3)d(i,k)x_j + (2/3)d(i,j)x_k |
| Duflo | x_i x_j + A_ij - d(i,j)/3 | x_i x_j x_k + B_ijk + (1/3)d(j,k)x_i - (2/3)d(i,k)x_j + (1/3)d(i,j)x_k |
| FLM | x_i x_j + A_ij | x_i x_j x_k + B_ijk + d(j,k)x_i - d(i,k)x_j + d(i,j)x_k |

Definitions used for the independent rebuild:

- Section 3, journal Eq. (28): Q(f star g)=Q(f)Q(g).
- Section 5, Eq. (54): words equal Q^-1(hatX_i ... hatX_k);
  projection does not affect derivatives at identity (explicitly stated next page).
- SU(2) basis: Pauli matrices, sigma_i sigma_j=d(i,j)I+i e(i,j,k)sigma_k;
  hence [hatX_i,hatX_j]=2i e(i,j,k)hatX_k.
- S averages all permutations. Thus S(x_1^n)=hatX_1^n.
- D=S o j^(1/2)(partial); j(X)=(sinh|X|/|X|)^2.
  Therefore through degree three D=S o (1+Delta/6).
- D^-1(exp(i k.hatX))=(|k|/sin|k|)exp(i k.x).
- Q_FLM(exp(i p.x))=exp(i (asin|p|/|p|)p.hatX), journal Eq. (68).
  Its inverse plane wave is exp(i (sin|k|/|k|)k.x).

No proposing-job search or verifier code has been read or imported.

## Verdict

_Source: [friends/guedes-flm-identities/cg004-cubic-identities/VERDICT.md](friends/guedes-flm-identities/cg004-cubic-identities/VERDICT.md)_

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

## Prior Art

_Source: [friends/guedes-flm-identities/cg004-cubic-identities/PRIOR_ART.md](friends/guedes-flm-identities/cg004-cubic-identities/PRIOR_ART.md)_

## Prior-source check (2026-11-05)

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

### Completion check

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

---

# Carlos Guedes — coordinate word table

Folder: [friends/guedes-flm-identities/cg456-coordinate-word-table](friends/guedes-flm-identities/cg456-coordinate-word-table)

## Claim

_Source: [friends/guedes-flm-identities/cg456-coordinate-word-table/CLAIM.md](friends/guedes-flm-identities/cg456-coordinate-word-table/CLAIM.md)_

## guedes_CG456: correct coordinate-word lists through length 4 for the symmetric, Duflo and FLM maps (11-05)

UNVERIFIED extension from the Guedes board job (computed 11-03 on a pod before the 11-05 incident). It follows guedes_CG004 (HOLDS; re-check SURVIVES), which found that the printed symmetric and Duflo cubics in Section 5.2 are wrong.

Paper: Guedes, Oriti and Raasakka, J. Math. Phys. 54, 083508 (2013), arXiv:1301.7750, Section 5.2 (5.2.1 symmetric, 5.2.2 Duflo, 5.2.3 Freidel-Livine-Majid). The paper displays coordinate words up to length 3 only. Normalization [Xhat_i, Xhat_j] = 2 i epsilon_ijk Xhat_k.

Claim: the inverse images of all coordinate words Xhat_i1 ... Xhat_in for n = 1..4 (3 + 9 + 27 + 81 words per map) under each of the three quantization maps, as exact polynomials in commuting X_i with rational and imaginary coefficients, are as listed in the board job's artifacts/coordinate_words.json, in a private working copy, not in this repository (the board computed through length 6; only lengths 1-4 are claimed here). They agree with the paper's printed words wherever the printed words are right (all quadratics, FLM cubics) and give the corrected symmetric and Duflo cubics.

Not claimed: novelty of method. The maps are defined in all orders in the paper, and Kupriyanov-Vitale arXiv:1502.06544 Eq. (6.13) gives related machinery. The value is a correct, complete, checkable table through length 4.

Evidence (read-only): the board's REPORT.md, REPRODUCTION_FINDING.md, artifacts/coordinate_words.json, word_verification.json; and claims/guedes_CG004/VERDICT.md.

Referee the exact claim: download the paper fresh, write your own exact code from the paper's definitions of the three maps (do not import the board's search_words.py or verify_words.py), compute all words through length 4 for each map, and compare term by term with the length 1-4 entries of coordinate_words.json. Report the number of agreeing words per map and length, and any disagreement in full. Use a second independent method for at least the length-4 words of one map. End HOLDS, HOLDS WITH CAVEATS or FAILS.

## Verdict

_Source: [friends/guedes-flm-identities/cg456-coordinate-word-table/VERDICT.md](friends/guedes-flm-identities/cg456-coordinate-word-table/VERDICT.md)_

HOLDS
Referee: gpt-6.1-sol

All 360 claimed inverse images through length 4 agree exactly with an independent rebuild from [Guedes–Oriti–Raasakka, Sec. 5.2](https://arxiv.org/abs/1301.7750v2). The primary source names Carlos Guedes, Daniele Oriti and Matti Raasakka.

| Map | Length 1 | Length 2 | Length 3 | Length 4 |
| --- | --- | --- | --- | --- |
| Symmetric | 3/3 | 9/9 | 27/27 | 81/81 |
| Duflo | 3/3 | 9/9 | 27/27 | 81/81 |
| FLM | 3/3 | 9/9 | 27/27 | 81/81 |

No disagreements with the claimed table. Checked precisely Q⁻¹(Xhat_i1…Xhat_in), with [Xhat_i,Xhat_j]=2iε_ijk Xhat_k and ordinary commuting polynomial coordinates; no finite-spin quotient was substituted.

Ran referee_forward.py: exact PBW reduction, explicit forward quantization and triangular inversion; all 360 forward round trips pass. Separately ran referee_flm_action.py: Fraction-only differential action derived from the source FLM group law; all 81 quartics agree, plus 90 commutator controls. Neither imports proposing or previous-referee code.

All printed quadratics agree. Printed cubics agree 18/27 for symmetric, 12/27 for Duflo and 27/27 for FLM. Rebuilt minus printed: symmetric −δ_ik X_j; Duflo −δ_ik X_j−iε_ijk/3. All 24 printed disagreements are retained in comparison.json.

Trivial control: symmetric Q⁻¹(Xhat₁³)=X₁³, whereas its printed cubic gives X₁³+X₁. The claimed corrected table passes this control. Quartics at 1111 are X₁⁴, X₁⁴−2X₁²+7/15 and X₁⁴+4X₁² for symmetric, Duflo and FLM respectively.

Relative to the paper: explicit complete quartic lists and corrected cubic evaluations; all-order map definitions already exist. Related all-order Weyl/Duflo machinery appears in [Kupriyanov–Vitale (2015)](https://arxiv.org/abs/1502.06544). This is an exact algebra claim; published ML scores, hold-out, trivial predictive baselines and SBS do not apply. Lengths 5–6 were not checked.

Commands, derivations, fresh-source hashes and complete polynomials are in REPORT.md, manifest.json and rebuilt_*.json. Runs used one small process at a time; no infrastructure limit arose.

Strongest author objection: the cubic errors may be typographical examples, while the general maps already determine every table entry. This audit supports the finite table and does not refute the general construction.

NEXT BAR: independently derive symmetric and Duflo differential actions and check all 81 quartics per map, matching the second-method coverage already completed for FLM.

## Prior Art

_Source: [friends/guedes-flm-identities/cg456-coordinate-word-table/PRIOR_ART.md](friends/guedes-flm-identities/cg456-coordinate-word-table/PRIOR_ART.md)_

## Prior-art check (2026-11-05)

Scope: independent audit of the three quantization maps in Guedes, Oriti and Raasakka, arXiv:1301.7750, Section 5.2; exact coordinate words of lengths 1–4. No search for improved bounds or novelty is intended.

Primary source to retrieve fresh: https://arxiv.org/abs/1301.7750 and https://arxiv.org/pdf/1301.7750 . Related prior machinery named by the claim: Kupriyanov–Vitale, https://arxiv.org/abs/1502.06544 , Eq. (6.13).

The source paper defines all orders; the claimed contribution is an explicit table, correcting two cubic displays. There is no numerical scoreboard identified in the claim. Public code, recent literature, agent-result repositories and community searches will be logged below before any independent implementation is written. The proposed reference baseline is direct inversion of the source-defined quantization maps; this audit will not import claimant code.

### Public sweep before implementation
- Fresh arXiv abstract confirms Carlos Guedes, Daniele Oriti and Matti Raasakka, JMP 54 (2013) 083508, v2 dated 2013-09-27. PDF and TeX source downloaded locally (about 0.55 MB combined).
- Best reference construction: the primary paper's all-order symmetrization, Duflo factor and FLM plane waves. No scalar performance record or official leaderboard applies.
- Related source: Kupriyanov–Vitale, arXiv:1502.06544, https://arxiv.org/abs/1502.06544 . Its abstract describes an all-order Weyl differential representation and Duflo-related gauge operator.
- GitHub repository searches for Guedes+Duflo and Duflo+2026, sorted updated, failed with cache miss; indexed GitHub searches for Guedes/Duflo/star-product supplied no relevant code. This is a search limitation, not proof of absence.
- Indexed searches named BakeLab/Epi-results, google-deepmind/alphaevolve_results, openai/math, EinsteinArena, kisonecat/openai-math and plasma-ai/erdos with Duflo. No topic match surfaced. AlphaEvolve's live README was checked: https://github.com/google-deepmind/alphaevolve_results . No relevant scoreboard was identified. This is a limited indexed sweep, not a full repository-content audit.
- Recent arXiv queries for Duflo/star products in 2025–2026 and Guedes/quantization/erratum did not identify a replacement table or correction. Queries often returned unrelated people named Guedes or Duflo; these were excluded.
- Public community query (X, Reddit, blogs) found no relevant correction. The indexed nLab research bibliography https://ncatlab.org/zoranskoda/show/ncFourier points back to the primary paper and Freidel–Majid (2008), hep-th/0601004. No account, contact or post was made.
- Read claimant REPORT.md and REPRODUCTION_FINDING.md as claims, and certificate JSON as data. No proposing implementation was read. Earlier referee verdict is background only; its code/results are not being reused.

Reproduction plan: independently implement forward symmetrization and polynomial-map inversion; reconstruct FLM forward map from its local plane wave. Separately derive a differential left-action for FLM from the source group law and check all 81 quartics. These are two mathematical routes, not a search for an improvement.

---

# References


Everything here builds on other people's papers and code.

- Brian Armstrong, [publicly funded science as open source](https://x.com/brian_armstrong/status/2119150702446420027), November 7, 2026.
- Hogervorst, Penedones and Salehi Vaziri, [arXiv:2107.13871](https://arxiv.org/abs/2107.13871).
- Olivucci and Vieira, *Stampedes I*, [arXiv:2111.12131](https://arxiv.org/abs/2111.12131); Kostov, Petkova and Serban, [arXiv:1905.11467](https://arxiv.org/abs/1905.11467).
- Alho and Calogero, [arXiv:1907.09970](https://arxiv.org/abs/1907.09970); Alho, Calogero and Liljenberg, [arXiv:2104.11131](https://arxiv.org/abs/2104.11131); Alho, Hell and Uggla, [arXiv:1503.06994](https://arxiv.org/abs/1503.06994); Alho and Uggla, [arXiv:2407.14378](https://arxiv.org/abs/2407.14378).
- Fonseca and Zinn-Justin, [arXiv:1212.4672](https://arxiv.org/abs/1212.4672), *Comm. Math. Phys.* 328 (2014) 1079–1115.
- João, Anđelković, Covaci, Rappoport, Lopes and Ferreira, KITE, [*Royal Society Open Science* 7:191809 (2020)](https://doi.org/10.1098/rsos.191809).
- Arb/FLINT for the interval arithmetic behind the certificates.
- Anthropic Economics, [AI for scientific discovery: how researchers use Claude](https://www.anthropic.com/research/how-researchers-use-claude), November 5, 2026 — physics and astronomy at 40% of researcher time, against 32% for biology.
