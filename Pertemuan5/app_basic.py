from fastapi import FastAPI
import asyncio
import time

app = FastAPI(title="Pertemuan 5 - Multi-Worker Demo")

@app.get("/hello")
def hello():
    return {"msg": "hello", "note": "single/multi worker demo"}

# I/O-bound (blocking)
@app.get("/io_sync")
def io_sync(delay: float = 0.1):
    time.sleep(delay)  # BLOCKING
    time.sleep(delay)  # BLOCKING
    time.sleep(delay)  # BLOCKING
    return {"type": "io_sync", "delay": delay}

# I/O-bound (non-blocking jika dipakai di async stack)
@app.get("/io")
async def io_bound(delay: float = 0.1):
    await asyncio.sleep(delay)
    await asyncio.sleep(delay)
    await asyncio.sleep(delay)
    return {"type": "io", "delay": delay, "msg": "done"}

# CPU-bound (blocking di proses ini)
def fib(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

@app.get("/cpu")
def cpu_bound(n: int = 35):
    start = time.time()
    v = fib(n)
    dt = time.time() - start
    return {"type": "cpu", "n": n, "value": v, "elapsed": dt}

@app.get("/cpu_heavy")
def cpu_heavy(n: int = 40):
    start = time.time()
    v = fib(n)
    v2 = fib(n)  # Double computation
    v3 = fib(n)  # Triple computation
    dt = time.time() - start
    return {"type": "cpu_heavy", "n": n, "result": v + v2 + v3, "elapsed": dt}

# Tantangan tugas: campuran I/O dan CPU
@app.get("/mix")
async def mix(delay: float = 1.0, n: int = 35):
    t0 = time.time()
    await asyncio.sleep(delay)  # I/O-bound
    v = fib(n)  # CPU-bound
    dt = time.time() - t0
    return {"type": "mix", "delay": delay, "n": n, "value": v, "elapsed": dt}
