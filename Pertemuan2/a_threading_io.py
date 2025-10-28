import time
import threading
from time import perf_counter

def fake_io(task_id: int, delay: float = 0.2):
    """Mensimulasikan I/O (menunggu)"""
    time.sleep(delay)
    return f"task-{task_id} done"

def worker(task_id: int, delay: float):
    result = fake_io(task_id, delay)
    print(result)

def main():
    # Serial
    start = perf_counter()
    N = 100
    for i in range(N):
        result = fake_io(i, 0.2)
        print(result)
    end = perf_counter()
    print(f"Total time (serial): {end - start:.3f}s for {N} tasks")

    # Threading
    start = perf_counter()
    threads = []
    for i in range(N):
        t = threading.Thread(target=worker, args=(i, 0.2))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    end = perf_counter()
    print(f"Total time (threads): {end - start:.3f}s for {N} tasks")

if __name__ == "__main__":
    main()
