# alho O004 — proposed full above-natural-density Signorini existence theorem

**Status: claimed for external referee and taste; no self-adjudication of novelty.**

## Published number and exact location

Alho–Calogero, [1907.09970v2 §6.4](https://arxiv.org/abs/1907.09970v2), printed p.28, leaves quasi-linear Signorini regular-ball existence outside its theorem (exponents a=b=−2,c=1). Best located target-specific public method is Alho–Calogero–Liljenberg [2104.11131v2 §3.4/Figure8](https://arxiv.org/abs/2104.11131v2), printed pp.17–18: numerical finite-radius balls at δc=2, ν=−0.5 and0.25, numerical success for tested δc>1 and −1<ν<1/2, and explicit question(a) about existence. There is no tabulated certified radius. Do not describe the baseline as zero general existence results: Beig–Schmidt already gives a generic small-body theorem.

## Proposed result

For **every** −1<ν<1/2 and **every prescribed** δc>1, prove a strongly regular static quasi-linear Signorini ball with finite radius, positive density and positive interior principal pressures. At its surface radial pressure is zero while density and tangential pressure remain positive. Thus the claimed movement is numerical evidence → an analytic existence theorem for the entire parameter range of question(a), not a faster shooting solver.

Explicit certificate: α=2+8ν, B=3/[2(α+6)], Z=δc^(2/3), ε=(6−α)/[2(7Z²+6Z)], N=9B(Z+1)². Until a first pressure zero, 1<x≤δc^(1/3), ε<y<1, P_y≥2B(6−α). A virial inequality forces R_s²≤5N/(3ε). Exact example ν=1/4,δc=8: ε=1/136,N=135/4,R_s²≤7650. Dimensionless s=r√[4πGK²/(3κ)]. The radius upper bound is not tight.

## Local code and evidence

Root: `friends_pf_alho/O004_worker/`.

- `PROOF.md`: complete center, barrier, tangential pressure, continuation and finite-radius proof.
- `derive_barriers.py`: SymPy producer; `verify_signorini.py`: independent stdlib Fraction Laurent-polynomial verifier, reconstructed from literal source stored energy; `verify_instance.py`: exact rational example.
- `pod_results/exact_verification.json`: PASS26 checks; `pod_results/barrier_certificate.json`; `pod_results/rational_instance.json`; producer/verifier logs and copied source code.
- `baseline.py`, `pod_results/baseline.json`: Figure8 parameters reproduced first at two tolerances. Surface s=1.23262325218866 and1.07701968265372 for ν=−0.5 and0.25; surface δ=1.73087188579510 and1.24380776644345. Those digits are our reproduction, not numbers tabulated in the source. Baselines are uncertified floating point and do not support the theorem by themselves.
- `PRIOR_ART.md`, `SWEEP.md`, `pod_results/prior/`: primary sources, dated audit, raw public-source receipts and final recheck. `REPORT.md`: exact pod reproduction commands. `PLAN.md`, immutable `config_A1.json` and `ATTEMPT1.md`: frozen method/kill-line and outcome. `BACKUP_RECEIPT.json`, `pod_results/process_audit.json`: backup and worker-lifecycle evidence.

All scientific computation was on mscr, nice10, capped threads, under8 cores. Protected source outputs `/workspace/alho/RESULTS/O004`; work/input PDFs `/workspace/alho/O004`. Mini work was editing/transport only. No sealed data or biological work.

## Verification and controls

A separately written exact rational polynomial engine differentiates the 2020 stored energy, reconstructs both pressures, and checks26 source identities, positive-sign decompositions, local unstable eigenvector, radial balance and negative controls. It imports nothing from the SymPy producer. `PROOF.md` supplies the standard unstable-manifold and ODE continuation arguments; those analytic theorems are not formalized by the checker. This is an exact algebraic certificate plus a human-readable analytic proof, pending external review.

Controls include reproduction at printed Figure8 parameters, the natural zero-pressure state, rejection of a wrong initial pressure constant (bad run explicitly retained/labelled and rerun before construction), rejection of a universal fixed2/3 barrier near ν=1/2, exclusion of the fluid endpoint where ε=0, and the no-gravity constant-pressure infinite branch. The Beig–Schmidt small-body result is an older perturbative control; the proposed theorem prescribes all δc>1.

## Worries and scope

The referee should scrutinize local unstable-fiber existence/regularity and the compact first-exit/continuation step, beyond checking polynomial identities. No machine-formalized proof, interval trajectory, pressure transversality, fluid-endpoint, low-density-branch or stability claim is made. Priority coverage is incomplete: GitHub code search was unauthorized/rate-limited, X required login, Reddit403, and repository trees were rate-limited. A public2019 Alho talk explicitly mentions Signorini existence, although the later paper poses this question and no complete proof was located. Generic variational/perturbative results may affect priority; the external taste stage must decide. No “first” claim is made.

Requested `_codex/friends_pf_alho.md` was absent. RULES/current Alho board specification and common portfolio claim requirements were read; this package includes the published/result/code/verification/control/worry fields. Only O004 was edited. A1 cleared its frozen kill line; no failed-attempt close or artificial A2 is being submitted. No contact or publication occurred.
