import httpx, asyncio, time

URL_SYNC = "http://127.0.0.1:8000/sync"
URL_ASYNC = "http://127.0.0.1:8000/async"

async def fetch(client, url):
    r = await client.get(url)
    return r.json()

async def test(url, n=10):
    async with httpx.AsyncClient() as client:
        tasks = [fetch(client, url) for _ in range(n)]
        start = time.time()
        results = await asyncio.gather(*tasks)
        end = time.time()
        print(f"URL {url} selesai dalam {end - start:.2f} detik")
        return results

if __name__ == "__main__":
    asyncio.run(test(URL_SYNC))
    asyncio.run(test(URL_ASYNC))
