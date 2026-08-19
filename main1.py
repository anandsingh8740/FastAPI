from fastapi import FastAPI

app = FastAPI()

# Create multiple Routes
# Home Route
@app.get("/")
def home():
    return {"message" : "Welcome to FastAPI"}

# About Route
@app.get("/about")
def about():
    return {"message" : "This is the About page"}

# User Route
@app.get("/users")
def users():
    return {
        "users": ["Anand", "Adarsh", "Shekhar"]
    }