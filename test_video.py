import os

from python_video import frames_to_video, video_frames, video_info

video = "v_BaseballPitch_g08_c01.avi"

print("video_info()")
for reader in "opencv", "moviepy":
    print(f"    {reader}: {video_info(video)}")

print("video_frames()")
for reader in "opencv", "moviepy", "pyav", "decord":
    count = sum(1 for frame in video_frames(video, reader=reader))

    print(f"    {reader}: {count} frames")

print("frames_to_video()")
frames = list(video_frames(video, reader="decord"))
info = video_info(video)

for writer in "opencv", "moviepy":
    frames_to_video(frames, target=f"{writer}.mp4", writer=writer, fps=info["fps"])

test_videos = [f"{writer}.mp4" for writer in ("opencv", "moviepy")]

for test_video in test_videos:
    print(f"    {test_video}: {video_info(test_video)}")
    os.remove(test_video)
