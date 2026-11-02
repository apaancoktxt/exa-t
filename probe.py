import os, json, urllib.request
k = os.environ["EXAK"]
def post(p, body):
    r = urllib.request.Request("https://api.exa.ai"+p, data=json.dumps(body).encode(),
        headers={"content-type":"application/json","x-api-key":k})
    try:
        with urllib.request.urlopen(r, timeout=120) as x: return x.status, x.read().decode()
    except Exception as e:
        try: return getattr(e,"code",0), e.read().decode()[:400]
        except: return getattr(e,"code",0), str(e)[:200]

print("=== cari endpoint deep research pengganti ===")
for p in ["/deep-search", "/search/deep", "/agent", "/v1/deep-search"]:
    s,b = post(p, {"query":"test"})
    print(f"  {p:<20} -> {s}  {b[:100] if s!=200 else 'OK'}")
