
# 1. LIST (berurutan dan bisa diubah)
hobi = ["Membaca", "Koding", "Berenang"]
print("List Hobi:", hobi)
print("Tipe:", type(hobi))

# 2. TUPLE (berurutan dan tidak bisa diubah)
koordinat = (-6.1751, 106.8650)
print("Tuple Koordinat:", koordinat)
print("Tipe:", type(koordinat))

# 3. DICTIONARY (pasangan key dan value)
mahasiswa = {
    "nama": "Siti",
    "nim": "123456",
    "ipk": 3.85
}
print("Dict Mahasiswa:", mahasiswa)
print("Nama Mahasiswa:", mahasiswa["nama"])
print("Tipe:", type(mahasiswa))

# 4. SET (nilai unik, tanpa duplikat)
angka_unik = {1, 2, 2, 3, 4, 4, 5}
print("Set Angka Unik (otomatis menghapus duplikat):", angka_unik)
print("Tipe:", type(angka_unik))
