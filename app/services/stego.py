import os
from PIL import Image

def encode_lsb(image_file, message):
    image = Image.open(image_file)

    # Pastikan gambar dalam mode RGB
    if image.mode != 'RGB':
        image = image.convert('RGB')

    encoded = image.copy()
    binary = ''.join(format(ord(i), '08b') for i in message) + '1111111111111110'  # EOF
    pixels = encoded.load()

    i = 0
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            if i < len(binary):
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary[i])
                pixels[x, y] = (r, g, b)
                i += 1

    # Pastikan folder tujuan ada
    output_dir = 'static/uploads'
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, 'encoded_image.png')
    encoded.save(output_path)
    return output_path

def decode_lsb(image_file):
    image = Image.open(image_file)

    # Pastikan gambar dalam mode RGB
    if image.mode != 'RGB':
        image = image.convert('RGB')

    binary_data = ""
    pixels = image.load()

    for y in range(image.size[1]):
        for x in range(image.size[0]):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)

    # EOF marker untuk menentukan akhir pesan
    eof_marker = '1111111111111110'
    if eof_marker in binary_data:
        binary_data = binary_data.split(eof_marker)[0]
    else:
        return "❌ Pesan tidak ditemukan atau tidak valid."

    # Konversi dari biner ke teks
    message = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        message += chr(int(byte, 2))

    return message
