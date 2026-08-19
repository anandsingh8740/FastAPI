from fastapi import FastAPI
app = FastAPI()

# User Route
# We can define type based on data
@app.get("/users/{user_id}") # dynamic route
def get_user(user_id: str):
    return{"user_id": user_id}