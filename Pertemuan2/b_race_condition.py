import sys
import threading
import time

# Atur seberapa sering Python berpindah antar-thread
sys.setswitchinterval(1e-6)

N_THREADS = 50
N_INCREMENTS = 1000

COUNTER_BOX = [0]  # index-0 berperan sebagai COUNTER (list agar mutable)

def increment_without_lock():
    box = COUNTER_BOX
    for _ in range(N_INCREMENTS):
        cur = box[0]  # READ
        time.sleep(0)  # yield ke thread lain (sangat singkat)
        box[0] = cur + 1  # WRITE

def increment_with_lock(lock: threading.Lock):
    box = COUNTER_BOX
    for _ in range(N_INCREMENTS):
        with lock:
            cur = box[0]
            time.sleep(0)
            box[0] = cur + 1

def run_without_lock():
    COUNTER_BOX[0] = 0
    threads = [threading.Thread(target=increment_without_lock) for _ in range(N_THREADS)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Tanpa Lock -> COUNTER = {COUNTER_BOX[0]} (ekspektasi: {N_THREADS * N_INCREMENTS})")

def run_with_lock():
    COUNTER_BOX[0] = 0
    lock = threading.Lock()
    threads = [threading.Thread(target=increment_with_lock, args=(lock,)) for _ in range(N_THREADS)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Dengan Lock -> COUNTER = {COUNTER_BOX[0]} (ekspektasi: {N_THREADS * N_INCREMENTS})")

if __name__ == "__main__":
    run_without_lock()
    run_with_lock()
