from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import time

app = FastAPI()

# Cache Storage
cache_data = []
last_fetch = 0

@app.get("/news")

def get_news(page: int=1, limit:int=5):
    global cache_data, last_fetch
    
    start = time.time()
    
    if time.time() - last_fetch > 60:
        print("Fetching Fresh Data")
        
        url="https://news.ycombinator.com/"
        
        response = requests.get(url)
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        cache_data = [
            item.text for item in soup.find_all("span", class_="titleline")
        ]
        
        
        last_fetch = time.time()
        
    else:
        print("Using catching Data")
        
    end = time.time()
    
    time_taken = round(end-start, 4)
    
    print("Time Taken: ", time_taken)
    
    start_index = (page - 1) * limit
    end_index = start_index + limit

    return {
        "time_taken" :time_taken,
        "data": cache_data[start_index:end_index]
    }
        
        
        
        
        
        
    # url = "https://news.ycombinator.com/"
    
    # response = requests.get(url)
    
    # soup = BeautifulSoup(response.text, "html.parser")
    
    # title = []
    
    # for item in soup.find_all("span", class_ ="titleline"):
    #     title.append(item.text)
        
    # # Pagination Logic 
    # start = (page -1)*limit
    # end = start+limit
    
    # return{
    #     "data":title[:5]
        
    # }