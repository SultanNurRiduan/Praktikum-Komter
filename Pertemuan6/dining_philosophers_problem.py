import threading
import time
import random

# Jumlah filsuf dan garpu
jumlah_filsuf = 5

# Membuat lock untuk setiap garpu
garpu = [threading.Lock() for _ in range(jumlah_filsuf)]

def makan(filsuf_id):
    kiri = filsuf_id
    kanan = (filsuf_id + 1) % jumlah_filsuf

    # Terapkan Lock Ordering: ambil garpu dengan nomor lebih kecil dulu
    first = min(kiri, kanan)
    second = max(kiri, kanan)

    while True:
        print(f"Filsuf-{filsuf_id} sedang berpikir...")
        time.sleep(random.uniform(1, 2))  # waktu berpikir acak

        print(f"Filsuf-{filsuf_id} lapar dan mencoba mengambil garpu {first} dan {second}...")
        with garpu[first]:
            with garpu[second]:
                print(f"Filsuf-{filsuf_id} mulai makan menggunakan garpu {first} dan {second}.")
                time.sleep(random.uniform(1, 2))  # waktu makan acak
                print(f"Filsuf-{filsuf_id} selesai makan dan meletakkan garpu {first} dan {second}.\n")

# Membuat thread untuk setiap filsuf
threads = []
for i in range(jumlah_filsuf):
    t = threading.Thread(target=makan, args=(i,), daemon=True)
    threads.append(t)
    t.start()

# Jalankan simulasi selama 10 detik
time.sleep(10)
print("Simulasi selesai. Tidak terjadi deadlock berkat Lock Ordering.")
