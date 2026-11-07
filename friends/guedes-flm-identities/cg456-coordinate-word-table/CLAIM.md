# guedes_CG456: correct coordinate-word lists through length 4 for the symmetric, Duflo and FLM maps (11-05)

UNVERIFIED extension from the Guedes board job (friends_board_guedes_1103, computed 11-03 on a pod before the 11-05 incident). It follows guedes_CG004 (HOLDS; re-check SURVIVES), which found that the printed symmetric and Duflo cubics in Section 5.2 are wrong.

Paper: Guedes, Oriti and Raasakka, J. Math. Phys. 54, 083508 (2013), arXiv:1301.7750, Section 5.2 (5.2.1 symmetric, 5.2.2 Duflo, 5.2.3 Freidel-Livine-Majid). The paper displays coordinate words up to length 3 only. Normalization [Xhat_i, Xhat_j] = 2 i epsilon_ijk Xhat_k.

Claim: the inverse images of all coordinate words Xhat_i1 ... Xhat_in for n = 1..4 (3 + 9 + 27 + 81 words per map) under each of the three quantization maps, as exact polynomials in commuting X_i with rational and imaginary coefficients, are as listed in friends_board_guedes_1103/artifacts/coordinate_words.json (the board computed through length 6; only lengths 1-4 are claimed here). They agree with the paper's printed words wherever the printed words are right (all quadratics, FLM cubics) and give the corrected symmetric and Duflo cubics.

Not claimed: novelty of method. The maps are defined in all orders in the paper, and Kupriyanov-Vitale arXiv:1502.06544 Eq. (6.13) gives related machinery. The value is a correct, complete, checkable table through length 4.

Evidence (read-only): the board's REPORT.md, REPRODUCTION_FINDING.md, artifacts/coordinate_words.json, word_verification.json; and claims/guedes_CG004/VERDICT.md.

Referee the exact claim: download the paper fresh, write your own exact code from the paper's definitions of the three maps (do not import the board's search_words.py or verify_words.py), compute all words through length 4 for each map, and compare term by term with the length 1-4 entries of coordinate_words.json. Report the number of agreeing words per map and length, and any disagreement in full. Use a second independent method for at least the length-4 words of one map. End HOLDS, HOLDS WITH CAVEATS or FAILS.
