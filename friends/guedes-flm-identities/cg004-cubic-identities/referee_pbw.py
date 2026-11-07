"""Exact finite PBW rebuild from the definitions, no proposing-job imports.

Ordered U(su(2)) basis: nondecreasing generator words, degrees <= 3.
Commutative basis: matching monomials. Every map is built forwards, then
inverted as a 20 x 20 matrix over Q(i). Displayed expressions are only
loaded after construction of the maps; they do not define the products.
"""
import itertools as it
import json
import math
from functools import cache
from pathlib import Path
import sympy as s

I = s.I
R = s.Rational
x = s.symbols('X1:4')
p = s.symbols('p1:4')
y = s.symbols('Y1:4')
root = Path(__file__).resolve().parent


def eps(i, j, k):
    return int(s.LeviCivita(i, j, k))


@cache
def normal(word):
    """Adjacent exchange ab = ba + 2i epsilon_abc c, recursively."""
    for pos in range(len(word) - 1):
        a, b = word[pos:pos + 2]
        if a > b:
            out = dict(normal(word[:pos] + (b, a) + word[pos + 2:]))
            for c in range(3):
                if not eps(a, b, c):
                    continue
                for w, v in normal(word[:pos] + (c,) + word[pos + 2:]).items():
                    out[w] = s.expand(out.get(w, 0) + 2 * I * eps(a, b, c) * v)
            return {w: v for w, v in out.items() if v != 0}
    return {word: s.Integer(1)}


basis = [w for n in range(4) for w in it.combinations_with_replacement(range(3), n)]
row = {w: n for n, w in enumerate(basis)}


def vector(u):
    v = s.zeros(len(basis), 1)
    for w, c in u.items():
        v[row[w]] += c
    return v


def monomial(w):
    return s.prod(x[j] for j in w)


@cache
def symmetrize_word(w):
    out = {}
    for perm in it.permutations(w):
        for v, c in normal(perm).items():
            out[v] = out.get(v, 0) + c / math.factorial(len(w))
    return {v: s.expand(c) for v, c in out.items() if c != 0}


def symmetrize_polynomial(f):
    out = s.zeros(len(basis), 1)
    for powers, c in s.Poly(s.expand(f), *x).terms():
        w = tuple(j for j, n in enumerate(powers) for _ in range(n))
        out += c * vector(symmetrize_word(w))
    return out


def lap(f):
    return sum(s.diff(f, z, 2) for z in x)


# Derive the quadratic Duflo factor from the adjoint matrix:
# sinh(A/2)/(A/2) = Id + A^2/24 + ...;
# sqrt(det(...)) = 1 + tr(A^2)/48 + ... .
adj = s.Matrix(3, 3, lambda k, j: sum(2 * I * x[i] * eps(i, j, k) for i in range(3)))
duflo_quadratic = s.expand(s.trace(adj**2) / 48)
assert duflo_quadratic == sum(z*z for z in x) / 6

# FLM forward map is extracted from exp(i (asin|p|/|p|) p.Y).
# asin(r)/r = 1+r^2/6+...; terms beyond p-degree 3 cannot contribute.
radial = 1 + sum(z*z for z in p) / 6
dot = sum(a*b for a, b in zip(p, y))
flm_generating = s.Poly(s.expand(sum((I * radial * dot)**n / math.factorial(n)
                                    for n in range(4))), *p)


def flm_forward(fword):
    powers = tuple(fword.count(j) for j in range(3))
    c = flm_generating.coeff_monomial(powers)
    c *= math.prod(math.factorial(n) for n in powers) / I**len(fword)
    return symmetrize_polynomial(s.expand(c).subs(dict(zip(y, x))))


S = s.Matrix.hstack(*(vector(symmetrize_word(w)) for w in basis))
D = s.Matrix.hstack(*(symmetrize_polynomial(monomial(w) + lap(monomial(w))/6) for w in basis))
F = s.Matrix.hstack(*(flm_forward(w) for w in basis))
forward = {'symmetric': S, 'duflo': D, 'flm': F}
inverse = {name: q.inv() for name, q in forward.items()}
for name in forward:
    assert forward[name] * inverse[name] == s.eye(len(basis))


def inverse_word(name, word):
    v = vector(normal(tuple(word)))
    coefficients = inverse[name] * v
    # Verify the entire operator word in U(g), not a particular representation.
    assert forward[name] * coefficients == v
    return s.expand(sum(c * monomial(w) for c, w in zip(coefficients, basis)))


transcript = json.loads((root / 'source_transcription.json').read_text())['maps']


def displayed(name, word):
    spec = transcript[name]
    i, j = word[:2]
    if len(word) == 2:
        return s.expand(x[i]*x[j] + I*sum(eps(i, j, m)*x[m] for m in range(3))
                        + R(spec['quadratic_constant'])*int(i == j))
    k = word[2]
    B = I * sum((eps(i,j,m)*x[k] + eps(i,k,m)*x[j] + eps(j,k,m)*x[i])*x[m]
                for m in range(3))
    return s.expand(x[i]*x[j]*x[k] + B
        + R(spec['cubic_delta_jk_i'])*int(j == k)*x[i]
        + R(spec['cubic_delta_ik_j'])*int(i == k)*x[j]
        + R(spec['cubic_delta_ij_k'])*int(i == j)*x[k])


results = {'method': 'Exact PBW normal ordering; independent forward quantization matrices',
           'basis_dimension': len(basis), 'duflo_j_half_degree_2': str(duflo_quadratic), 'maps': {}}
for name in forward:
    records = []
    counts = {}
    for n in [2, 3]:
        agree = 0
        for word in it.product(range(3), repeat=n):
            actual = inverse_word(name, word)
            printed = displayed(name, word)
            diff = s.expand(actual - printed)
            agree += int(diff == 0)
            records.append({'word': [j+1 for j in word], 'computed': str(actual),
                            'displayed': str(printed), 'computed_minus_displayed': str(diff)})
        counts[str(n)] = {'agree': agree, 'disagree': 3**n-agree, 'total': 3**n}
    # Check word commutators against the independently reconstructed quadratic.
    for i, j, k in it.product(range(3), repeat=3):
        lhs = inverse_word(name, (i,j,k)) - inverse_word(name, (j,i,k))
        rhs = 2*I*sum(eps(i,j,m)*inverse_word(name,(m,k)) for m in range(3))
        assert s.expand(lhs-rhs) == 0
    results['maps'][name] = {'counts': counts, 'words': records}

# Independent one-axis control, straight from the inverse plane waves.
t = s.symbols('t')
waves = {'symmetric': s.exp(I*t*x[0]),
         'duflo': (t/s.sin(t))*s.exp(I*t*x[0]),
         'flm': s.exp(I*s.sin(t)*x[0])}
results['one_axis_controls'] = {}
for name, wave in waves.items():
    series = s.series(wave, t, 0, 4).removeO().expand()
    cubic = s.expand(6*series.coeff(t,3)/I**3)
    assert cubic == inverse_word(name, (0,0,0))
    results['one_axis_controls'][name] = {'computed_cubic': str(cubic),
                                        'displayed_cubic': str(displayed(name,(0,0,0)))}
(root/'pbw_results.json').write_text(json.dumps(results, indent=2)+'\n')
print(json.dumps({name: r['counts'] for name, r in results['maps'].items()}, indent=2))
print('ONE AXIS:', results['one_axis_controls'])
print('Exact map roundtrips and word commutators: all passed.')
