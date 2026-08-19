from fastapi import FastAPI
app = FastAPI()

# /users?name= mohit
# /products?price=1000
@app.get("/users") # dynamic route
def get_users(name: str = None):   # Optional query parameter
    return{"Name": name}

@app.get("/products")
def get_users(limit: int=10):
    return{"limit": limit}

# Multiple query parameters
@app.get("/items")
def get_users(name: str = None, price: int=0): # (default, optional parameter)
    return {
        "name": name,
        "price": price
    }