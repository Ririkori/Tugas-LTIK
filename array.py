# Nama: Kori'ah 
# kelas: 1A
# NIM: 2603261

import numpy as np

# 1. Menyiapkan data suhu Celsius selama 10 hari
suhu_celsius = np.array([28, 30, 29, 31, 27, 32, 30, 28, 29, 31])

# 2. Rumus konversi Celsius ke Fahrenheit
suhu_fahrenheit = (9/5) * suhu_celsius + 32

# 3. Menghitung statistik sederhana menggunakan fungsi bawaan NumPy
rata_rata_celsius = np.mean(suhu_celsius)
suhu_tertinggi = np.max(suhu_celsius)
suhu_terendah = np.min(suhu_celsius)

# 4. Menampilkan hasil ke layar
print("--- DATA SUHU HARIAN ---")
print("Suhu Celsius   :", suhu_celsius)
print("Suhu Fahrenheit:", suhu_fahrenheit)

print("\n--- RINGKASAN HASIL ---")
print("Rata-rata suhu :", rata_rata_celsius, "°C")
print("Suhu paling panas:", suhu_tertinggi, "°C")
print("Suhu paling dingin:", suhu_terendah, "°C")