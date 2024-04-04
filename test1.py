import requests
from bs4 import BeautifulSoup

list_of_urls = ["https://www.chocolate.co.uk/collections/all",]

scraped_data = []

def start_scrape():

  for url in list_of_urls:
    response = response.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    products = soup.select ("product-item")

    for product in products:
        name = product.select("a.product-item-meta__title")[0].get_text()
        price = product.select("span.price").replace('\nSale price£', '')
        
        scraped_data.append({
            "name": name,
            "price": price
        })

        start_scrape()