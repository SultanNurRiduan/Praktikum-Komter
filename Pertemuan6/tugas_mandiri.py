import threading
import time
import random

# Maksimal 3 koneksi database aktif
db_pool = threading.Semaphore(3)

def akses_database(user_id):
    print(f"User-{user_id} menunggu koneksi database...")
    with db_pool:
        print(f"User-{user_id} tersambung! Eksekusi query...")
        waktu_query = random.randint(1, 2)
        time.sleep(waktu_query)
        print(f"User-{user_id} selesai dalam {waktu_query} detik.\n")

# Simulasi 6 user
threads = []
for i in range(1, 7):
    t = threading.Thread(target=akses_database, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Semua user telah selesai mengakses database.")
