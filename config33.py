# For production level project 
# For big project we have to manage configuration


import os
from dotenv import load_dotenv

load_dotenv() # connect to the environment


class Settings:
    # Allowed Origins(Front-end URL)
    origins = os.getenv("ORIGINS")

    # We can secret key like that.
    SECRET_KEY = os.getenv("SECRET_KEY")
    DB_URL = os.getenv("DB_URL")
    
    
settings = Settings()
