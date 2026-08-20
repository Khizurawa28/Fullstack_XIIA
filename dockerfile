# 1. gunakan base image resmi python versi
FROM python:3.12-slim

# 2. lembar kerja
WORKDIR /app

# 3. salin requirements text
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. menyalin seluruh code di komputer lokal
COPY . .

# 5. buka port 5000
EXPOSE 5000

# 6. jalankan otomatis perintah utama
CMD ["python", "app.py"]