# Independent referee report

The explicitly ordinary-generator statement is verified, with the algebra-form
caveat below. Independent reconstruction imported no submitter code; only the
submitted witness JSON was read as data and compared coefficient by coefficient.

| ell,L,q | fused image | strict-zero ordinary invariants | all K=1 ordinary invariants | strict zero with divided E and F |
|---|---:|---:|---:|---:|
| 3,6,2 | 34 | 34 | 34 | — |
| 3,6,primitive fifth root | 34 | 35 | 37 | 34 |
| 1,10,primitive third root | 42 | 43 | 45 | 42 |

For ell=3,L=6 the E/F ranks are 119,545,119 on sectors of sizes
120,580,120. These ranks match at primes 101 and 151 with fifth-root
embeddings 36 and 8, different from the submitter's large prime. Exact projected
columns and the three exact witnesses attain the resulting kernel upper bounds.
All 34 columns are killed exactly by divided E^(5) and F^(5); E^(5)w_9=2w_14
is nonzero. Adding E^(5) alone raises the central operator rank to 546.
The ell=1 check used primes 103 and 151 and independently generated 42 columns.

I reconstructed the actual 2^ell-by-2^ell projector recursion, checked its
idempotence and intertwining with both local generators, enumerated noncrossing
matchings without within-block arcs, and projected their singlet orientations.
This avoids the submitter's compact projection formula. Exact arithmetic used
python-flint 0.9.0 over Q and Q[x]/Phi_p, and nmod_mat for modular ranks.
The special complex q is covered because the identities hold in its cyclotomic
field, including all Galois conjugates. Detailed proof audit: PROOF_AUDIT.md.

The run took 6.29 seconds on one pod CPU at nice 10, with library thread counts
one. There was one initial JSON string-to-rational parsing error, fixed before
the complete ALL PASS run; both logs are retained. No predictive hold-out exists
in this deterministic algebra problem; the claim describes its parameter sweep
openly and does not assert held-out performance.

Reproduction, using only the claim directory and the approved helper:

```sh
python3 _codex/friends_podsh.py mscr pod_launch.sh 90
python3 _codex/friends_podsh.py mscr pod_poll.sh 90
```

pod_launch.sh embeds the final code and witness data. The exact final source
is referee.py and evidence/referee.py; their SHA256 is recorded in
evidence/pod_manifest.json. The archive referee_evidence.tar.gz and extracted
evidence/ were copied back and all ten payload hashes checked on the Mini.
The archive contains every machine result needed for the verdict; the pod is
not required to retain them. No large intermediate was generated.

Interpretation is the main limit: imposing regular divided-power invariance
removes the entire extra strict-zero dimension. Thus these numbers do not
disprove a divided-power or flat-specialization reading. The source's literal
Chevalley-generator description supports the restricted claim, but does not
resolve author intent. The prior-art and identity audits, with primary links,
are in PRIOR_ART.md; the general ordinary/divided-power distinction predates
this job. Relative to Appendix C.2, the contribution under review is the explicit
ordinary-kernel dimension/witness and the odd-level obstruction family, rather
than a better link-image rank or a published numerical score. No novelty,
priority, or author-interest conclusion is drawn.
