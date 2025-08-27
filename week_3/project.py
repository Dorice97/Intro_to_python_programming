import requests
from bs4 import BeautifulSoup

url = "https://www.jumia.co.ke/flash-sales/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
print("Status Code:", response.status_code)

if response.status_code == 200:
    print("The page can be scraped.")
elif response.status_code == 403:
    print("Access denied.")
elif response.status_code == 404:
    print("Page not found.")

page = 1
all_products = []

while True:
    url = f"https://www.jumia.co.ke/flash-sales/?page={page}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        break  # stop if no more pages

    soup = BeautifulSoup(response.text, "html.parser")

    
    products = soup.find_all("article", class_="prd")

    if not products:  
        break

    for p in products:
        name_tag = p.find("h3", class_="name")
        brand_tag = p.find("div", class_="brand")
        price_tag = p.find("div", class_="prc")
        discount_tag = p.find("div", class_="bdg _dsct")
        reviews_tag = p.find("div", class_="rev")
        rating_tag = p.find("div", class_="stars _s")

        product_data = {
            "Product Name": name_tag.text.strip() if name_tag else "N/A",
            "Brand": brand_tag.text.strip() if brand_tag else "N/A",
            "Price": price_tag.text.strip() if price_tag else "N/A",
            "Discount": discount_tag.text.strip() if discount_tag else "No discount",
            "Reviews": reviews_tag.text.strip() if reviews_tag else "0",
            "Rating": rating_tag["data-star-rating"] if rating_tag and rating_tag.has_attr("data-star-rating") else "N/A"
        }

        all_products.append(product_data)

    page += 1

# Print summary
for product in all_products:
    print(product)

print(f"\nTotal products scraped: {len(all_products)}")




