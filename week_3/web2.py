#scrapping news headlines and summaries
import requests
from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/List_of_banks_in_Kenya"

response=requests.get(url)

# print(response)

soup=BeautifulSoup(response.text, "html.parser")

banks=soup.find("div",class_="mw-content-ltr mw-parser-output")

# print(banks)

items=banks.find("ul")

links=items.find_all("li")

for link in links:
    print(link.text)
    


