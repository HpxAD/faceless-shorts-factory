
import os
import time
import requests
import json

api = os.environ["GEMINI_API_KEY"]

site = open("websites.txt", encoding="utf-8").read().splitlines()[0]

os.makedirs("output", exist_ok=True)

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent"

payload = {
    "contents": [{
        "parts": [{
            "text": f"Write a 30-second YouTube Shorts script about {site}. Hook first. End with 'Save this for later.'"
        }]
    }]
}

for attempt in range(5):
    try:
        r = requests.post(
            url,
            headers={
                "x-goog-api-key": api,
                "Content-Type": "application/json"
            },
            json=payload,
            timeout=60
        )

        data = r.json()

        print(json.dumps(data, indent=2))

        if "error" in data:
            raise Exception(data["error"]["message"])

        if "candidates" not in data:
            raise Exception("No candidates returned from Gemini")

        text = data["candidates"][0]["content"]["parts"][0]["text"]

        with open("output/script.txt", "w", encoding="utf-8") as f:
            f.write(text)

        print("Saved output/script.txt")
        break

    except Exception as e:
        print(f"Attempt {attempt+1}/5 failed: {e}")
        if attempt == 4:
            raise
        time.sleep(5)
