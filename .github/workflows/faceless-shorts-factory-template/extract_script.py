import json
with open("output.json",encoding="utf-8") as f:
    data=json.load(f)
if "error" in data:
    raise SystemExit(data["error"])
text=data["candidates"][0]["content"]["parts"][0]["text"]
open("script.txt","w",encoding="utf-8").write(text)
print(text)
