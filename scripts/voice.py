
import os
import asyncio
import edge_tts

os.makedirs("output", exist_ok=True)

text = open("output/script.txt", encoding="utf-8").read()

async def main():
    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-AvaMultilingualNeural"
    )
    await communicate.save("output/voice.mp3")

asyncio.run(main())

print("Saved output/voice.mp3")
