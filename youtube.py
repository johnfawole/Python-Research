import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
print(soup)

books = soup.select("article", class_="product_pod")

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").get_text().strip()
    #second element in the class has the actual rating
    rating = book.find("p", class_= "star-rating")["class"][1]
    availability = book.find("p", class_="instock availability").text.strip()

    
    print("Title:", title)
    print("Price:", price)
    print("Rating:", rating)
    print("Availability:", availability)