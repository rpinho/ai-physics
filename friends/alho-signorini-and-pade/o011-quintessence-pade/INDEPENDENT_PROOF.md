# What the independent interval audit establishes

The mathematical target is the positive tracker of the source's dust/scalar
system, with p=1 or 1/10 and x=Omega_phi=17/25 at N=0. All finite-start
integrations are diagnostics; none initializes the rigorous enclosure.

Eliminating H from the source equations in REPORT.md gives
x_N=3(1-q A^2)x(1-x). With t=log(x), the two remaining equations are

f(A,B,x)=(2-q A^2)(B-A)/(2(1-q A^2)(1-x)),
g(A,B,x)=B/2-(q/p)AB^2/((1-q A^2)(1-x)).

The tracker tends to (A,B,x)=(1,1,0) in the past. Its existence and unique
positive branch also follow locally from the hyperbolic saddle: x has
positive eigenvalue k=6/(p+2); the A,B block has negative trace and positive
determinant. The source identifies this branch as its tracker orbit.

`interval_ref.py` reads the auxiliary rational a(x),b(x) as proposed data.
It asserts exactly a(0)=b(0)=1, builds r=(x a'-f(a,b,x),x b'-g(a,b,x)) with
exact rational polynomial arithmetic, and tests a box of radius delta=2e-7
on each of 2048 intervals covering 0<=x<=17/25. It checks positivity of A,B,
W=1-qA^2, and A<1.1; ||r||_2 < .1*delta; and negativity of the symmetric
Jacobian plus .1 times the identity (both diagonals negative, determinant
positive). Polynomial translation about interval midpoints is evaluated
with Arb enclosures, not floating estimates.

For e=(A-a,B-b), these inequalities give d||e||/dt <= -.1||e||+||r||.
The Euclidean delta sphere is strictly inward pointing. As x->0 both the
true tracker and auxiliary curve tend to (1,1), so e tends to zero. Starting
arbitrarily early inside the sphere proves the tube for every x>0 up to
17/25. This also extends the branch across this interval: its state remains
in a compact regular region and W stays positive.

For y=log((17/25)/x), integrate the auxiliary time map directly in x:
N_c(x)=integral_(17/25)^x [3(1-q a(s)^2)s(1-s)]^-1 ds.
This callback is rational and meromorphic. With Wmin=1-q*(1.1)^2,
D=q*delta*(2.2+delta), the true time lies within
y*D/[3*Wmin^2*(1-17/25)] of N_c(x).

The candidate's exact Padé P/Q is independently reproduced by referee.py.
All Q coefficients are positive and all P coefficients negative. Thus no
positive-axis pole exists, w/w_inf>0, and its R(T) is strictly increasing.
Validated bisection encloses the unique root R(T0)=17/8 in (1,3).
The rational removable singularity in (w/w_inf-1)/T is cancelled exactly.

Both time and log R quadratures use Acb at 192 bits. Integrators receive
exact dyadic endpoint midpoints. For an uncertain endpoint, an additional
real interval integrand bound times its radius encloses the displacement.
Callbacks contain no branch-dependent log, sqrt or absolute-value operation.
The callbacks are meromorphic; any interval containing a pole returns a
nonfinite value. Nonfinite or insufficiently narrow quadratures abort.

Each y cell has width 1/2048. A rigorous center value and a whole-cell
bound on |dN/dy| enclose the true time over the cell. Continuity gives
dlogR/dN=-3w, which encloses candidate density over the entire cell.
For L=log(Omega_m,candidate(N_true(y))/(1-x(y))), exact differentiation gives
L_y=(-w_candidate*Omega_phi,candidate/W_true-x)/(1-x).
The audit bounds |L| by its interval center magnitude plus half the cell
width times a whole-cell |L_y| bound. It continues until the entire last
time enclosure is earlier than -log(7). Monotonicity and adjoining cells
then cover every z in the closed target interval [0,6].

If the resulting uniform log bound is M, exp(M)-1 bounds the relative
Omega_m error and exp(M/2)-1 bounds the E error. The latter follows exactly
from dust conservation E^2=(8/25)exp(-3N)/Omega_m, with common present H0.
Arb inequalities compare these bounds directly with the claim's p-specific
limits. The audit also encloses published [1/1], normalization-only [1/1],
wCDM and LambdaCDM errors at the exact true x=2/5, proves that point lies
inside the redshift interval, and compares the control lower bounds with
the degree-6 uniform upper bounds.

This is an independently programmed rational/ball certificate with a written
ODE argument, not a proof-assistant formalization. It assumes the stated
dust/scalar equations. Exact arithmetic and the validated integration backend
are provided by python-flint 0.9.0; versions and reproduction files are retained.
