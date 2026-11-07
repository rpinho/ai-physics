# dinis W011 — exact ordinary-invariant obstruction, pending referee and taste

Submitted 2026-11-03 America/New_York (2026-11-04 UTC). Scope is arXiv:1212.4672 Appendix C.2, with the algebra form stated explicitly. This worker makes no novelty or author-interest judgment.

## Published baseline and source

Tiago Fonseca and Paul Zinn-Justin, Higher spin polynomial solutions of quantum Knizhnik–Zamolodchikov equation, arXiv:1212.4672v2 (17 October 2013), Comm. Math. Phys. 328 (2014), 1079–1115, DOI 10.1007/s00220-014-1963-7. Primary text: https://arxiv.org/html/1212.4672 . Section 2.1 gives the horizontal generators and (2.1) their local matrices. Section 4.3.2 and Appendix C.2 prove injectivity of the fused-link map whenever [2]...[ell] are nonzero, including q=-exp(-i*pi/(ell+2)), and generic-q surjectivity. C.2 conjectures special-q isomorphism.

There is no printed numerical special-q dimension frontier to improve. At ell=3,L=6 the published generic characterization and full image rank specialize to the link count 34. We reproduce dimension 34 at generic q=2 exactly. The best public method is the source's triangular projection proof; checking rank 34 alone would only reproduce its theorem. PRIOR_ART.md documents later literature and final repository/source checks.

## Our number and statement

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

## Code and data on the Mini

Directory: friends_pf_dinis/W011_worker/ .

- REPORT.md: reproduction instructions, result/controls/limitations.
- PROOF.md: algebra convention, explicit family and finite lower/upper argument.
- PRIOR_ART.md: baseline and final literature/repository recheck, including coverage limits.
- config_A1.json and ATTEMPT1.md: frozen attempt and final immutable outcome.
- a1_rank.py, a1_witness.py: search and exact witness construction.
- verify_a1.py: independent exact verifier; imports no search/construction module.
- verify_projection.py, baseline_target.py: actual Jones–Wenzl recursion and same-size rational generic control.
- REPRODUCE.sh: pod-only nohup entrypoint. Run through `_codex/friends_podsh.py mscr SCRIPT.sh 90` as detailed in REPORT.md; poll the protected reproduce.log.
- pod_backup/a1_witness_ell3_L6.json: exact explicit coefficients and tensor basis states.
- pod_backup/verified_patterns_ell3_L6.json: complete 34-pattern list.
- pod_backup/verification_ell3_L6.json, verification_ell1_L10.json, verification_projection.json, baseline_target_ell3_L6.json: PASS receipts.
- pod_backup/exact_pipeline.log and baseline_target.log: completed verification logs.
- W011_results.tar.gz, BACKUP_RECEIPT.json and pod_backup/SHA256_MANIFEST.json: checksummed backup.

The protected pod originals are /workspace/dinis/RESULTS/W011. Small artifacts are well below 50 MB; no bulky datasets are needed.

## Verification

The independent verifier implements Z[q]/Phi_5(q) arithmetic directly, builds the local tensor E/F matrices separately, enumerates noncrossing singlet orientations and reconstructs fused columns. It checks exact E/F invariance of all columns and witnesses, and direct regular divided-power action, without dividing by vanishing [5]. It independently checks all 34 columns are killed by E^(5), while E^(5)w_9=2w_14 is nonzero. Actual Jones–Wenzl recursion is separately checked against the compact projection normalization over Q and Q(zeta_5).

Modular column rank 34, and rank 35 after adding w_9, is checked at prime 1000081 with embeddings q=188136 and q=287744. The prime is separately checked by trial division. Independent E/F row assembly gives ranks 119,545,119 in the three K=1 sectors of sizes 120,580,120. Modular reduction supplies upper bounds 1,35,1 on characteristic-zero kernel dimensions; exact columns plus three witnesses attain them. This is an exact lower/upper certificate, not an assumption that modular nullity equals characteristic-zero nullity. The generic baseline uses exact rational annihilation plus matching modular lower/upper ranks. Main verification ends ALL PASS. Earlier launch/API errors remain in historical logs and are explicitly identified in REPORT.md.

## Controls and worries

Controls: source injectivity/full column rank; generic-q isomorphism reproduced before the root search on small cases and at the claimed size afterward; strict integer weight zero; direct divided-power separation; actual projector recursion; independent ell=1 cross-check. No predictive hold-out or sealed data is involved. All computation ran on mscr, nice 10, at most 8 processes and thread counts 1. Final process receipt confirms no worker remains.

Worries: the intended algebra form may make this an illustration of known representation theory rather than movement of the authors' intended conjecture. Later papers already establish the general categorical distinction. No matching finite table was found, which does not establish novelty; GitHub sorted-update API and unauthenticated code search/X retrieval had access limits, documented in PRIOR_ART.md. Other exploratory panel nullities are UNVERIFIED over characteristic zero and excluded from this claim. Neither VERDICT.md nor TASTE.md is supplied by this worker. Nothing was contacted or published externally.
