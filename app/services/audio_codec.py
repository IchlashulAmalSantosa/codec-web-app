from pydub import AudioSegment
import os

def compress_audio(input_path, output_path, bitrate="64k"):
    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, format="mp3", bitrate=bitrate)
    return output_path

def convert_audio_format(input_path, output_path, format="wav"):
    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, format=format)
    return output_path
