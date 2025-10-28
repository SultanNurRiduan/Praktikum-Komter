import threading

counter = 0
lock = threading.Lock()  # Buat lock

def tambah_counter_aman():
    """ Fungsi aman dengan lock """
    global counter
    for _ in range(100000):
        with lock:  # Kunci critical section
            counter += 1  # Operasi aman
    # Lock otomatis dilepas di sini

# Buat 2 thread
t1 = threading.Thread(target=tambah_counter_aman)
t2 = threading.Thread(target=tambah_counter_aman)

# Jalankan
t1.start()
t2.start()

# Tunggu selesai
t1.join()
t2.join()

print(f"Counter akhir: {counter}")
print(f"Harusnya: 200000")
print(f"Selisih: {200000 - counter}")

if counter == 200000:
    print("SUKSES! Data aman dengan Lock")
