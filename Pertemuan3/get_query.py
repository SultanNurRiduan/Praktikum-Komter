from fastapi import FastAPI

app = FastAPI()

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
