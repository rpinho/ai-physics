"""Report the physically derived radius conversion; run on pod."""
from pathlib import Path
import json,math
rows=json.loads(Path('independent_baseline.json').read_text())
result={'relation':'s = r sqrt(4 pi G K^2 / (3 kappa))',
 'unit_case':'G=K=kappa=1',
 'warning':'Figure 8 labels Radius without a stated numerical unit convention in the nearby text. The unit-case conversion below visually matches its approximate surfaces; that convention is an inference, not a published certified number.',
 'radii':[{'nu':r['nu'],'rtol':r['rtol'],'R_s':r['R_s'],
  'r_if_G_K_kappa_are_1':r['R_s']*math.sqrt(3/(4*math.pi))} for r in rows]}
Path('figure_units.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
