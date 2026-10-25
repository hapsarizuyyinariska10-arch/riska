
# KODE PRAKTIKUM B0103
# SISTEM PROFIL KARAKTER GAME RPG

# 1. Membuat variabel profil karakter
nama_hero = "Arka"
level = 10
hp = 95.5
is_alive = True

inventory = ["Pedang", "Perisai", "Busur"]

atribut = {
    "kekuatan": 80,
    "kelincahan": 65
}

# 2. Menampilkan seluruh informasi karakter
print("=== PROFIL KARAKTER ===")
print("Nama Hero:", nama_hero)
print("Level:", level)
print("HP:", hp)
print("Masih Hidup:", is_alive)
print("Inventory:", inventory)
print("Atribut:", atribut)

# 3. Menampilkan tipe data setiap variabel
print("\n=== TIPE DATA ===")
print("Tipe nama_hero:", type(nama_hero))
print("Tipe level:", type(level))
print("Tipe hp:", type(hp))
print("Tipe is_alive:", type(is_alive))
print("Tipe inventory:", type(inventory))
print("Tipe atribut:", type(atribut))

# 4. Aksi karakter
# Karakter mendapatkan item baru
inventory.append("Ramuan HP")

# Karakter naik level
level = float(level) + 0.5

# 5. Menampilkan informasi terbaru
print("\n=== PROFIL KARAKTER TERBARU ===")
print("Nama Hero:", nama_hero)
print("Level Terbaru:", level)
print("HP:", hp)
print("Masih Hidup:", is_alive)
print("Inventory Terbaru:", inventory)
print("Atribut:", atribut)
