# c_multiprocessing_cpu.py

import math
from time import perf_counter
from multiprocessing import Pool, cpu_count

def is_prime(n: int) -> bool:
    """Cek apakah bilangan n adalah bilangan prima."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.isqrt(n))
    for f in range(3, r + 1, 2):
        if n % f == 0:
            return False
    return True

def count_primes(start: int, end: int) -> int:
    """Hitung jumlah bilangan prima dalam rentang tertentu."""
    return sum(1 for x in range(start, end) if is_prime(x))

def single_process(total_n: int = 300_000):
    """Hitung jumlah bilangan prima menggunakan satu proses."""
    start = perf_counter()
    result = count_primes(1, total_n)
    dur = perf_counter() - start
    print(f"[Single] primes <= {total_n}: {result} in {dur:.2f}s")

def multi_process(total_n: int = 300_000):
    """Hitung jumlah bilangan prima menggunakan beberapa proses (multi-core)."""
    start = perf_counter()
    cores = max(1, cpu_count() - 1)
    chunk = total_n // cores
    ranges = [
        (i * chunk + 1, (i + 1) * chunk if i < cores - 1 else total_n)
        for i in range(cores)
    ]

    with Pool(processes=cores) as p:
        parts = p.starmap(count_primes, ranges)

    result = sum(parts)
    dur = perf_counter() - start
    print(f"[Multi x{cores}] primes <= {total_n}: {result} in {dur:.2f}s")

if __name__ == "__main__":
    N = 300_000
    single_process(N)
    multi_process(N)
