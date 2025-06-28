from flask import Blueprint, request, jsonify, render_template
from app.services import image_codec, audio_codec, video_codec, stego
from werkzeug.utils import secure_filename
import os

main = Blueprint('main', __name__)
UPLOAD_FOLDER = 'static/uploads'

@main.route('/')
def home():
    return render_template("index.html")

# 🔏 Steganografi Gambar
@main.route('/encode-image', methods=['POST'])
def encode_image():
    image = request.files['image']
    message = request.form['message']
    result = stego.encode_lsb(image, message)
    return jsonify({"status": "success", "output_path": result})

@main.route('/decode-image', methods=['POST'])
def decode_image():
    image = request.files['image']
    message = stego.decode_lsb(image)
    return jsonify({"status": "success", "message": message})


# 🎵 Kompresi Audio
@main.route('/compress-audio', methods=['POST'])
def compress_audio():
    audio = request.files['audio']
    bitrate = request.form.get('bitrate', '64k')
    filename = secure_filename(audio.filename)
    input_path = os.path.join(UPLOAD_FOLDER, filename)
    output_path = os.path.join(UPLOAD_FOLDER, f"compressed_{filename}")

    audio.save(input_path)
    audio_codec.compress_audio(input_path, output_path, bitrate=bitrate)

    return jsonify({"status": "success", "output_path": output_path})

# 📹 Kompresi Video
@main.route('/compress-video', methods=['POST'])
def compress_video():
    video = request.files['video']
    bitrate = request.form.get('bitrate', '500k')
    filename = secure_filename(video.filename)
    input_path = os.path.join(UPLOAD_FOLDER, filename)
    output_path = os.path.join(UPLOAD_FOLDER, f"compressed_{filename}")

    video.save(input_path)
    video_codec.compress_video(input_path, output_path, bitrate=bitrate)

    return jsonify({"status": "success", "output_path": output_path})
