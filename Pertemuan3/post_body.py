from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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
