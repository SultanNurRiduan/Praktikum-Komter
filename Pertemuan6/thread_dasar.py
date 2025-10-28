import threading
import time

def tugas_1():
    """Thread pertama"""
    for i in range(5):
        print(f"Thread 1: {i}")
        time.sleep(0.5)

def tugas_2():
    """Thread kedua"""
    for i in range(5):
        print(f"Thread 2: {i}")
        time.sleep(0.5)

# Buat thread
t1 = threading.Thread(target=tugas_1)
t2 = threading.Thread(target=tugas_2)

# Jalankan thread
print("Memulai thread ...")
t1.start()
t2.start()

# Tunggu semua thread selesai
t1.join()
t2.join()

print("Semua thread selesai!")
