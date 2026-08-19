from fastapi import FastAPI

app = FastAPI()

# Create a Get API
@app.get("/")    # "/" -> home page path
def home():
    return {"message": "Hello world from FastAPI VENV"}

