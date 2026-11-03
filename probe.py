import os, json, urllib.request
k=os.environ["EXAK"]
def post(p,b):
    r=urllib.request.Request("https://api.exa.ai"+p,data=json.dumps(b).encode(),
        headers={"content-type":"application/json","x-api-key":k})
    try:
        with urllib.request.urlopen(r,timeout=90) as x: return x.status,x.read().decode()
    except Exception as e:
        try: return getattr(e,"code",0), e.read().decode()[:300]
        except: return getattr(e,"code",0),str(e)[:200]

# 1. contents dengan livecrawl always - crawler Exa dari IP lain
s,b = post("/contents", {"urls":[
    "https://api.testnet.ticko.xyz/v1/market/coins",
    "https://docs.ticko.xyz/testnet-guide",
    "https://testnet.ticko.xyz/"
],"text":{"maxCharacters":3000},"livecrawl":"always"})
print("CONTENTS",s)
if s==200:
    d=json.loads(b)
    for r in d.get("results",[]):
        print(" -",r.get("url"),"| status:",r.get("status") if "status" in r else "?")
        print("  ",(r.get("text") or "")[:300].replace("\n"," "))
