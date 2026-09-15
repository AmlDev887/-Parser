import json
import requests 
import time 
from pydantic import BaseModel,TypeAdapter 
from bs4 import BeautifulSoup

session = requests.Session()
base_url = "https://quotes.toscrape.com"
url = "https://quotes.toscrape.com/"
file = "robots.json"
while True:
    
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    with open(file,"w",encoding="utf-8") as f:
        json.dump(soup.get_text(), f, indent=4, ensure_ascii=False)

    next_button = soup.find("li",class_="next")
    if next_button == None:
        print("Процесс окончен!")
        break
    next_url = next_button.find("a")["href"]
    url = base_url + next_url