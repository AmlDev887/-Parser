import json
import csv
import time
import requests
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser

base_url = "https://quotes.toscrape.com"
url = base_url + "/"

rp = RobotFileParser()
rp.set_url(base_url + "/robots.txt")
rp.read()

if not rp.can_fetch("*", url):
    print("Скрапинг запрещён правилами robots.txt")
    exit()

print("robots.txt разрешает скрапинг продолжаем")

session = requests.Session()
all_quotes = []

while True:
    response = session.get(url)
    soupe = BeautifulSoup(response.text,"html.parser")

    quote_blocks  = soupe.find_all("div",class_ = "quote")
    for block in quote_blocks :
        text = block.find("span", class_="text").get_text()
        author = block.find("small", class_="author").get_text()
        tags = [tag.get_text() for tag in block.find_all("a", class_="tag")]
            
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
        print("Страницы кончились завершаем")
        break
    next_url = next_button.find("a")["href"]
    url = base_url + next_url
    time.sleep(1)

with open("quotes.json","w",encoding="utf-8") as f:
    json.dump(all_quotes, f, indent=4, ensure_ascii=False )

with open("quotes.csv","w",newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f,fieldnames = ["text", "author", "tags"])
    writer.writeheader()
    for q in all_quotes:
        writer.writerow({
            "text": q["text"],
            "author": q["author"],
            "tags": ", ".join(q["tags"])
        })
print("Готово: quotes.json и quotes.csv сохранены")









    
    
