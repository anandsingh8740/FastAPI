'''
# BASIC LOGIC OF PYTHON
import requests

# API call
# response = requests.get("https://jsonplaceholder.typicode.com/posts")

# If we want data based on id 
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

data = response.json()

# print all data
# print(data)
# print for specific data like 2 field
print(data[:2])
'''


##### Using FastAPI
from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# GET ALL data
@app.get("/posts")
def get_posts():
    url="https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()

# for single post
@app.get("/posts/{post_id}")
def get_post(post_id:int):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    
    response = requests.get(url)
    
    if response.status_code !=200:
        raise HTTPException(status_code=404, detail="Page not found")
    return response.json()