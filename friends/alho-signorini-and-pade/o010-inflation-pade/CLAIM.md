# alho O010 — certified extension of the monomial inflation endpoint table

Claim status: ready for independent referee. The worker does not supply a novelty or taste verdict.

Published target: Artur Alho, Juliette Hell and Claes Uggla, *Global dynamics and asymptotics for monomial scalar field potentials and perfect fluids*, arXiv:1503.06994v2 (2015), Table 1 on PDF page 28, equations (66),(68),(70),(72),(76),(79). Public source: https://arxiv.org/pdf/1503.06994 . The printed n=20 best row is [1/1]Sigma, 31% relative Hubble error at first q=0; theta is 81%, slow roll 97%.

Our result: the n=20 [4/4] Padé approximant in the inverse center-manifold variable f(z) has certified relative Hubble error **<0.000067% at the same first q=0 endpoint**. Its exact rational percent-error upper bound is

    33116497335187782100667131 / 500000000000000000000000000000.

Also added n=30,50,100 rows, with certified upper bounds <0.000074%, <0.000095%, and <0.000037%, respectively. n=2 and 3 extensions pass as well. No data fitting or empirical hold-out was used; this is a deterministic exact-equation certificate.

Baseline reproduction and stronger controls: all requested n=2,3,20 printed integer percentages are reproduced using source slow roll and the first-order tangency angle/Sigma curves, with rounding checked by interval assertions. The literal higher-order (66),(68) give stronger approximations than the printed table. At n=20 their verified errors are approximately 0.654853089624% and 3.855396638078%. The source Hubble [2/2] formula (76b), independently rebuilt from (70), is stronger still at **0.386567606987%**. It is the best explicitly tested public n=20 formula and is also beaten. We do not use 31% as though it were the strongest formula available in the paper. All six added rows beat slow roll and the tested source formulas (66),(68),(76a,b).

Method and verification: let r=-Sigma/X^n, z=r² and f=n*tildeT*(1+r²)^((n+1)/(2n))/(3r). Then q=0 is exactly z=1/2. Construct P/Q from exact formal ODE coefficients, order 24. A separate standard-library Fraction verifier checks the series and Padé identities and proves strict polynomial residual signs over the whole [0,1/2] by rational Bernstein bounds. Upper/lower differential barriers, with an explicit singular-origin comparison argument, enclose the true attractor endpoint without a numerical initial condition. The approximant's monotonicity is separately certified. The Hubble error bound is rational. Arb at 256 bits encloses public-method roots and errors; exact polynomial checks exclude poles and multiple first endpoints. Two independent numerical integrations agree but are diagnostics only.

Mini paths:

- Report: `friends_pf_alho/O010_worker/REPORT.md`
- Proof: `friends_pf_alho/O010_worker/PROOF.md`
- Constructor: `friends_pf_alho/O010_worker/construct.py`
- Separate verifier: `friends_pf_alho/O010_worker/verify.py`
- Additional public controls: `friends_pf_alho/O010_worker/extra_controls.py`
- Source and complete raw evidence: `friends_pf_alho/O010_worker/pod_results/`
- Exact coefficients and certificates: `pod_results/certificate.json`, `certificate_n20.json` and other per-n files
- Source-control receipts: `pod_results/public_certificate_n*.json`, `extra_controls.json`, `baseline.json`, `crosscheck.json`
- Rebuild log and audit: `pod_results/reproduction.log`, `FINAL_AUDIT.json`
- Prior art: `friends_pf_alho/O010_worker/PRIOR_ART.md`
- Frozen attempt: `O010_worker/config_A1.json` and immutable `O010_worker/ATTEMPT1.md`

Pod copies are protected in `/workspace/alho/RESULTS/O010`. The full small result set was pulled through the approved helper and every file SHA-256 checked against `pod_results/MANIFEST.json` (55 files, about 3.5 MB uncompressed).

Reproduction from `friends_pf_alho` on the Mini:

```sh
python3 _codex/friends_podsh.py mscr O010_worker/reproduce.sh 90
python3 _codex/friends_podsh.py mscr O010_worker/poll_reproduction.sh 60
```

The first command starts a tracked nohup run. It computes only on mscr, nice 10, one thread per worker and at most six independent workers. The completed full rerun ended `O010_REPRODUCTION_PASS`; all tracked PIDs were confirmed exited. The code and certificates were copied back to the Mini after this rerun. No GPU or additional cores were needed.

What we worry about: the referee should audit the change of variables, admissible-domain argument and comparison at the singular r=0 endpoint; these are mathematical proof obligations beyond polynomial sign arithmetic. The printed table and literal formula comparisons must remain distinguished. The bound concerns the first q=0 endpoint and finitely many n, not an entire trajectory-error guarantee or a uniform convergence theorem. Higher-order Padé approximation and variable transformations were proposed in the source, and Medina–Álvarez (2024) already treat adapted monomial Hamilton–Jacobi expansions generally. The taste step must decide whether this certified table extension is useful. GitHub code API was rate-limited and X coverage was indexed/unauthenticated; no exhaustive novelty claim is made. No contact, commit, push, PR or external message occurred.
