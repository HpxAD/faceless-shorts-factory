from moviepy import *
import math

video = VideoFileClip("input/Upload.mp4")
audio = AudioFileClip("input/dof.mp3")

duration = min(30, video.duration, audio.duration)
video = video.subclipped(0, duration)
audio = audio.subclipped(0, duration)

# ---------- 16:9 -> 9:16 ----------
w, h = video.w, video.h
crop_w = h * 9 / 16
video = video.cropped(
    x1=(w - crop_w) / 2,
    width=crop_w
).resized(width=1080)

# ---------- Zack-style punch zoom ----------
def zoom(t):
    return 1 + 0.08 * abs(math.sin(t * 1.4))

video = video.resized(lambda t: zoom(t))

# ---------- Intro ----------
intro = (
    TextClip(
        text="⚡ Internet Ka Jugaad",
        font_size=78,
        color="white",
        stroke_color="black",
        stroke_width=3
    )
    .with_duration(0.8)
    .with_position("center")
)

# ---------- Big captions ----------
captions = [
("STOP!",0,1),
("CAMERA BLUR?",1.2,2.2),
("DOF SIMULATOR",2.5,4.5),
("APERTURE",5,6.3),
("BLUR LIVE",8,9.5),
("LENS CHANGE",12,13.8),
("SAVE KAR LO",duration-2.5,duration)
]

layers=[video,intro]

for txt,s,e in captions:
    color="#FACC15" if txt in ["STOP!","DOF SIMULATOR","SAVE KAR LO"] else "white"
    layers.append(
        TextClip(
            text=txt,
            font_size=90,
            color=color,
            stroke_color="black",
            stroke_width=4
        )
        .with_start(s)
        .with_duration(e-s)
        .with_position(("center",140 if s<duration-3 else "bottom"))
    )

final = CompositeVideoClip(layers, size=(1080,1920)).with_audio(audio)

final.write_videofile(
    "output/short.mp4",
    fps=30,
    codec="libx264",
    audio_codec="aac",
    preset="ultrafast"
)
