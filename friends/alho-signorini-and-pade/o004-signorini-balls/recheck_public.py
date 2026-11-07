from pathlib import Path
from urllib.request import Request, urlopen
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import hashlib,json
initial=json.loads(Path('public_receipts.json').read_text())
selected=[r for r in initial if r['name'] in ['paper2020.html','paper2021.html','github_repositories.json','github_issues.json','github_code.json'] or r['name'].endswith('.md')]
def fetch(r):
 receipt=dict(name=r['name'],url=r['url'],utc=datetime.now(timezone.utc).isoformat())
 try:
  with urlopen(Request(r['url'],headers={'User-Agent':'IndependentMathReferee/1.0'}),timeout=30) as f:
   data=f.read(3000000);receipt['status']=f.status
  receipt.update(sha256=hashlib.sha256(data).hexdigest(),bytes=len(data))
  receipt['same_as_initial']=receipt['sha256']==r.get('sha256')
  if r['name'].endswith('.json'):receipt['total_count']=json.loads(data).get('total_count')
  if r['name'].endswith('.md'):receipt['Signorini_mentions']=data.lower().count(b'signorini')
 except Exception as e:receipt['error']=str(e)
 return receipt
with ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(fetch,selected))
Path('recheck_receipts.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2),flush=True)
