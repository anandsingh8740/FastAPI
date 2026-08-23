### Environment Variables ###
# create env file

# CORS Handling
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config33 import settings
# import os
# from dotenv import load_dotenv

app = FastAPI()

# Read the Environment file
# load_dotenv() # means we are loading env file.

# Allowed Origins(Front-end URL)
#origins = os.getenv("ORIGINS")

origins = settings.origins

# We can secret key like that.
# SECRET_KEY = os.getenv("SECRET_KEY")
# DB_URL = os.getenv("DB_URL")

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


