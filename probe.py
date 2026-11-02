import os, json, urllib.request
k = os.environ["EXAK"]
def post(p, body):
    r = urllib.request.Request("https://api.exa.ai"+p, data=json.dumps(body).encode(),
        headers={"content-type":"application/json","x-api-key":k})
    try:
        with urllib.request.urlopen(r, timeout=120) as x: return x.status, x.read().decode()
    except Exception as e:
        try: return getattr(e,"code",0), e.read().decode()[:300]
        except: return getattr(e,"code",0), str(e)[:200]

# 1. ambil halaman bug bounty langsung
s,b = post("/contents", {"urls":["https://docs.ticko.xyz/resources/ticko-bug-bounty"],"text":{"maxCharacters":15000}})
print("=== CONTENTS status:", s)
if s==200:
    d=json.loads(b)
    for r in d.get("results",[]):
        print(r.get("title"))
        print((r.get("text") or "")[:4000])
else:
    print(b[:300])

# 2. deep search konteks Ticko
s2,b2 = post("/search", {"query":"Ticko xyz bug bounty scope program","type":"deep","numResults":6,"contents":{"text":{"maxCharacters":2500}}})
print("\n=== DEEP SEARCH status:", s2)
if s2==200:
    d=json.loads(b2)
    for r in d.get("results",[]):
        print("-",r.get("title"),"|",r.get("url"))
        print("  ",(r.get("text") or "")[:400].replace("\n"," "))
