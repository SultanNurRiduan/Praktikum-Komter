import threading
import time

# Membuat dua lock
lock_X = threading.Lock()
lock_Y = threading.Lock()

def proses_dengan_timeout(nama, lock1, lock2):
    """Coba ambil lock dengan timeout"""
    for percobaan in range(5):
        # Coba ambil lock pertama
        if lock1.acquire(timeout=1):
            print(f"{nama}: Lock 1 didapat (percobaan {percobaan + 1})")
            time.sleep(0.2)

            # Coba ambil lock kedua dengan timeout
            if lock2.acquire(timeout=1):
                print(f"{nama}: Lock 2 didapat! SELESAI\n")
                lock2.release()
                lock1.release()
                return
            else:
                # Timeout pada lock kedua, lepaskan lock pertama
                print(f"{nama}: Timeout! Lepas lock 1, coba lagi\n")
                lock1.release()
                time.sleep(0.1)
        else:
            # Timeout pada lock pertama
            print(f"{nama}: Timeout pada lock 1\n")
            time.sleep(0.1)

    print(f"{nama}: Gagal setelah 5 percobaan\n")

# Jalankan dua thread yang saling bersaing lock
t1 = threading.Thread(target=proses_dengan_timeout, args=("Thread-1", lock_X, lock_Y))
t2 = threading.Thread(target=proses_dengan_timeout, args=("Thread-2", lock_Y, lock_X))

t1.start()
t2.start()

t1.join()
t2.join()

print("Selesai! Timeout mencegah deadlock permanen")
