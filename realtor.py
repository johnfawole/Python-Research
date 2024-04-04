import requests
from bs4 import BeautifulSoup
import json
 
output_data = []
base_url = "https://www.realtor.com/realestateandhomes-search/Atlanta_GA/show-newest-listings/sby-6"
API_KEY = "API_KEY"
 
 
def scrape_listing(num_pages):
    for page in range(1, num_pages + 1):
        # To scrape page 1
        if page == 1:
            url = f"{base_url}"
        else:
            url = (
                f"{base_url}/pg-{page}"  # Adjust the URL structure based on the website
            )
        print(f"Scraping data from page {page}... {url}")
 
        payload = {"api_key": API_KEY, "url": url}
        # Make a request to the ScraperAPI
        r = requests.get("http://api.scraperapi.com", params=payload)
        html_response = r.text
 
        # Parse the HTML response using BeautifulSoup
        soup = BeautifulSoup(html_response, "lxml")
 
        # scraping individual page
        listings = soup.select("div[class^='BasePropertyCard_propertyCardWrap__']")
        print("Listings found!")
 
        for listing in listings:
           
            price = listing.find("div", class_="card-price")
            price = price.get_text(strip=True) if price else "nil"
 
            full_address = listing.find("div", class_="card-address")
            full_address = full_address.get_text(strip=True) if full_address else "nil"
            address_parts = full_address.split(", ")
            address = address_parts[0] if address_parts else "nil"
            township = address_parts[1] if len(address_parts) > 1 else "nil"
 
            property_url_elements = listing.select("a[class^='LinkComponent_anchor__']")
            property_url = "nil"  # Default value if property_url_elements is empty
            for element in property_url_elements:
                property_url = "https://www.realtor.com" + element["href"]
                break
 
            beds = listing.find(
                "li",
                class_="PropertyBedMetastyles__StyledPropertyBedMeta-rui__a4nnof-0",
            )
            beds = (
                beds.find("span", {"data-testid": "meta-value"}).text.strip()
                if beds
                else "nil"
            )
            baths = listing.find(
                "li",
                class_="PropertyBathMetastyles__StyledPropertyBathMeta-rui__sc-67m6bo-0",
            )
            baths = baths.find("span").text.strip() if baths else "nil"
 
            sqft = listing.find(
                "li",
                class_="PropertySqftMetastyles__StyledPropertySqftMeta-rui__sc-1gdau7i-0",
            )
            sqft = (
                sqft.find("span", {"data-testid": "screen-reader-value"}).text.strip()
                if sqft
                else "nil"
            )
 
            plot_size = listing.find(
                "li",
                class_="PropertyLotSizeMetastyles__StyledPropertyLotSizeMeta-rui__sc-1cz4zco-0",
            )
            plot_size = (
                plot_size.find(
                    "span", {"data-testid": "screen-reader-value"}
                ).text.strip()
                if plot_size
                else "nil"
            )
 
            property_data = {
                "price": price,
                "address": address,
                "township": township,
                "url": property_url,
                "beds": beds,
                "baths": baths,
                "square_footage": sqft,
                "plot_size": plot_size,
            }
 
            output_data.append(property_data)
 
 
num_pages = 5  # Set the desired number of pages
 
# Scrape data from multiple pages
scrape_listing(num_pages)
 
# our property count
output_data.append({"num_hits": len(output_data)})
 
# Write the output to a JSON file
with open("Realtor_data.json", "w") as json_file:
    json.dump(output_data, json_file, indent=2)
 
print("Output written to output.json")