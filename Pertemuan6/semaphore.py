import threading
import time

# Semaphore dengan maksimal 2 thread (2 printer tersedia)
printer = threading.Semaphore(2)

def print_dokumen(karyawan, halaman):
    """Simulasi proses print dokumen"""
    print(f"{karyawan} menunggu printer ...")

    # Tunggu sampai ada printer yang tersedia
    with printer:
        print(f"{karyawan} mulai print {halaman} halaman")
        time.sleep(halaman * 0.5)  # simulasi waktu print (0.5 detik per halaman)
        print(f"{karyawan} selesai print!\n")

# 5 karyawan ingin print
karyawan_list = [
    ("Ani", 3),
    ("Budi", 2),
    ("Citra", 4),
    ("Deni", 2),
    ("Eka", 3),
]

# Buat thread untuk setiap karyawan
threads = []
for nama, halaman in karyawan_list:
    t = threading.Thread(target=print_dokumen, args=(nama, halaman))
    threads.append(t)
    t.start()

# Tunggu semua thread selesai
for t in threads:
    t.join()

print("\nSemua dokumen selesai dicetak!")
