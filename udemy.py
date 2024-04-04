import requests
from bs4 import BeautifulSoup
import json

url = "https://books.toscrape.com/"

scraped_books = []

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
print(soup)

books = soup.select("article", class_="product_pod")

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").get_text().strip()

    book_details = {
        "title": title,
        "price": price
    }

    scraped_books.append(book_details)

    output_json = json.dumps(scraped_books, indent = 2)


    with open("booksss.json", "w") as json_file:
        json_file.write(output_json)

        print("It is printed already")
