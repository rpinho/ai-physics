# Independent referee report: alho_O004

The proposed existence theorem survives this audit. The review covers the
literal tau=0 Signorini law and every fixed -1<nu<1/2, delta_c>1. It is a
human mathematical audit with exact symbolic support, not machine-formalized
analysis. The logical review, including an independent integral formulation
of center existence, is in ANALYSIS.md. The short decision is VERDICT.md.

## Reproduction

All scientific work ran on the shared mscr pod, under
`/workspace/ref_alho_O004`, with nice 10 and thread caps of one. The Mini
performed file editing, reading and transport only. The pod initially had
163,262,689,280 bytes available, well above the 5 GB infrastructure cutoff.
There were no other files in this task's pod directory initially.

From this claim directory, run the following transport commands. The pod
scripts contain the base64 payloads of the adjacent independent Python files.
Each background script records its PID and writes its own log; poll before
proceeding to export. No claimant search/verifier code is used.

```sh
python3 _codex/friends_podsh.py mscr pod_setup.sh 90
python3 _codex/friends_podsh.py mscr pod_fetch.sh 90
python3 _codex/friends_podsh.py mscr pod_run.sh 90
python3 _codex/friends_podsh.py mscr pod_poll.sh 90
python3 _codex/friends_podsh.py mscr pod_replay.sh 90
python3 _codex/friends_podsh.py mscr pod_replay_poll.sh 90
python3 _codex/friends_podsh.py mscr pod_figure.sh 90
python3 _codex/friends_podsh.py mscr pod_units.sh 90
python3 _codex/friends_podsh.py mscr pod_recheck.sh 90
python3 pull_artifacts.py
```

Recorded environment: Python 3.12.3, SymPy 1.14.0, SciPy 1.18.1,
NumPy 2.5.4, mpmath 1.3.0, pypdf 6.21.4. Initial PDF extraction emitted
fontTools warnings; the key formulas were checked against primary HTML,
and the actual Figure 8 PDF page was rendered separately with PyMuPDF.
The setup script now specifies a task-local cache and disables pip caching.
The initial setup invocation used pip's default cache; no cache outside
the task directory was subsequently inspected, exported, or deleted.

## Results and scope

`pod_evidence/independent_exact.json` contains 36 exact rational symbolic
identity checks derived from the primary energies and force/mass equations.
They include the center Jacobian/eigenvector, pressure-denominator gap,
barrier signs, tangential-pressure implication, virial identity and the
rational example epsilon=1/136, N=135/4, R_s^2<=7650. All passed.
`independent_referee.py` is original referee code. The reviewed claimant
proof is retained as `reviewed_PROOF.md`; it was read as an argument, not
executed as code. The analytic theorems and domain signs are reviewed in
ANALYSIS.md, not established merely by a script's PASS.

The independent density-variable baseline reproduces R_s about
1.232623252189 and 1.077019682654 at delta_c=2, nu=-0.5 and 0.25,
respectively, with agreement about 5e-13 with the supplied results.
Figure 8 plots ordinary radius; the corresponding radii for G=K=kappa=1
are about 0.60226281725 and 0.52623452231. That unit convention is inferred
from the plot, not explicitly documented nearby. The many digits are our
computations, not published measured/certified values.

Forty-two stress cases all found a finite pressure zero. One coarse dense
output gave negative tangential pressure near nu=-1 and delta_c=1; it is
retained verbatim in `independent_stress.json` and the false summary flag
is retained in `independent_summary.json`. Three tighter integrations and
two 70-digit runs resolved it as a numerical artifact; see `flag_replay.json`.
Neither the original nor refined numerical trajectories are certificates.
The exact sign proof supplies positivity throughout the parameter range.
Removing gravity gave constant compressed branches without any surface.
Other negative controls checked the natural state, a wrong pressure
constant, the fixed two-thirds barrier and the excluded fluid endpoint.

No dataset or hold-out is involved. Public Figure 8 cases are calibration,
not hidden validation. The generic small-body theorem does not cover all
prescribed central densities. No endpoint, stability, uniqueness or
transversality claim is being verified.

## Literature and next step

PRIOR_ART.md records the primary papers, author/affiliation match, the
Beig–Schmidt small-body theorem, the Calogero–Leonori variational result,
and the 2019 Alho talk mentioning Signorini. It also records recent-first
arXiv, GitHub repository/issue queries, seven AI result-repository indices,
and community access failures. The source/repository recheck was unchanged.
GitHub code search was rate limited, X required login, Reddit was blocked;
the searches cannot establish novelty. No priority/taste judgment is made.

Relative to the papers, the proposed addition is the full-parameter analytic
existence argument and explicit loose radius bound, replacing their numerical
support for question (a). Its center and compact-continuation arguments
should be presented as explicit lemmas in a complete mathematical manuscript.
The NEXT BAR in VERDICT.md is aimed at making that analytic dependency
self-contained. All decisive evidence has been copied locally; final
transport and cleanup receipts are retained alongside this report.
