
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote, quote
import json
import os
import re
import mimetypes

user = input("Enter image name: ").strip()

if not user:
    print("Please enter an image name.")
    raise SystemExit

search_url = (
    f"https://www.bing.com/images/search?q={quote(user)}"
)

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/140.0.0.0 Safari/537.36"
    )
}

try:
    response = requests.get(
        search_url,
        headers=headers,
        timeout=20
    )
    response.raise_for_status()

except requests.RequestException as e:
    print("Search request failed:", e)
    raise SystemExit

soup = BeautifulSoup(response.text, "html.parser")
cards = soup.select("a.iusc")

print("Total image results:", len(cards))

if not cards:
    print("No image results found.")
    raise SystemExit

try:
    limit = int(input("How many images do you want? "))
except ValueError:
    print("Please enter a valid number.")
    raise SystemExit

if limit <= 0:
    print("Enter a number greater than zero.")
    raise SystemExit

# Create a safe folder name
folder = re.sub(r'[<>:"/\\|?*]', "_", user).strip()
os.makedirs(folder, exist_ok=True)

downloaded = 0

for index, card in enumerate(cards[:limit], start=1):
    data = card.get("m")

    if not data:
        continue

    try:
        details = json.loads(data)
        image_url = details.get("murl")

        if not image_url:
            continue

        print(f"\nImage {index}: {image_url}")

        try:
            image_response = requests.get(
                image_url,
                headers={
                    **headers,
                    "Referer": "https://www.bing.com/"
                },
                timeout=20
            )
            image_response.raise_for_status()

            content_type = image_response.headers.get(
                "Content-Type", ""
            ).split(";")[0].lower()

            # Avoid saving HTML error pages as images
            if not content_type.startswith("image/"):
                print("Skipped: URL did not return an image.")
                continue

            # Determine a safe file extension
            extension = mimetypes.guess_extension(content_type)

            if not extension:
                extension = ".img"

            image_name = f"image_{index}{extension}"
            file_path = os.path.join(folder, image_name)

            with open(file_path, "wb") as file:
                file.write(image_response.content)

            downloaded += 1
            print("Downloaded:", file_path)

        except requests.RequestException as e:
            print(f"Download failed for image {index}: {e}")
            continue

    except (json.JSONDecodeError, TypeError) as e:
        print(f"Skipped invalid image data: {e}")
        continue

print(f"\nFinished. Downloaded {downloaded} image(s).")
print("Folder:", os.path.abspath(folder))