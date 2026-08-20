# Global Exception Handling
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Custom Exception Handling
class UserNotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(UserNotFoundException)
def user_not_found_handler(request:Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content ={
        "status": "error",
        "message": f"User {exc.name} not found."
        }
    )
@app.get("/user/{user_id}")
def get_user(name:str):
    if name!= "mohit":
        raise UserNotFoundException(name=name)
    return{
        "name": name
    }
    
# 