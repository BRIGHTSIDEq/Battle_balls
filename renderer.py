import moviepy.editor as mp

def export_video(frames, fps, voice_file, output="battle.mp4"):
    clips = [mp.ImageClip(frame).set_duration(1 / fps) for frame in frames]
    video = mp.concatenate_videoclips(clips, method="compose")

    audio = mp.AudioFileClip(voice_file)
    video = video.set_audio(audio)

    video.write_videofile(output, fps=fps)
