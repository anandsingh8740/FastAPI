#### Using FastAPI WEb Crawling.

from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/news")
def get_news(page: int=1, limit:int=5):
    url = "https://news.ycombinator.com/"
    
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    title = []
    
    for item in soup.find_all("span", class_ ="titleline"):
        title.append(item.text)
        
    # Pagination Logic 
    start = (page -1)*limit
    end = start+limit
    
    return{
        "page": page,  # Page means which page we want to display.
        "limit": limit, # Limit means how many items we want to display per page.
        "total": len(title), # Total means the total number of items we have.
        "data": title[start:end] # Data means the data that will be displayed based on the start and end positions.
        
        
    }