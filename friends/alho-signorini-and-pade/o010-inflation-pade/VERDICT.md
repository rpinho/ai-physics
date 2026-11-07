HOLDS WITH CAVEATS
Referee: gpt-6.1-sol
The n=20 <0.000067% bound is correct for the paper's relative Hubble error
at the same first q=0 endpoint on the pure-scalar attractor. All six rows pass.
The primary PDF confirms Artur Alho, Juliette Hell and Claes Uggla as authors.

I derived the transformed ODE from the paper, rebuilt the series and selected
Padé coefficients, checked all 279 accepted curves with exact rational Bernstein
bounds, and audited comparison at the singular origin. Original-variable
integrations provide a separate diagnostic. No submitted executable was imported.
Code, exact results, logs and the public source are retained here; see AUDIT.md.

The printed 31% matches a tangency curve, not the literal formula cited by
Table 1. Literal source controls are stronger and are still beaten.
I also checked the omitted source (81)+(76b): n=20 error is <0.049385789816%,
stronger than the claim's tested 0.386567606987% source control.

The decisive trivial control is source (81) with ordinary Hubble [4/4]:
its certified error is <0.000004789186%, about 14 times better than the claimed
inverse [4/4], with eight coefficients in each series. These are my control
calculations, not a previously printed numerical result. See source81_controls.json.

There is no empirical hold-out. Degrees were selected using certified endpoint
errors; coefficients match the ODE exactly. Added exponents are constructed cases,
not untouched validation. No trajectory-wide or uniform-in-n result was checked.

Relative to the paper, the contribution is an inverse-variable parametrization,
finite-n endpoint rows and exact differential-barrier certificates. Higher-degree
Padé and variable changes are already proposed there; Álvarez–Medina (2024),
arXiv:2304.05650, also covers adapted monomial expansions and Padé summation.

Strongest author objection: the paper deliberately displayed simple low-order
curves; extending its own prescription already surpasses this endpoint accuracy.
The certificate survives; it does not establish an advantage over higher-order source controls.

NEXT BAR: give a certified error-versus-degree/cost table for inverse Padé and
both source Hubble prescriptions, including equation (81) with [4/4], on all six n.
