from moviepy.editor import VideoFileClip
import os

def compress_video(input_path, output_path, bitrate="500k"):
    clip = VideoFileClip(input_path)
    clip.write_videofile(output_path, bitrate=bitrate, codec='libx264')
    return output_path

def extract_audio(input_path, output_audio_path):
    clip = VideoFileClip(input_path)
    clip.audio.write_audiofile(output_audio_path)
    return output_audio_path
