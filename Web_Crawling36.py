'''
# for python code
import requests
from bs4 import BeautifulSoup

url ="http://example.com" # We want to crawl this website.

response = requests.get(url)

soup = BeautifulSoup(requests.text, "html.parser")

print(soup.title.text)
'''

#### Using FastAPI WEb Crawling.
from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/news")
def get_news():
    url = "https://indianexpress.com/"
    
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    title = []
    
    for item in soup.find_all("a", class_ = "article-click topblockNews__sidebarLink"):
        title.append(item.text)
        
    
    return{
        #"news": title[:5]
        # "news": title
        "news": title[:2]
    }
    
