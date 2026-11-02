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

qs = [
 "Ticko xyz bug bounty program scope rewards severity",
 "Ticko bug bounty hackerone immunefi ticko.xyz",
 "site:docs.ticko.xyz bug bounty",
]
for q in qs:
    s,b = post("/search", {"query":q,"type":"neural","numResults":8,
                           "contents":{"text":{"maxCharacters":3000}}})
    print(f"\n### Q: {q}  [{s}]")
    if s==200:
        d=json.loads(b)
        for r in d.get("results",[]):
            print("-", r.get("title"), "|", r.get("url"))
            t=(r.get("text") or "").replace("\n"," ")[:600]
            if t: print("  ", t)
