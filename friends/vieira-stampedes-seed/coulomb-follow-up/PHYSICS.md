The seed is an origin-normalized radial Coulomb scattering wave in two dimensions. This is an exact auxiliary Schrödinger interpretation, with checkable consequences; a microscopic Coulomb particle in the gauge theory has not been derived.

For real $L>0$, divide the equation by $L$:
\[
\left[-\partial_L^2-L^{-1}\partial_L+\frac{B}{L}\right]\tau=\pi^2\tau.
\]
The first two terms are the two-dimensional radial Laplacian in the zero-angular-momentum sector. In units \(\hbar^2/(2m)=1\), \(L\) is radius, \(B\) is Coulomb strength, and energy is fixed at \(\pi^2\). Positive \(B\) is repulsive. This is the usual planar \(1/r\) potential, not the logarithmic electrostatic potential of strictly two-dimensional electromagnetism. The regular origin condition gives \(\tau(0)=1,\ \tau'(0)=B\). Equivalently, \(u=\sqrt L\tau\) obeys
\[
-u''+\left(\frac B L-\frac1{4L^2}\right)u=\pi^2u;
\]
the inverse-square term cannot be discarded to call this three-dimensional hydrogen.

There is also a direct octagon meaning: a bridge insertion is a fermionic boundary insertion, and \(O_1/O_0\) is a dressed Bessel boundary mode. The published Fredholm-resolvent equation reduces at that boundary to this ODE. Thus the scattering wave describes an auxiliary mode of the existing determinant, not an independently postulated microscopic Hamiltonian. See [the derivation](DERIVATION.md) and [Kostov–Petkova, Eqs.(1.8), (2.34)–(2.41)](https://arxiv.org/abs/2102.05000).

The intuition is useful. Increasing the repulsion delays oscillations. If \(r_n(B)\) is a positive zero, exact differentiation gives
\[
\frac{dr_n}{dB}=\frac{\int_0^{r_n}\tau(L,B)^2\,dL}{r_n\tau_L(r_n,B)^2}>0.
\]
For fixed \(B\), put \(\eta=B/(2\pi)\). Standard [Coulomb asymptotics](https://dlmf.nist.gov/33.11), continued to angular index \(-1/2\), give
\[
\tau=\frac{\sqrt{1+e^B}}{\pi\sqrt L}
\sin\!\left[\pi L-\eta\log(2\pi L)+\frac\pi4+\arg\Gamma(\tfrac12+i\eta)\right]
+O_B(L^{-3/2}).
\]
The logarithm is the Coulomb phase shift. The Fermi-looking amplitude follows from Gamma normalization; it does not establish a thermal stampede.

Why did Stampedes II find a Bessel function? At fixed \(x=LB\), sending \(B\to\infty\) changes the equation to \(xf''+f'-f+(\pi^2/B^2)xf=0\), hence \(f\to I_0(2\sqrt x)\). The energy correction disappears. Retaining it reproduces the printed \(\pi^2\) and \(\pi^4\) corrections in Stampedes I Eq.(93)/published Eq.(E.7), independently checked here. Those printed coefficients confirm the local expansion; the papers contain no large-\(L\) zero data. The zeros and asymptotics are consequences of the projected seed, not established zeros or asymptotics of the full finite-cross-ratio octagon. A direct probability interpretation fails because this wave changes sign. No microscopic spin-chain or new Painlevé explanation was established.
