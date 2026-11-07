"""Independent exact plane-wave differentiation using explicit Pauli matrices.

No PBW routines or forward-map code is imported. Work in Q(i)[t1,...,tn]/
(t1^2,...,tn^2), so the coefficient t1...tn is the exact mixed derivative.
Products of exp(i ta sigma_a) are exactly products (Id+i ta sigma_a) in
this ring. Scalar and vector parts recover SU(2) coordinates without BCH.
"""
import itertools
import json
import math
from pathlib import Path
import sympy as s

root = Path(__file__).resolve().parent
I = s.I
x = s.symbols('X1:4')


def add(*args):
    out = {}
    for a in args:
        for k, v in a.items():
            out[k] = s.expand(out.get(k, 0) + v)
    return {k: v for k, v in out.items() if v != 0}


def scale(a, c):
    return {k: s.expand(c*v) for k, v in a.items() if c*v != 0}


def mul(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            if ka & kb:
                continue
            k = ka | kb
            out[k] = s.expand(out.get(k, 0) + va*vb)
    return {k: v for k, v in out.items() if v != 0}


def mmul(a, b):
    return [[add(*(mul(a[r][m], b[m][c]) for m in range(2)))
             for c in range(2)] for r in range(2)]


def exponential(a, degree):
    assert a.get(0, 0) == 0
    out = {0: s.Integer(1)}
    power = {0: s.Integer(1)}
    for n in range(1, degree+1):
        power = mul(power, a)
        out = add(out, scale(power, s.Rational(1, math.factorial(n))))
    return out


pauli = [s.Matrix([[0,1],[1,0]]), s.Matrix([[0,-I],[I,0]]), s.Matrix([[1,0],[0,-1]])]
results = {'method': 'Explicit 2x2 Pauli products and independent exact nilpotent-ring differentiation',
           'maps': {k: [] for k in ['symmetric','duflo','flm']}}
reference = json.loads((root/'pbw_results.json').read_text())
lookups = {name: {tuple(r['word']): r for r in data['words']}
           for name, data in reference['maps'].items()}

for n in [2,3]:
    for word in itertools.product(range(3), repeat=n):
        g = [[{0:s.Integer(1)},{}],[{},{0:s.Integer(1)}]]
        for position, axis in enumerate(word):
            factor = [[add(({0:s.Integer(1)} if r == c else {}),
                           {1 << position: I*pauli[axis][r,c]})
                       for c in range(2)] for r in range(2)]
            g = mmul(g, factor)
        scalar = scale(add(g[0][0],g[1][1]),s.Rational(1,2))
        vector = []
        for sigma in pauli:
            tr = add(*(scale(g[c][r],sigma[r,c]) for r in range(2) for c in range(2)))
            vector.append(scale(tr,1/(2*I)))
        p2 = add(*(mul(a,a) for a in vector))
        assert add(mul(scalar,scalar),p2) == {0:s.Integer(1)}
        # p = sin|k| k/|k|; inverse k = (asin|p|/|p|)p.
        # Up to degree 3, asin(r)/r = 1 + r^2/6.
        amplitude = add({0:s.Integer(1)},scale(p2,s.Rational(1,6)))
        k = [mul(amplitude,a) for a in vector]
        S_phase = scale(add(*(scale(a,z) for a,z in zip(k,x))),I)
        F_phase = scale(add(*(scale(a,z) for a,z in zip(vector,x))),I)
        waves = {'symmetric': exponential(S_phase,n),
                 'duflo': mul(amplitude,exponential(S_phase,n)),
                 'flm': exponential(F_phase,n)}
        for name, wave in waves.items():
            actual = s.expand(wave.get((1 << n)-1,0)/I**n)
            assert not actual.has(s.Float)
            key = tuple(a+1 for a in word)
            ref = lookups[name][key]
            assert s.expand(actual-s.sympify(ref['computed'])) == 0, (name,key,actual,ref)
            results['maps'][name].append({'word':key,'computed':str(actual),
                'matches_PBW':True,
                'computed_minus_displayed':str(s.expand(actual-s.sympify(ref['displayed'])))})

# Fit the discrepancy to the four rotation-covariant tensors instead of
# assuming the discrepancy asserted in CLAIM.md.
a,b,c,d = s.symbols('a b c d')
for name, records in results['maps'].items():
    equations = []
    for rec in records:
        if len(rec['word']) != 3:
            continue
        i,j,k = [z-1 for z in rec['word']]
        candidate = (a*int(j==k)*x[i]+b*int(i==k)*x[j]+c*int(i==j)*x[k]
                     +d*I*s.LeviCivita(i,j,k))
        residual = s.Poly(s.expand(s.sympify(rec['computed_minus_displayed'])-candidate),*x)
        equations.extend(residual.coeffs())
    fit = s.solve(equations,[a,b,c,d],dict=True)
    assert len(fit)==1
    results.setdefault('discrepancy_tensor_coefficients',{})[name] = {
        str(z): str(fit[0][z]) for z in [a,b,c,d]}
results['tensor_order'] = ['delta_jk X_i','delta_ik X_j','delta_ij X_k','i epsilon_ijk']
results['verified_words'] = sum(len(v) for v in results['maps'].values())
(root/'plane_wave_results.json').write_text(json.dumps(results,indent=2)+'\n')
print('Independent plane waves agree with PBW for',results['verified_words'],'map/word cases.')
print('Computed-minus-printed tensor coefficients:',results['discrepancy_tensor_coefficients'])
