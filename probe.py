import os, json, urllib.request
k = os.environ["EXAK"]
def post(p, body=None):
    data = json.dumps(body).encode() if body is not None else b""
    r = urllib.request.Request("https://api.exa.ai"+p, data=data,
        headers={"content-type":"application/json","x-api-key":k})
    try:
        with urllib.request.urlopen(r, timeout=60) as x: return x.status, x.read().decode()
    except Exception as e:
        try: return getattr(e,"code",0), e.read().decode()[:400]
        except: return getattr(e,"code",0), str(e)[:300]

# 1. endpoint answer - cek model field
for body in [
    {"query":"what is a bitcoin covenant","text":True},
    {"query":"what is a bitcoin covenant","model":"exa"},
    {"query":"what is a bitcoin covenant","model":"exa-pro"},
]:
    s,b = post("/answer", body)
    ok = s==200
    print(f"/answer model={body.get('model','(default)')} -> {s}")
    if ok:
        try:
            d=json.loads(b)
            print("   keys:", list(d.keys()))
            print("   answer:", (d.get("answer") or "")[:200])
            print("   cost:", d.get("costDollars"))
        except: print("   raw:", b[:200])
    else:
        print("   err:", b[:200])
