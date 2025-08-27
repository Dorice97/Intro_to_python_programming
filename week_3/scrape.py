import requests
from bs4 import BeautifulSoup

url="https://quotes.toscrape.com/"

response=requests.get(url)

print(response)

# if response.status_code==200:
#     # print("fetched successfull")

# else:
#     # print("error")

soup =BeautifulSoup(response.text,'html.parser')

one = soup.find("div",class_="quote")

# print(one.text)

for i in one :
    print(i.text)

# one = soup.find_a("div",class_="tags")

# links= one.find_all("a",class_="tag")
# for link in links :
#     print(link.text)
#     print(link['href'])

# extract all quotes
# quotes=soup.find_all("span",class_="text")

# for quote in quotes:
#     print(quote.text)

#extract authers
# authers=soup.find_all("small",class_="auther")

# for auther in authers :
#     print(auther.text)

#top ten tags
tags = soup.find_all("span",class_ ="tag-item")
print(tags)

for tag in tags:
    print(tag.text)
    links=tag.find("a",class_="tag")
    print(links['href'])



