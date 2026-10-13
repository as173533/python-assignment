import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import re

# Task 3: Download product image
# Based on image downloading and binary file handling from web.py and web4.py

def download_product_image(page_url, folder="downloaded_images"):
    """
    Finds the product image on the webpage and downloads it to a local folder.
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }

    print(f"Fetching webpage to locate image:\n{page_url}\n")
    try:
        response = requests.get(page_url, headers=headers, timeout=20)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "lxml")

        # 1. Locate product title for safe naming (same technique as web4.py)
        title_tag = soup.find("span", {"id": "productTitle"}) or soup.find("h1")
        title = title_tag.text.strip() if title_tag else "product_image"
        safe_name = re.sub(r'[<>:"/\\|?*]', '_', title)[:30].strip()

        # 2. Locate product image URL
        img = (
            soup.find("img", {"id": "landingImage"}) or
            (soup.find("div", {"class": "item active"}).find("img") if soup.find("div", {"class": "item active"}) else None) or
            soup.find("img")
        )
        if not img:
            print("Product image not found on the page.")
            return None

        src = img.get("src") or img.get("data-old-hires") or img.get("data-src")
        img_url = urljoin(page_url, src)
        print(f"Found Image URL: {img_url}")

        # 3. Create folder (as done in web4.py)
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, f"{safe_name}.jpg")

        # 4. Download and save the image in binary write mode (wb) (as in web.py and web4.py)
        img_response = requests.get(img_url, headers=headers, timeout=20)
        img_response.raise_for_status()

        with open(file_path, "wb") as f:
            f.write(img_response.content)

        file_size = os.path.getsize(file_path)

        print("=" * 60)
        print("          TASK 3: PRODUCT IMAGE DOWNLOADED")
        print("=" * 60)
        print(f"Saved Path : {file_path}")
        print(f"File Size  : {file_size} bytes")
        print(f"Status     : Success")
        print("=" * 60)

        return file_path

    except requests.RequestException as e:
        print(f"Failed to download image: {e}")
        return None


if __name__ == "__main__":
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    download_product_image(page_url=url, folder="downloaded_images")
