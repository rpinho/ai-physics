# alho O011: certified higher-degree tracking Padé bounds

Submitted 2026-11-03T21:19:38.327526+00:00. State requested: claimed, awaiting independent referee and taste review. This worker makes no novelty or author-interest verdict.

## Published baseline and location

Best directly comparable public method located: Alho–Uggla, *New simple and accurate quintessence approximations*, arXiv:2407.14378v3, tracking [1/1]wDE from (26b),(58b,c),(81),(82). Figure 3 uses V=V0 phi^-p, p=1, Omega_phi0=.68 and 0<=z<=6. The immediately preceding discussion reports E error ~0.1% for p=1 and ~0.01% for p=.1. Source: https://arxiv.org/html/2407.14378v3 . The queue's ~0.1% Omega_m is a rough summary, not an exact table value. The 2511.02727v1 review §4 retains [1/1]. See local PRIOR_ART.md for dated audit and end refresh; community/code-search coverage has explicit gaps.

The published method was reproduced first on the pod. Floating maxima (percent, **UNVERIFIED as exact maxima**): p=1 Omega_m 0.2672536124%, E 0.1338952460%; p=.1 Omega_m 0.02072648818%, E 0.01036485532%. Source w0 and wa are reproduced to their printed digits. No claim that the authors made an error follows from the queue's rough number.

## Result and frozen problem

Same original tracker branch, both p=1 and p=1/10, Omega_phi0=17/25, dust plus scalar with no radiation, full closed interval 0<=z<=6. PLAN.md froze these before search. There is no statistical dataset or hold-out.

Analytically generated w(T) [6/6] Padé, exact rational series through order 12, no trajectory fit. Density follows R(T)=T exp(integral_0^T (w(s)/w_inf-1)/s ds), with R(T0)=17/8. This is a disclosed self-consistent normalization change from the source; it is controlled separately below.

| p | certified uniform Omega_m relative error | certified uniform E relative error |
|---|---:|---:|
| 1 | <1.326e-5 (<0.001326%) | <6.63e-6 (<0.000663%) |
| 1/10 | <1.209e-5 (<0.001209%) | <6.05e-6 (<0.000605%) |

Common safe limits: **Omega_m <0.0014%, E <0.0007%**. These are conservative supremum upper bounds, not claimed exact maxima. Smaller float errors remain unverified. Degree [2/2] also passed independently; degrees 3–5 are not certified claims.

## Verification and controls

Independently written verify_uniform.py never imports the search code. It checks all three source ODE coefficient identities and Padé matching over exact rationals. An independent Omega-variable auxiliary rational reference is verified by an inward contracting tube (radius 1e-6, 1024 intervals). Arb/Acb at 160 bits validates time-map quadrature and every continuous error cell: 3034 for p=1, 4557 for p=.1. It returned PASS for both p values, including a full pipeline rerun completed 2026-11-03T21:17:02Z. PROOF.md is the mathematical justification; this is not a proof-assistant formalization.

At exact true Omega_phi=2/5, inside the frozen redshift interval, the checker proves each control error positive and larger than the candidate's uniform upper, for both metrics. For the published [1/1], conservative relative lower bounds are p=1 Omega_m >.0026710, E >.0013382; p=.1 Omega_m >.00019708, E >.00009855. Controls also include [1/1] with the candidate's density-consistent normalization (stronger than the published formula), constant wCDM at w=-2/(p+2), and LambdaCDM. Thus each candidate has lower worst-case error; pointwise superiority at every z is not asserted. Exact control inequalities are in uniform_certificate*.json.

## Local code, data and reproduction

Mini directory: friends_pf_alho/O011_worker/

- Code: baseline.py, attempt1.py, enclosure_reference.py, verify_uniform.py, run_science.sh.
- Exact coefficients: pod_results/attempt1_p1.0.json and attempt1_p0.1.json; auxiliary reference enclosure_p*.json.
- Certificates: pod_results/uniform_certificate.json and uniform_certificate_p*.json; logs, environment.json, SCIENCE_COMPLETE, process_check.json and SHA256SUMS.json accompany them.
- Data/source receipts: pod_results/baseline.json and pod_results/sources/ (original HTML, public API replies, timestamps and hashes).
- Protocol: PLAN.md, immutable config_A1.json and ATTEMPT1.md; config SHA-256 2feaf1fea82f6b1f8ec61268a4c7828af93c90c5a8172d568fdf6abcdefa615f.
- Argument and instructions: PROOF.md, REPORT.md, PRIOR_ART.md. REPORT.md has the exact transport/launch/poll/pull commands; all scientific work runs on mscr, nice 10, thread caps 1, at most two simultaneous potential workers.

Protected pod copy: /workspace/alho/RESULTS/O011/. Active code directory: /workspace/alho/O011/. Small-file archive and SHA-256 verification receipt are kept on the Mini. No large inputs or external/private data are required. No own scientific workers remain running.

## Worries for the referee and taste stage

Check the source-to-ODE transformation, singular-past tracker tube argument, interval quadrature semantics and full-domain error derivative, rather than relying only on PASS. The exact baseline suprema are only numerical reproductions; strict improvement instead follows from rigorous control point lower bounds. The bounds are loose compared with floating diagnostics. Normalization and degree both change, hence the normalization-only control. Longer rational formulas and quadrature sacrifice simplicity; no claim about other p, radiation, data fitting or cosmological inference is made. Prior-art searches cannot establish exhaustive absence, and taste/novelty are explicitly left to the designated separate stage.
