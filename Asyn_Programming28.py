'''
# Normal Sync programming
import time

def task():
    time.sleep(3) # wait 3 sec
    return "Done"

'''
'''
# Asyn Programming
import time 
import asyncio # we can write non blocking code


async def task():
    await asyncio.sleep(3) # await, wait without blocking
    return "Done"

'''

import time
import asyncio # async input output
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(3) # It will task 3 sec for execute the program
    return{
        "message": "Async API"
    }
