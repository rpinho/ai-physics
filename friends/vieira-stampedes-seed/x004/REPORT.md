# Independent referee report

The submitted closed seed holds within its explicit formal projection, with qualifications about the source's Gaussian sign and finite-B interpretation. The all-order boundary-resolvent argument is applicable to that projection. No counterexample to that stated identity was found. See `VERDICT.md` for the requested decision and `DERIVATION.md` for the source audit and exact construction.

## What was independently checked

- Primary published JHEP PDF and four primary paper HTML sources, including actual authorship: Enrico Olivucci and Pedro Vieira. PDF pages 27–28 were also visually inspected after rendering on the pod.
- All 30 displayed bridge coefficients reproduced using an independent transcription of the public KPS formula and the source's factorial normalization. The published numbers 1 and 18/5 refer to different bridge rows of the same c_(2,4) convention.
- A different Bessel integral representation gave 528/528 exact rational coefficient matches through L^32, including five-particle sectors, for bridges 0–3 and B=-3/2,2/7,31,0 with pi^2=7/3. These are new referee points, not a statistical hold-out or a polynomial interpolation certificate for arbitrary B through degree 32.
- Direct Kummer-series coefficients matched the candidate recurrence in all four cases; imaginary parts canceled exactly. Mixed derivative determinants matched bridges 2–3.
- The first three printed E.7 terms matched symbolically in 99 coefficient comparisons through L^32. The rank-one identity, boundary value, cusp scaling and reduced potential passed exact symbolic checks.
- I0 fails at L^2, and in 109/132 fresh seed coefficients. The printed minus Gaussian fails in 101/132 fresh zero-bridge coefficients; the plus Gaussian passes every one.
- A finite-B scope control exposes the excluded terms already in [L]tau: (1+exp(-B))*log(1+exp(B)) rather than B. At B=2 the difference is about 0.4147764. The claim explicitly discards these cross-ratio power corrections, consistent with section 4's full inverse-log target.

No claimant search or verifier code was read, imported, or executed. Its claim, proof, configuration and notes were read as assertions to audit. There is no statistical or sealed hold-out; the displayed source corrections informed the candidate, and no predictive validation is inferred from later coefficients. Retrospective configuration files do not independently prove their creation history. This does not affect an exact identity established from applicable published equations.

## Reproduction

All research computation ran on mscr at nice 10. At most four worker processes were active, numerical thread limits were 1, and no research calculation ran on the Mini. Python 3.12.3, python-flint 0.9.0, SymPy 1.13.3. Only public sources and the referee's derived code were sent to the pod.

From this claim directory, using the provided helper:

```sh
python3 _codex/friends_podsh.py mscr pod_init.sh 60
python3 _codex/friends_podsh.py mscr pod_smoke.sh 120
python3 _codex/friends_podsh.py mscr pod_start.sh 60
python3 _codex/friends_podsh.py mscr pod_poll.sh 60
python3 _codex/friends_podsh.py mscr pod_source_audit.sh 60
```

`pod_smoke.sh` and `pod_source_audit.sh` contain the exact base64 payloads used. The full test command on the pod is `nice -n 10 python3 ref_bessel.py`, with OMP_NUM_THREADS, OPENBLAS_NUM_THREADS and MKL_NUM_THREADS all set to 1. Source acquisition is reproduced by `pod_sources.sh`; `pod_sweep.sh` and `pod_final_prior.sh` record the public literature/repository sweep. Cleanup does not remove the pod's code and compact results, so rerunning the two Python files also suffices there.

Evidence is protected locally in `evidence/`, with source responses, source receipts, the full PDF, rendered pages, rational coefficients, per-particle-sector coefficients, logs, scripts and a SHA256 manifest. All 51 archived files were verified against the pod manifest. `evidence.tar.gz` SHA256 is `75329aaaaec0ed498b93ff07a29d5e03a0154ba8d13ef27226b288918e4eb679`. Original root-code hashes agree with the archived executed copies.

`cleanup_receipt.txt` records temporary-download removal after verified backup and a final process check. The tracked worker PIDs include the ProcessPool parent, all four children, and the symbolic audit worker; all had exited before backup. The pod directory finishes well below 1 GB. No pod lifecycle operation, external contact, publication, or credential upload was performed.

## Literature and remaining bar

Primary references: [Stampedes I](https://arxiv.org/abs/2111.12131v2), [KPS determinant](https://arxiv.org/abs/1905.11467), [exact resolvent](https://arxiv.org/abs/2003.01121), [Bessel bridge determinant](https://arxiv.org/abs/2006.01831). `PRIOR_ART.md` records public code, lab repositories, recent arXiv and community search coverage and its limits. A later [2024 paper](https://arxiv.org/abs/2408.15331) recalls the known single-scaling Toda observation. The factual addition relative to Stampedes I is the closed Kummer form of the formal E.7 seed; the general determinant, Gaussian, resolvent equations and Toda representation were already public. Novelty, priority and author interest are not judged.

The next concrete bar is to quantify the omitted cross-ratio powers by a finite-B Fredholm comparison with an explicit remainder bound. Without that, the result remains a formal resummation and must not be presented as a finite-cross-ratio accuracy improvement.
