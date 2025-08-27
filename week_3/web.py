import requests
from bs4 import BeautifulSoup

#use get function to access request module
#access to webpage as an arguement to the function

results=requests.get("https://www.jumia.co.ke/mlp-jumia-official-stores/")

#print result status code to make sure the page is accessible

# print(results.status_code)

#http headers to veryfy that we have accessed correct page
# print(results.headers)

#extract content
src=results.content

# beatufulsoup to parse and process the source
#create a beatifullsoup object based on source variable above

soup=BeautifulSoup(src, 'lxml')

#try request for all links

links=soup.find_all('a')
# print(links)
# print('\n')

#for loop to filter and print out specific links

for link in links:
    if "about" in link.text:
        print(link)
        print(link.attres['href'])

print(link)

