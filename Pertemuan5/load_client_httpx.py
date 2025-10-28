import argparse
import asyncio
import statistics
import time
import httpx
from collections import Counter

async def fetch(client: httpx.AsyncClient, url: str):
    t0 = time.perf_counter()
    r = await client.get(url)
    t1 = time.perf_counter()
    return (r.status_code, r.elapsed.total_seconds(), t1 - t0)

async def run(url: str, n: int, c: int):
    results = []
    async with httpx.AsyncClient(timeout=30.0) as client:
        sem = asyncio.Semaphore(c)

        async def worker():
            async with sem:
                return await fetch(client, url)

        tasks = [asyncio.create_task(worker()) for _ in range(n)]
        t0 = time.perf_counter()
        results = await asyncio.gather(*tasks)
        t1 = time.perf_counter()

    codes = [rc for rc, _, _ in results]
    server_elapsed = [e for _, e, _ in results]
    client_elapsed = [e for _, _, e in results]

    def stats(name, arr):
        if not arr:
            return f"{name}: (no data)"
        return (
            f"{name}: count={len(arr)} "
            f"min={min(arr):.3f}s "
            f"p50={statistics.median(arr):.3f}s "
            f"avg={statistics.mean(arr):.3f}s "
            f"p95={statistics.quantiles(arr, n=20)[18]:.3f}s "
            f"max={max(arr):.3f}s"
        )

    print(f"\n=== Load Test {url} ===")
    print(f"Requests: {n}, Concurrency: {c}")
    print(f"Total time: {(t1 - t0):.3f}s")
    print(f"Throughput (approx): {n / (t1 - t0):.2f} req/s")
    print(f"HTTP status counts: {dict(Counter(codes))}")
    print(stats("Server elapsed (httpx r.elapsed)", server_elapsed))
    print(stats("Client round-trip", client_elapsed))
    print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="Target URL")
    parser.add_argument("--n", type=int, default=50, help="Total requests")
    parser.add_argument("--c", type=int, default=10, help="Concurrency")
    args = parser.parse_args()

    asyncio.run(run(args.url, args.n, args.c))
