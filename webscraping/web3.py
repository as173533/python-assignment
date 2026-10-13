#filter the part of  ta data
import requests
from bs4 import BeautifulSoup
import csv

def Extract(url):
    headers = {
        "User-Agent": (
            "MyLearningScraper/1.0 "
            "(contact: your-email@example.com)"
        )
    }
    response = requests.get(url = url,headers=headers).content
    soup = BeautifulSoup(response, "lxml")
    tag = soup.find("div", {"id": "mp-right"})
    h = tag.find_all("h2")
    content = [h2.text for h2 in h]

    print(content)

    with open("wiki.csv", "w") as csv_file:
        csv_write = csv.writer(csv_file)
        csv_write.writerow(content)



Extract(url= 'https://en.wikipedia.org/wiki/Main_Page')