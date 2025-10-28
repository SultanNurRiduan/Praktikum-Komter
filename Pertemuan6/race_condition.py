import threading

counter = 0

def tambah_counter():
    """Fungsi untuk menambah counter"""
    global counter
    for _ in range(100000):
        counter += 1

# Buat 2 thread
t1 = threading.Thread(target=tambah_counter)
t2 = threading.Thread(target=tambah_counter)

# Jalankan
t1.start()
t2.start()

# Tunggu selesai
t1.join()
t2.join()

print(f"Counter akhir: {counter}")
print(f"Harusnya: 200000")
print(f"Selisih: {200000 - counter}")
