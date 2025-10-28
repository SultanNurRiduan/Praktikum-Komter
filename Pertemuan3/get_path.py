from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
def hello_name(name: str):
    return {"msg": f"Hello {name}!"}

@app.get("/multiply/{a}/{b}")
def multiply(a: int, b: int):
    return {"result": a * b}
