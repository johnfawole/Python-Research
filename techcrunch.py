import requests
from bs4 import BeautifulSoup

techcrunch = "https://techcrunch.com/"

res = requests.get(techcrunch)
soup = BeautifulSoup(res.text, "html.parser")

articles = soup.find_all("div=", class_="post-block")
print("the scraping has started")
for article in articles:
   title = article.find("h2", class_= "post-block__title").text.strip()

   print("Title:", title)
 

