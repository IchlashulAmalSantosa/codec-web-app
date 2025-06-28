FROM python:3.12-slim

# Install sistem dependencies (libGL, ffmpeg, dll)
RUN apt-get update && apt-get install -y \
    libgl1 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy seluruh file ke container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Jalankan aplikasi Flask
CMD ["python", "app.py"]
