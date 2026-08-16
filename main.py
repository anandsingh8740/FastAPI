from fastapi import FastAPI

app = FastAPI()

# Create a Get API
@app.get("/")    # "/" -> home path
def home():
    return {"message": "Hello without vern"}
