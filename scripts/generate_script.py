
import os
import json
import requests

API_KEY = os.environ["GEMINI_API_KEY"]

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

payload = {
    "contents": [{
        "parts": [{
            "text": "Write a 30-second YouTube Shorts script about one useful AI website. Include Hook, Demo, CTA."
        }]
    }]
}

r = requests.post(url, json=payload, timeout=60)

print("Status:", r.status_code)

data = r.json()

# Save the full response for debugging
with open("response.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

if "candidates" not in data:
    raise Exception(f"Gemini Error: {json.dumps(data, indent=2)}")

text = data["candidates"][0]["content"]["parts"][0]["text"]

os.makedirs("output", exist_ok=True)

with open("output/script.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Script created.")
