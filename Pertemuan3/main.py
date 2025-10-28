from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 1️⃣ Hello World
@app.get("/hello")
def hello():
    return {"msg": "Hello FastAPI!"}

# 2️⃣ Hello Name dan Multiply
@app.get("/hello/{name}")
def hello_name(name: str):
    return {"msg": f"Hello {name}!"}

@app.get("/multiply/{a}/{b}")
def multiply(a: int, b: int):
    return {"result": a * b}

# 3️⃣ Query Parameters (square dan greet)
@app.get("/square")
def square(n: int):
    return {"n": n, "square": n * n}

@app.get("/greet")
def greet(name: str = "Guest", age: int = 0):
    return {
        "name": name,
        "age": age,
        "msg": f"Hello {name}, you are {age} years old"
    }

# 4️⃣ Model User (POST)
class User(BaseModel):
    username: str
    email: str
    age: int

@app.post("/users")
def create_user(user: User):
    return {
        "msg": "User created successfully",
        "data": user
    }

# 5️⃣ CRUD Item
db = {}

class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
def create_item(item: Item):
    item_id = len(db) + 1
    db[item_id] = {"id": item_id, **item.dict()}
    return db[item_id]

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return db[item_id]

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    db[item_id].update(item.dict())
    return db[item_id]

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    del db[item_id]
    return {"msg": "deleted"}
