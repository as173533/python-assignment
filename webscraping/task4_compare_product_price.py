import requests
from bs4 import BeautifulSoup
import re
import sys

# Task 4: Compare product price with a target price
# Builds on the PriceTracer structure from web5.py

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


class PriceComparator:
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
        title = self.soup.find("span", {"id": "productTitle"}) or self.soup.find("h1")
        if title is not None:
            return title.text.strip()
        return "Title not found"

    def product_price(self):
        if not self.soup:
            return "Price not found"
        price = (
            self.soup.find("span", {"class": "a-price-whole"}) or
            self.soup.find("span", {"class": "priceblock_ourprice"}) or
            self.soup.find("p", {"class": "price_color"}) or
            self.soup.find("span", {"class": "price"})
        )
        if price is not None:
            return price.text.strip()
        return "Price not found"

    def get_numeric_price(self):
        raw_price = self.product_price()
        if raw_price == "Price not found":
            return None
        cleaned = re.sub(r"[^\d.]", "", raw_price.replace(",", ""))
        try:
            return float(cleaned)
        except ValueError:
            return None

    def compare_with_target(self, target_price):
        current_price = self.get_numeric_price()
        if current_price is None:
            return {
                "status": "Error",
                "message": "Could not determine numeric price for comparison."
            }

        if current_price <= target_price:
            difference = target_price - current_price
            return {
                "status": "DEAL FOUND (Within Target)",
                "current_price": current_price,
                "target_price": target_price,
                "difference": difference,
                "message": (
                    f"GREAT DEAL! Current price ({current_price:.2f}) is within target price ({target_price:.2f}). "
                    f"You save {difference:.2f}."
                )
            }
        else:
            difference = current_price - target_price
            return {
                "status": "ABOVE TARGET",
                "current_price": current_price,
                "target_price": target_price,
                "difference": difference,
                "message": (
                    f"ABOVE TARGET: Current price ({current_price:.2f}) exceeds target price ({target_price:.2f}) "
                    f"by {difference:.2f}."
                )
            }


if __name__ == "__main__":
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    target_price = 55.00

    comparator = PriceComparator(url=url)
    title = comparator.product_title()
    price = comparator.product_price()
    result = comparator.compare_with_target(target_price=target_price)

    print("=" * 60)
    print("      TASK 4: PRODUCT PRICE COMPARISON")
    print("=" * 60)
    print(f"Product Title : {title}")
    print(f"Current Price : {price}")
    print(f"Target Price  : {target_price:.2f}")
    print("-" * 60)
    print(f"Status        : {result['status']}")
    print(f"Result        : {result['message']}")
    print("=" * 60)
