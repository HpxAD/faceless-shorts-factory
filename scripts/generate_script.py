
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

response = requests.post(url, json=payload, timeout=60)

print("Status:", response.status_code)

data = response.json()

# Save the full API response
with open("response.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

# Stop and show the real error instead of KeyError
if "candidates" not in data:
    raise Exception(json.dumps(data, indent=2))

text = data["candidates"][0]["content"]["parts"][0]["text"]

os.makedirs("output", exist_ok=True)

with open("output/script.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Script created.")
