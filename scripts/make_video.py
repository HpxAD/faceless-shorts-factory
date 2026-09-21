
import os
from moviepy import ColorClip, AudioFileClip

os.makedirs("output", exist_ok=True)

audio = AudioFileClip("output/voice.mp3")

video = ColorClip(
    size=(1080, 1920),
    color=(20, 20, 20),
    duration=audio.duration
)

video = video.with_audio(audio)

video.write_videofile(
    "output/short.mp4",
    fps=30
)

print("Saved output/short.mp4")
