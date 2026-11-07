# Independent referee report: penedones_NB01

The claimed bound survives an independent all-spectrum verification. The remaining caveat is historical reproducibility: the eight parameter pairs behind the paper's printed 5.67049 were not recovered, so the directly reproduced baseline is its fully specified 6.43174 example. This does not obstruct proving the new inequality for the same coefficient, normalization, external dimension h=5/8 and principal-series gap 8.53.

The primary paper is [Hogervorst, Penedones and Salehi Vaziri, arXiv:2107.13871v2](https://arxiv.org/abs/2107.13871); Penedones is indeed João Penedones, EPFL, in its author block. Equation (5.53) prints 5.67049. My independent gamma/3F2 implementation gives 6.431737260572546574... for equation (5.52), and 2.386377515308742831... for its companion h=3/8 case. Applied to the reconstructed new crossing test, it gives 5.4580734714720031025... .

A second implementation, written here without importing claimant code, integrates convergent endpoint series using 640-bit Arb arithmetic, explicit truncation bounds, and exact rational polynomial coefficients. It independently certifies all 61 closed intervals covering nu in [8.53,39], every finite even discrete mode through n=38, both infinite tails, and the objective inequality -D/F2 < 34113/6250. The run took about 115 seconds on four pod workers. [DERIVATION.md](DERIVATION.md) supplies the argument; `referee_certificate/VERIFIED.json` is the fresh acceptance record. Full charts, primary sources, public audit receipts and all four scientific scripts are preserved in [REFEREE_EVIDENCE.tar.gz](REFEREE_EVIDENCE.tar.gz), with a separate SHA-256 receipt. No existing cached spectral values are needed to reproduce it.

The controls actively catch invalid shortcuts. A single degree-1 term gives objective 10.8757188312. Removing degree 5 yields apparent 2.78965859952 but fails at discrete n=6; removing degree 7 also fails there. Removing degree 3 worsens the objective to 17.63037. Removing the principal gap exposes negative action near nu=2.21. These are diagnostic controls, not alternate certified bounds. There is no statistical hold-out; a frozen rational witness must instead satisfy every allowed spectral constraint, which the new certificate proves.

The claimant search and verifier are separate modules with no verifier import of a search module. That alone would not establish correctness; the referee certificate imports neither. Its integration route differs from the claimant's Gaussian quadrature. All numerical evaluation, public-source processing and certification ran on mscr under the authorized directory. The Mini only held edits, transported artifacts and checked file integrity.

To reproduce on an authorized compute host, copy the evidence archive into a fresh directory, then run:

```sh
tar -xzf REFEREE_EVIDENCE.tar.gz
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
nice -n 10 python3 independent_check.py > independent.jsonl
nice -n 10 python3 certify_referee.py > certificate.log
nice -n 10 python3 controls_referee.py > controls.jsonl
```

The recorded environment is Python 3.12.3, python-flint 0.9.0, mpmath 1.3.0, NumPy 2.1.2 and SciPy 1.18.1. The rigorous certificate itself needs only python-flint and the Python standard library. Its source hashes are embedded in the acceptance record.

[PRIOR_ART.md](PRIOR_ART.md) records the primary-source, recent-paper, GitHub/open-issue, agent-repository and community screens, including access/coverage limitations. An encountered prior result is Salehi Vaziri's thesis repeating 5.67049. The paper already describes linear programming over regularizing functionals. The added result is the concrete rational witness, smaller certified number and full-spectrum certificate within that framework; no optimality, novelty or priority conclusion is drawn.

The strongest technical objection is that the direct baseline reproduction does not recover the historical eight-functional calculation behind 5.67049. Recovering those eight pairs and coefficients and checking them with this independent evaluator would clear that reproducibility caveat. No further computation is needed to establish the new 34113/6250 inequality under the stated paper assumptions.
