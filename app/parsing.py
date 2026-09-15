import json
import requests 
import time 
from pydantic import BaseModel,TypeAdapter 
from bs4 import BeautifulSoup
import os 


base_url = "https://quotes.toscrape.com"
url = base_url + "/"

session = requests.Session()
all_quotes = []

while True:
    response = session.get(base_url)
    soupe = BeautifulSoup(response.text,"html.parser")

    quote_blocks  = soupe.find_all("div",class_ = "quote")
    for block in quote_blocks :
        text = block.find("span", class_="text").get_text()
        author = block.find("small", class_="author").get_text()
        tags = [tag.get_text() for tag in block.find_all("a", class_="tag")]:
            
        all_quotes.append(
            {
                "text":text,
                "author":author,
                "tags":tags
            }
        )
    print(f"Собрано цитат: {len(all_quotes)} (страница: {url})")

    next_button = soupe.find("li", class_="next")
    if next_button is None:
        print("Страницы кончились — завершаем")
        break
    next_url = next_button.find("a")["href"]
    url = base_url + next_url
    time.slepp(1)





    
    
