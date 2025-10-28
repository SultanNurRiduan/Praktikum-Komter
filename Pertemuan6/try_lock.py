import threading
import time

# Dua lock untuk simulasi resource
lock_P = threading.Lock()
lock_Q = threading.Lock()

def proses_dengan_trylock(nama, lock1, lock2):
    """Try-lock pattern untuk mencegah deadlock"""
    for percobaan in range(10):
        # Ambil lock pertama (blocking)
        lock1.acquire()
        print(f"{nama}: Lock 1 didapat (percobaan {percobaan + 1})")

        # Coba ambil lock kedua secara non-blocking
        if lock2.acquire(blocking=False):
            print(f"{nama}: Lock 2 juga didapat! SELESAI\n")
            time.sleep(0.1)
            lock2.release()
            lock1.release()
            return
        else:
            # Gagal ambil lock kedua → lepaskan lock pertama dan coba lagi
            print(f"{nama}: Lock 2 tidak tersedia, lepas lock 1\n")
            lock1.release()
            time.sleep(0.05)

    print(f"{nama}: Gagal setelah 10 percobaan\n")

# Jalankan dua thread yang saling mencoba mengakses resource berbeda
t1 = threading.Thread(target=proses_dengan_trylock, args=("Thread-A", lock_P, lock_Q))
t2 = threading.Thread(target=proses_dengan_trylock, args=("Thread-B", lock_Q, lock_P))

t1.start()
t2.start()

t1.join()
t2.join()

print("Selesai! Try-lock mencegah deadlock")
