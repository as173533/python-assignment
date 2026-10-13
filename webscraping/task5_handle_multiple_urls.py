import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import re
import sys

# Task 5: Handle multiple product URLs
# Combines the complete pipeline across multiple product URLs

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


class ProductTracker:
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
            self.response.raise_for_status()
            if self.response.encoding == 'ISO-8859-1':
                self.response.encoding = self.response.apparent_encoding
            self.soup = BeautifulSoup(self.response.text, "lxml")
        except requests.RequestException as e:
            print(f"Error fetching {self.url}: {e}")
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

    def product_image_url(self):
        if not self.soup:
            return "Image URL not found"
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

    def download_image(self, folder="downloaded_images"):
        img_url = self.product_image_url()
        if not img_url or img_url == "Image URL not found":
            return "Image download skipped: image URL not found."

        os.makedirs(folder, exist_ok=True)
        safe_name = re.sub(r'[<>:"/\\|?*]', '_', self.product_title())[:30].strip()
        file_path = os.path.join(folder, f"{safe_name}.jpg")

        try:
            img_response = requests.get(img_url, headers=self.user_agent, timeout=20)
            img_response.raise_for_status()
            with open(file_path, "wb") as f:
                f.write(img_response.content)
            return file_path
        except requests.RequestException as e:
            return f"Download failed: {e}"

    def compare_price(self, target_price):
        current_price = self.get_numeric_price()
        if current_price is None:
            return "Comparison unavailable: could not parse numeric price."

        if current_price <= target_price:
            savings = target_price - current_price
            return (
                f"GOOD DEAL: Current price ({current_price:.2f}) is within target price ({target_price:.2f}). "
                f"Savings: {savings:.2f}"
            )
        else:
            diff = current_price - target_price
            return (
                f"ABOVE TARGET: Current price ({current_price:.2f}) exceeds target price ({target_price:.2f}) "
                f"by {diff:.2f}"
            )


if __name__ == "__main__":
    # Multiple product URLs with target prices
    products_list = [
        {
            "url": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
            "target_price": 55.00
        },
        {
            "url": "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html",
            "target_price": 50.00
        },
        {
            "url": "https://books.toscrape.com/catalogue/soumission_998/index.html",
            "target_price": 52.00
        }
    ]

    print("=" * 65)
    print(" TASK 5: HANDLE MULTIPLE PRODUCT URLS & COMPLETE PIPELINE")
    print("=" * 65)

    for idx, item in enumerate(products_list, start=1):
        print(f"\n[Product #{idx}]")
        print(f"URL: {item['url']}")

        # 1. Fetch data & initialize tracker
        tracker = ProductTracker(url=item["url"])

        # 2. Extract product details
        title = tracker.product_title()
        price = tracker.product_price()
        img_url = tracker.product_image_url()

        print("\nExtracted Details:")
        print(f"  • Title     : {title}")
        print(f"  • Price     : {price}")
        print(f"  • Image URL : {img_url}")

        # 3. Download product image
        saved_img = tracker.download_image(folder="downloaded_images")
        print(f"  • Image File: {saved_img}")

        # 4. Compare product price with target price
        comparison = tracker.compare_price(target_price=item["target_price"])
        print("\nPrice Comparison Result:")
        print(f"  • Target Price: {item['target_price']:.2f}")
        print(f"  • Result      : {comparison}")
        print("-" * 65)

    print("\n" + "=" * 65)
    print("All multiple product URLs processed successfully!")
    print("=" * 65)
