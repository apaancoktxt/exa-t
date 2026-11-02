import os, json, urllib.request
k = os.environ["EXAK"]
def post(p, body):
    r = urllib.request.Request("https://api.exa.ai"+p, data=json.dumps(body).encode(),
        headers={"content-type":"application/json","x-api-key":k})
    try:
        with urllib.request.urlopen(r, timeout=45) as x: return x.status, x.read().decode()
    except Exception as e: return getattr(e,"code",0), str(e)[:300]

# uji tiap type yang didokumentasikan
for t in ["auto","neural","fast","deep","keyword","hybrid"]:
    s,b = post("/search", {"query":"test query","numResults":1,"type":t})
    ok = "OK" if s==200 else f"FAIL({s})"
    print(f"search.type={t:<8} -> {ok}")

# contents dengan berbagai model
for m in ["exa","exa-fast","always_exa"]:
    body={"ids":["https://example.com"],"text":{"maxCharacters":200},"livecrawl":"never" if m!="exa-fast" else "always"}
    s,b = post("/contents", body)
    print(f"contents({m}) -> {s}")
