# Independent transcription from fresh PDFs

Viewed rendered journal PDF pages 24--26 (journal labels 083508-23--25).
The FLM cubic is on journal page 25, one page beyond CLAIM.md's page range.
Fresh arXiv v2 shows the same formulas (PDF pages 26, 27, 29).

Write `x=(X1,X2,X3)`, `e(i,j,k)=epsilon_ijk`, `d(i,j)=delta_ij`,
`A_ij = i sum_m e(i,j,m) x_m` and
`B_ijk = i sum_m [e(i,j,m)x_k+e(i,k,m)x_j+e(j,k,m)x_i]x_m`.
Repeated `m` is summed; external `i,j,k` are arbitrary fixed indices.
Juxtaposition on the right means ordinary commuting polynomial product.

Displayed lists:

| Map | Quadratic | Cubic |
| --- | --- | --- |
| Symmetric | x_i x_j + A_ij | x_i x_j x_k + B_ijk + (2/3)d(j,k)x_i - (1/3)d(i,k)x_j + (2/3)d(i,j)x_k |
| Duflo | x_i x_j + A_ij - d(i,j)/3 | x_i x_j x_k + B_ijk + (1/3)d(j,k)x_i - (2/3)d(i,k)x_j + (1/3)d(i,j)x_k |
| FLM | x_i x_j + A_ij | x_i x_j x_k + B_ijk + d(j,k)x_i - d(i,k)x_j + d(i,j)x_k |

Definitions used for the independent rebuild:

- Section 3, journal Eq. (28): Q(f star g)=Q(f)Q(g).
- Section 5, Eq. (54): words equal Q^-1(hatX_i ... hatX_k);
  projection does not affect derivatives at identity (explicitly stated next page).
- SU(2) basis: Pauli matrices, sigma_i sigma_j=d(i,j)I+i e(i,j,k)sigma_k;
  hence [hatX_i,hatX_j]=2i e(i,j,k)hatX_k.
- S averages all permutations. Thus S(x_1^n)=hatX_1^n.
- D=S o j^(1/2)(partial); j(X)=(sinh|X|/|X|)^2.
  Therefore through degree three D=S o (1+Delta/6).
- D^-1(exp(i k.hatX))=(|k|/sin|k|)exp(i k.x).
- Q_FLM(exp(i p.x))=exp(i (asin|p|/|p|)p.hatX), journal Eq. (68).
  Its inverse plane wave is exp(i (sin|k|/|k|)k.x).

No proposing-job search or verifier code has been read or imported.
