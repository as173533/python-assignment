import requests

# Task 1: Fetch webpage data
# Based on requests structure from web.py and web2.py

def fetch_webpage_data(url):
    """
    Fetches raw webpage HTML data from a given URL using requests.
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }

    print(f"Fetching webpage data from:\n{url}\n")
    try:
        response = requests.get(url=url, headers=headers, timeout=20)
        response.raise_for_status()

        print("=" * 60)
        print("          TASK 1: WEBPAGE DATA FETCHED SUCCESSFULLY")
        print("=" * 60)
        print(f"HTTP Status Code : {response.status_code} OK")
        print(f"Content Type     : {response.headers.get('Content-Type')}")
        print(f"Total Bytes      : {len(response.content)} bytes")
        print(f"Detected Encoding: {response.encoding}")
        print("=" * 60)
        print("Preview of webpage HTML (First 350 characters):")
        print("-" * 60)
        print(response.text[:350].strip())
        print("-" * 60)

        return response.text

    except requests.RequestException as e:
        print(f"Error fetching webpage data: {e}")
        return None


if __name__ == "__main__":
    # Test product webpage URL
    product_url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    html_data = fetch_webpage_data(product_url)
