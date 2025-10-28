from fastapi import FastAPI
import time, asyncio

app = FastAPI()

@app.get("/sync")
def sync_api():
    time.sleep(2)
    return {"mode": "sync", "msg": "done"}

@app.get("/async")
async def async_api():
    await asyncio.sleep(2)
    return {"mode": "async", "msg": "done"}
