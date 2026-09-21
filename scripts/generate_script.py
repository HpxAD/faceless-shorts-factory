
import os
import requests

api = os.environ["GEMINI_API_KEY"]

site = open("websites.txt", encoding="utf-8").read().splitlines()[0]

os.makedirs("output", exist_ok=True)

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent"

r = requests.post(
    url,
    headers={
        "x-goog-api-key": api,
        "Content-Type": "application/json"
    },
    json={
        "contents": [{
            "parts": [{
                "text": f"Write a 30-second YouTube Shorts script about {site}. Hook first. End with 'Save this for later.'"
            }]
        }]
    }
)

data = r.json()
text = data["candidates"][0]["content"]["parts"][0]["text"]

with open("output/script.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Saved output/script.txt")
