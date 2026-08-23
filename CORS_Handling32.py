# CORS Handling
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowed Origins(Front-end URL)
origins = [
"http://localhost:3000/"  # frontend url  # generally this url we write in env file    
]

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,   # allowed FE
    allow_credentials = True,
    allow_methods = ["*"],  # * -> allow all API like get, put, post, delete etc
    allow_headers = ["*"]
    
)

@app.get("/")
def home():
    return{
        "message": "CORS ENABLE API"
    }

