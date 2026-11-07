# Nama: Kori'ah 
# kelas: 1A
# NIM: 2603261

import numpy as np

# Data nilai ujian 30 siswa
nilai = np.array([
    80, 75, 90, 85, 70,
    95, 88, 76, 92, 84,
    78, 89, 91, 73, 86,
    94, 81, 79, 97, 83,
    87, 72, 96, 90, 85,
    77, 93, 82, 98, 88
])

# Mengurutkan nilai dari terbesar ke terkecil
nilai_urut = np.sort(nilai)[::-1]

# Mengambil 5 nilai tertinggi
lima_tertinggi = nilai_urut[:5]

# Menampilkan hasil
print("Data Nilai 30 Siswa:")
print(nilai)

print("\nNilai Setelah Diurutkan (Terbesar ke Terkecil):")
print(nilai_urut)

print("\n5 Nilai Tertinggi:")
print(lima_tertinggi)
