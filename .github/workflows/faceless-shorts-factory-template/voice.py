import asyncio, edge_tts
text=open("script.txt",encoding="utf-8").read()
async def main():
    c=edge_tts.Communicate(text=text,voice="en-US-AvaMultilingualNeural")
    await c.save("script.mp3")
asyncio.run(main())
