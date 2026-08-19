# Path + Query + Body Combo
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# PUT / users/101?nitify=true  #users/101 -> path param | nitify=true -> parts of query param
'''
# How can we use all these three things in a single(same) API?
Request Body -> 
{
    "name": "John Doe",
    "age": 30,
}
'''

users = []
class User(BaseModel):
    name: str
    age: int
    
@app.post("/users")
def create_user(user:User):
    users.append(user)
    return {
        "message": "User created", 
        "data": user
    }

@app.put("/users/{user_id}")
def updated_user(user_id: int, user:User, notify:bool = False):
    if user_id < len(users):
        users[user_id] = user
        
        return {
            "message": "User Updated",
            "notify": notify,
            "data": user
        }
    return {
        "error": "User not found"
    }
        
# 1:28:00
    
