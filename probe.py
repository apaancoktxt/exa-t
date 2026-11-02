import os, json, urllib.request
k = os.environ["EXAK"]
def post(p, body):
    r = urllib.request.Request("https://api.exa.ai"+p, data=json.dumps(body).encode(),
        headers={"content-type":"application/json","x-api-key":k})
    try:
        with urllib.request.urlopen(r, timeout=90) as x: return x.status, x.read().decode()
    except Exception as e:
        try: return getattr(e,"code",0), e.read().decode()[:300]
        except: return getattr(e,"code",0), str(e)[:200]

print("=== /research (deep research) ===")
for body in [
    {"query":"bitcoin covenants overview","model":"exa-research-fast"},
    {"query":"bitcoin covenants overview","model":"exa-research"},
    {"query":"bitcoin covenants","model":"exa-research-pro"},
]:
    s,b=post("/research",body)
    print(f"  {body['model']:<22} -> {s}")
    if s==200:
        d=json.loads(b); print("     keys:",list(d.keys())[:6])
    else: print("     err:",b[:160])
