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
