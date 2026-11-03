import time

# Catat waktu mulai
waktu_mulai = time.perf_counter()

# --- KODE YANG INGIN DIUKUR ---
total = 0
for i in range(10_000_000):
    total += i

# Catat waktu selesai
waktu_selesai = time.perf_counter()
lama_eksekusi = waktu_selesai - waktu_mulai

print(f"Hasil perhitungan: {total}")
print(f"Lama waktu eksekusi: {lama_eksekusi:.6f} detik")
