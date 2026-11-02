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

# coba ambil tweet
for u in ["https://x.com/shelleymaeph/status/2116792232925913166"]:
    s,b = post("/contents", {"urls":[u],"text":{"maxCharacters":4000},"livecrawl":"always"})
    print("TWEET",s)
    if s==200:
        d=json.loads(b)
        for r in d.get("results",[]):
            print("title:",r.get("title"))
            print("text:",(r.get("text") or "")[:1500])
    else: print(b[:250])
