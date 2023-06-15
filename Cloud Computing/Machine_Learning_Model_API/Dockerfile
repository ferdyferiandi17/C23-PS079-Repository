# Menggunakan base image Python official
FROM python:3.9

# Menentukan working directory di dalam container
WORKDIR /app

# Menyalin file requirements.txt ke dalam container
COPY requirements.txt .

# Menginstal dependensi yang diperlukan
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin file-file aplikasi ke dalam container
COPY static/ static/
COPY apps.py .
COPY acnegra_model.h5 .

# Menjalankan perintah untuk menjalankan aplikasi Flask
CMD ["python", "apps.py"]