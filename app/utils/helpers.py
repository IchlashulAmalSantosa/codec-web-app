import os
import time

def generate_filename(extension):
    timestamp = int(time.time())
    return f"{timestamp}.{extension}"

def allowed_file(filename, extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extensions
