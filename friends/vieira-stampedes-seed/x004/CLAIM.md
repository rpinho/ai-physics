# vieira_X004 — proposed closed single-light-cone Toda seed

Submitted 2026-11-03 for independent mechanical referee and separate taste review. Neither review has been performed by this worker. Only queue row X004 is owned by this worker.

## Published baseline and open item

Olivucci–Vieira, [Stampedes I,2111.12131v2](https://arxiv.org/abs/2111.12131v2), JHEP07(2022)017. The unnumbered table on printed page 13 in section4 gives30 entries for bridges 0,1,2 through six loops, including c^(1)_(2,4)=1 and c^(0)_(2,4)=18/5. All30 were reproduced first.

The best public general method is the exact all-loop arbitrary-bridge determinant of Kostov–Petkova–Serban,[1905.11467](https://arxiv.org/abs/1905.11467), equations1.38–1.40; its coverage already includes larger bridge rows. A1 independently confirmed those rows with the sl(2) Hamiltonian but did not improve that coverage. Immutable ATTEMPT1.md records the failure and SWEEP.md precedes A2.

A2 changes formulation to a stated open item in the same paper: section4 equation 4.10/page 14 reports an unresummed single-LCDS seed series through (L/B)^6; appendixE equation E.7/page 28 displays its corrections, and the paragraph after E.10/page 29 requests a closed resummation. The [published PDF](https://inspirehep.net/files/a85c2fd13096f2cdc4ad8195d2604431) was checked. In arXiv HTML these are equations93 and96. This claim replaces that unresummed seed, rather than asserting better numerical accuracy than an exact determinant.

## Proposed result

In the leading-power double-light-cone sector of appendixE, retaining all inverse-log corrections, write L=g^2*log(z), B=log(1/bar(z)) and g^2=-lambda as there. Then

    tau(L,B)=O1/O0
            =exp(i*pi*L)*1F1(1/2+i*B/(2*pi);1;-2*i*pi*L).

Equivalently,

    L*tau_LL+tau_L+(pi^2*L-B)*tau=0, tau(0,B)=1,
    a_0=1, a_-1=0, (n+1)^2*a_(n+1)=B*a_n-pi^2*a_(n-1).

This is an all-order formal identity, not a general-cross-ratio octagon formula. The source's equation E.8/94 then expresses every bridge ratio as its mixed-derivative determinant. No new all-order proof of that already stated Toda hierarchy is claimed.

PROOF.md supplies an all-order argument independent of coefficient fitting: the Bessel recurrence gives a rank-one relation between kernels K0 and K1. The determinant lemma identifiesD1/D0 with Q(0), where Q=(1-K0*chi)^(-1)J0(sqrt(x)). The exact published resolvent ODE ([Belitsky–Korchemsky,2003.01121](https://arxiv.org/abs/2003.01121), equations27,29,30) at x=0, with the known zero-bridge Gaussian, reduces to the displayed ODE. Kummer's equation gives the unique regular solution. The kernel definition for arbitrary bridge is [2006.01831](https://arxiv.org/abs/2006.01831), equations23–25.

## Verification and controls

All computation ran on pod mscr, nice 10, at most 8 cores, thread counts 1. The Mini performed editing and transport only.

- Baseline: 30/30 published coefficient entries; 108 baseline and 156 extension Hamiltonian matrix elements agree exactly with independently coded determinant coefficients. Extensions cover bridge 3 through loop 12 and bridge 4 through loop 14, with J=1..6. These finite J checks are not an all-spin theorem.
- A2: 650/650 independent exact rational seed coefficient checks through L^24 at B=0,...,25,pi^2=1. The public full determinant includes all contributing particle sectors and does not import the proposed ODE. The separate verifier uses only the frozen recurrence. Degree bounds and weighted homogeneity turn these evaluations into polynomial identities, not statistical validation.
- Supplemental: 3250/3250 higher-bridge comparisons for bridges 2..6 through L^24 at the same 26 B values. Seed mixed derivatives use a signed-subset determinant algorithm, separate from KPS Gaussian elimination. Five symbolic checks audit the kernel relation, boundary value, potential, Kummer substitution and cusp expansion. Zero failures throughout.
- Trivial controls: I0(2*sqrt(L*B)) differs in 587 seed coefficient entries. A1's single-ladder/binomial control misses 30 nontrivial multi-ladder extension cases.

Concrete multi-ladder certificate: bridge 3,J=2,loop 10 has full 15393/256 versus single-ladder 4641/256. The two-ladder bridge coefficients include c^(3)_(4,6)=1 and c^(4)_(5,7)=1, with higher terms in ATTEMPT1.md. These are supporting verified data, not the claimed frontier.

The first three displayed source corrections informed A2 and are explicitly fitting evidence. config_A2.json and the later supplemental scope were frozen before their respective computations. No statistical or sealed hold-out was used or opened. Finite checks alone are not offered as the all-order proof.

## Files and exact reproduction

Mini root: `friends_pf_vieira/X004_worker/`.

- `PROOF.md`, `REPORT.md`, `PLAN.md`, immutable `ATTEMPT1.md`, `ATTEMPT2.md`, `config_A1.json`, `config_A2.json`.
- A1 code: `determinant.py`, `hamiltonian.py`, `compare.py`.
- A2 code: `toda_determinant.py`, `toda_verify.py`, `proof_verify.py`, `bridge_verify.py`.
- Exact data: `pod_results/baseline_determinant.json`, `comparison_baseline.json`, `comparison_extension.json`, `toda_det_B*.json`, `toda_verification.json`, `bridge_B*.json`, `bridge_verification.json`, `proof_verification.json`, logs and source receipts.
- Prior art: `PRIOR_ART.md`, `SWEEP.md`, `FINAL_RECHECK.md`, `PDF_AUDIT.md`, and timestamped public-source receipts in `pod_results/`. `backup_manifest.json` records transported-file hashes.

From the Mini:

```sh
cd friends_pf_vieira
python3 _codex/friends_podsh.py mscr X004_worker/pod_reproduce.sh 120
python3 _codex/friends_podsh.py mscr X004_worker/pod_poll_reproduce.sh 120
```

The payload starts a tracked nohup job under /workspace/vieira/X004. Outputs and logs go to /workspace/vieira/RESULTS/X004. Python dependencies: python-flint and SymPy. Do not run research computation on the Mini. The full command sequence is `reproduce_commands.sh`. Existing runs are complete; the reproduction payload is supplied for the separate referee.

## Worries and limits for the referee

1. Check the all-order source applicability and coefficientwise limit carefully. The claim projects out cross-ratio power corrections before specializing polynomial logarithms. B=0,...,25 are evaluation points of those formal coefficient polynomials, not actual finite-cross-ratio observations. No uniform finite-coupling remainder estimate is claimed.
2. Sign convention: sourceE.1–E.2/87 imply exp(-LB+pi^2*L^2/6), matching the full determinant in all 650 zero-bridge coefficient checks and the printed seed. The isolated single-LCDS Gaussian line prints a minus sign in both HTML and PDF. Our comparisons use the former convention; inspect PDF_AUDIT.md. No broader assertion about a physical-observable error is made.
3. Source 2003.01121 treats the simplest octagon; the asymptotic-octagon symbol differs by cross-ratio power corrections in this projected sector. Audit that projection and the exact rank-one identification, rather than relying on the finite match alone.
4. Prior-art coverage is limited by 403 GitHub code/tree responses and unreadable public X results. Current papers, source text, repository searches and AI-lab READMEs were rechecked 2026-11-03; no competing seed expression was identified. This does not establish novelty. Taste and author interest are for their designated review.
5. No claim of a new numerical record, full all-loop bootstrap, improved determinant accuracy, or additional biology result. No contact, post, email, PR or publication was made; no friend note was written.
