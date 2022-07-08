from bs4 import BeautifulSoup
import requests
import re
product = input("Enter product name:")
url = f"https://www.flipkart.com/search?q={product}"
page = requests.get(url).text
doc = BeautifulSoup(page,"html.parser")

page_text = doc.find(class_="_2MImiq").span.text
pages = int(str(page_text).split("Page 1 of")[-1])
for page in range(1, pages + 1):
    url = f"https://www.flipkart.com/search?q={product}&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page,"html.parser")
    div = doc.find(class_="_1YokD2 _2GoDe3")

    items = div.find_all(text=re.compile(product))
    for item in items:
        parent = item.parent
        
        if parent.name != "a":
            continue
        link = parent['href']

        print(link) 
