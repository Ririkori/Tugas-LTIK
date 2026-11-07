# Nama: Kori'ah 
# kelas: 1A
# NIM: 2603261

import numpy as np

# Data suhu Celsius selama 10 hari
suhu_celsius = np.array([28, 30, 29, 31, 27, 32, 30, 28, 29, 31, 40, 0, 16, 20])

# Konversi Celsius ke Fahrenheit
suhu_fahrenheit = (9/5) * suhu_celsius + 32

# Menampilkan hasil
print("Data Suhu Celsius:")
print(suhu_celsius)

print("\nHasil Konversi ke Fahrenheit:")
print(suhu_fahrenheit)

