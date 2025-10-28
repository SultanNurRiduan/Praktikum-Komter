import os
import math
from time import perf_counter
from multiprocessing import Process, Queue

def heavy(n: int) -> int:
    """Fungsi berat: menghitung jumlah faktor dari n."""
    c = 0
    r = int(math.isqrt(n))
    for i in range(1, r + 1):
        if n % i == 0:
            c += 2 if n // i != i else 1
    return c

def worker(nums, q: Queue):
    """Worker process: memproses sebagian data dan kirim hasil ke queue."""
    pid = os.getpid()
    subtotal = sum(heavy(x) for x in nums)
    q.put((pid, subtotal, len(nums)))

def main():
    data = list(range(100_000, 100_200))  # 200 angka
    chunks = [data[i:i + 50] for i in range(0, len(data), 50)]  # bagi jadi beberapa bagian

    q = Queue()
    procs = []
    t0 = perf_counter()

    # Jalankan semua proses
    for part in chunks:
        p = Process(target=worker, args=(part, q))
        procs.append(p)
        p.start()

    total = 0
    for _ in chunks:
        pid, subtotal, n_items = q.get()
        print(f"PID {pid} -> subtotal = {subtotal} (items = {n_items})")
        total += subtotal

    for p in procs:
        p.join()

    print(f"TOTAL: {total} | waktu: {perf_counter() - t0:.2f}s")

if __name__ == "__main__":
    main()
