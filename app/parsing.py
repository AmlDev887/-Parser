import json
import requests 
import time 
from pydantic import BaseModel,TypeAdapter 
from bs4 import BeautifulSoup

session = requests.Session()
url = "https://habr.com/ru/articles/803869/"
file = "robots.txt"

                    
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
text = soup.get_text() 
