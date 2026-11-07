HOLDS WITH CAVEATS
Referee: gpt-6.1-sol

The Kummer expression matches the paper's formal seed with all inverse-log corrections. The boundary-resolvent argument yields its ODE to all orders within that projection; no counterexample to this stated claim was found.

The published numbers use the claimed normalization: my independent source-based code reproduced all 30 table entries, including c^(1)_(2,4)=1 and c^(0)_(2,4)=18/5. The paper is by Enrico Olivucci and Pedro Vieira.

I independently expanded the published Bessel integral operator, using Cauchy–Binet minors rather than the claimant's KPS elimination. All 528 rational coefficient comparisons through L^32 passed for bridges 0–3 at B=-3/2,2/7,31,0 and pi^2=7/3, including every contributing particle sector. Direct Kummer expansion and 99 symbolic comparisons with the first printed E.7 terms also passed. No claimant implementation was imported or executed.

The I0 control fails already at L^2: B^2/4 versus (B^2-pi^2)/4. It does not explain the corrections. This reformulates an existing exact determinant; it does not improve its accuracy or arbitrary-bridge coverage.

The published PDF contains a real sign conflict: its standalone Gaussian has minus pi^2 L^2/6, while E.1–E.2 and my determinant give plus. The claim openly uses the latter, consistent convention.

There was no statistical or sealed hold-out. The displayed corrections informed the candidate; later coefficient checks are algebraic corroboration, not evidence of predictive generalization.

Relative to Stampedes I, the addition is the closed Kummer form of E.7. Arbitrary-bridge determinants, the null Gaussian, resolvent equations and Toda representation were already public. A 2024 paper (arXiv:2408.15331) also recalls the single-scaling Toda observation; no novelty or priority judgment is made.

Strongest author objection: this is not the literal finite-B seed. The full Bessel-symbol limit has linear coefficient (1+exp(-B))*log(1+exp(B)), about 2.4147764 at B=2, whereas the proposed seed gives 2. Those cross-ratio power corrections are explicitly excluded by the claim and by its full inverse-log interpretation.

Evidence, source receipts, independent code and exact outputs are copied here; see REPORT.md and DERIVATION.md. Tracked pod workers exited, and temporary downloads were removed after verified backup.

NEXT BAR: give a finite-B Fredholm comparison with an explicit bound on the omitted cross-ratio power corrections.
