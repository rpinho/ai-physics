# Independent audit of the stated family

Write [n]=(q^n-q^-n)/(q-q^-1). I used the local matrices in source (2.1)
and coproduct E=E⊗1+K⊗E, F=F⊗K^-1+1⊗F. This gives the source's
two-site singlet v10-q v01. Tensor reversal relates the opposite convention.

For a source basis state b and increments a with sum a=r and
0<=a_i<=ell-b_i, expansion of the q-commuting coproduct summands gives

E^(r) v_b = sum_a q^(sum_{i<j} a_i a_j +
                           sum_i a_i sum_{j<i}(2b_j-ell))
                 product_i [ell-b_i choose a_i] v_(b+a).

This is regular at the specified root because all local denominators have
index <=ell<p=ell+2. The referee code implements this tensor expansion,
with its normalization also checked against repeated ordinary action for
the nonvanishing local factorials. It does not evaluate E^p/[p]! at the root.

Applying the expansion to the lowest tensor reproduces exactly the claimed
w_t coefficients. Generic quantum-binomial identities then give
E w_t=[t+1]w_(t+1), F w_t=[N-t+1]w_(t-1), K w_t=q^(2t-N)w_t.
These identities specialize because their individual coefficients are regular.

For odd ell>=3, p=ell+2 is odd, q=-exp(-i*pi/p) has exact order p,
m=(ell+1)/2>=2, N=ell(ell+3), and s=N/2=mp-1.
Both raising/lowering coefficients at s are [mp]=0; the integer weight is zero.
All coefficients defining w_s are nonzero: their quantum integers have indices
strictly below p. Thus this is a nonzero ordinary invariant for composite p too.

The generic divided-power product identity gives
E^(p)w_s=[s+p choose p]w_(s+p). Separate the unique vanishing numerator
factor [mp] and denominator [p]. Their ratio tends to m by differentiation.
Each remaining ratio [mp+j]/[j], 1<=j<p, tends to 1. Therefore the scalar
is m. Also s+p<=N and w_(s+p) is nonzero.

Every generically invariant fused column is killed by E^(p) generically.
Both that operator and the Jones–Wenzl projected columns are regular at this
root; consequently their product remains zero after specialization. This
separates w_s from the entire image. The proof does not assert a failure of
divided-power invariance, or of flat continuation of the generic invariant space.

Finite independent certification is in evidence/referee_results.json. Exact
annihilation supplies lower bounds; two finite-field ranks give matching upper
bounds over the number field. No modular nullity is assumed equal to a
characteristic-zero nullity without those exact lower bounds.
