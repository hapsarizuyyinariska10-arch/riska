# KODE PRAKTIKUM B0102
# STUDI KASUS PENGOLAHAN DATA AKADEMIK MAHASISWA

# LANGKAH 1: INISIALISASI DATA MENTAH
nim = "23010199"
nama_mahasiswa = "Ahmad Rian"
semester = 3
is_aktif = True

# Data nilai mentah berbentuk string
str_nilai_algoritma = "85.5"
str_nilai_basis_data = "78.0"
str_nilai_pemrograman_web = "90.2"
sks_per_matkul = 3

# Menampilkan data awal
print("=== DATA AWAL MAHASISWA ===")
print(f"Data Mahasiswa: {nama_mahasiswa} (NIM: {nim})")
print("Semester:", semester)
print("Status Aktif:", is_aktif)

# LANGKAH 2: KONVERSI TIPE DATA DAN KALKULASI
nilai_algo = float(str_nilai_algoritma)
nilai_bd = float(str_nilai_basis_data)
nilai_web = float(str_nilai_pemrograman_web)

total_nilai = nilai_algo + nilai_bd + nilai_web
jumlah_matkul = 3
rata_rata_nilai = total_nilai / jumlah_matkul
total_sks_diambil = jumlah_matkul * sks_per_matkul

# Menentukan status kelulusan
is_lulus_semester = (rata_rata_nilai >= 75.0) and is_aktif

print("\n=== HASIL EVALUASI AWAL ===")
print("Total Nilai:", total_nilai)
print("Rata-Rata Nilai:", round(rata_rata_nilai, 2))
print("Total SKS:", total_sks_diambil)
print("Status Lulus:", is_lulus_semester)

# LANGKAH 3: DATA KOLEKSI
daftar_matkul = [
    "Algoritma dan Pemrograman",
    "Basis Data",
    "Pemrograman Web"
]

transkrip_nilai = {
    "Algoritma dan Pemrograman": 4.0,
    "Basis Data": 3.0,
    "Pemrograman Web": 4.0
}

print("\n=== TRANSKRIP NILAI ===")
print("Daftar Mata Kuliah:", daftar_matkul)

# LANGKAH 4: PEMBARUAN VARIABEL DAN PENAMBAHAN DATA

# Mahasiswa mengambil 1 mata kuliah susulan
matkul_baru = "Jaringan Komputer"
nilai_matkul_baru_str = "88.0"
mutu_matkul_baru = 3.5  # Nilai AB

# A. Tambahkan mata kuliah ke List
daftar_matkul.append(matkul_baru)

# B. Tambahkan nilai mutu ke Dictionary
transkrip_nilai[matkul_baru] = mutu_matkul_baru

# C. Hitung ulang total nilai dan rata-rata
nilai_jk = float(nilai_matkul_baru_str)
total_nilai = total_nilai + nilai_jk
jumlah_matkul = len(daftar_matkul)
rata_rata_terbaru = total_nilai / jumlah_matkul

# D. Hitung IPK sementara dari Dictionary nilai mutu
total_bobot_mutu = sum(transkrip_nilai.values())
ipk_sementara = total_bobot_mutu / jumlah_matkul

# Tampilkan hasil setelah penambahan mata kuliah
print("\n=== HASIL SETELAH PENAMBAHAN MATA KULIAH ===")
print("Daftar Matkul Terbaru:", daftar_matkul)
print("Jumlah Matkul Total:", jumlah_matkul)
print("Rata-Rata Angka Baru:", round(rata_rata_terbaru, 2))
print("IPK Sementara (Skala 4):", round(ipk_sementara, 2))

print("Detail Transkrip Mutu:", transkrip_nilai)
