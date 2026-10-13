import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys

# Task 2: Extract product title, price, and image URL
# Based on BeautifulSoup parsing structure from web3.py and web5.py

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


class ProductExtractor:
    def __init__(self, url):
        self.url = url
        self.user_agent = {
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/122.0.0.0 Safari/537.36'
            ),
            'Accept-Language': 'en-US,en;q=0.9',
        }
        try:
            self.response = requests.get(self.url, headers=self.user_agent, timeout=20)
            if self.response.encoding == 'ISO-8859-1':
                self.response.encoding = self.response.apparent_encoding
            self.soup = BeautifulSoup(self.response.text, "lxml")
        except requests.RequestException as e:
            print(f"Error connecting to {self.url}: {e}")
            self.soup = None

    def product_title(self):
        if not self.soup:
            return "Title not found"
        # Checks productTitle ID (Amazon/e-commerce) or standard h1 heading
        title = self.soup.find("span", {"id": "productTitle"}) or self.soup.find("h1")
        if title is not None:
            return title.text.strip()
        return "Title not found"

    def product_price(self):
        if not self.soup:
            return "Price not found"
        # Checks common e-commerce price classes
        price = (
            self.soup.find("span", {"class": "a-price-whole"}) or
            self.soup.find("span", {"class": "priceblock_ourprice"}) or
            self.soup.find("span", {"class": "priceblock_dealprice"}) or
            self.soup.find("p", {"class": "price_color"}) or
            self.soup.find("span", {"class": "price"})
        )
        if price is not None:
            return price.text.strip()
        return "Price not found"

    def product_image_url(self):
        if not self.soup:
            return "Image URL not found"
        # Find product image element
        img = (
            self.soup.find("img", {"id": "landingImage"}) or
            (self.soup.find("div", {"class": "item active"}).find("img") if self.soup.find("div", {"class": "item active"}) else None) or
            self.soup.find("img", {"class": "wp-post-image"}) or
            self.soup.find("img")
        )
        if img:
            src = img.get("src") or img.get("data-old-hires") or img.get("data-src")
            if src:
                return urljoin(self.url, src)
        return "Image URL not found"

    def extract_all(self):
        return {
            "title": self.product_title(),
            "price": self.product_price(),
            "image_url": self.product_image_url()
        }


if __name__ == "__main__":
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    print(f"Extracting details from:\n{url}\n")

    extractor = ProductExtractor(url=url)
    details = extractor.extract_all()

    print("=" * 60)
    print("      TASK 2: EXTRACTED PRODUCT DETAILS")
    print("=" * 60)
    print(f"Product Title : {details['title']}")
    print(f"Product Price : {details['price']}")
    print(f"Image URL     : {details['image_url']}")
    print("=" * 60)
