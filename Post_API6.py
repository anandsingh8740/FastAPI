from fastapi import FastAPI

app = FastAPI()

# Post API -> Create a new user
# @app.post("/create-user")
# def create_user(name: str, age: int):
#     return {
#         "name": name,
#         "age": age
#     }
    

# Real World Example
@app.post("/create-user")
def create_user(user:dict):
    return {
        "message": "User Created",
        "data": user
    }