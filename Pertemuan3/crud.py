from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

db = {}  

class Item(BaseModel):
    name: str
    price: float

# CREATE
@app.post("/items")
def create_item(item: Item):
    item_id = len(db) + 1
    db[item_id] = {"id": item_id, **item.dict()}
    return db[item_id]

# READ
@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return db[item_id]

# UPDATE
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    db[item_id].update(item.dict())
    return db[item_id]

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    del db[item_id]
    return {"msg": "deleted"}
