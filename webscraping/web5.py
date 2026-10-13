import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self, url):
        self.url = url
        self.user_agent = {'User-Agent': 'Mozilla/5.0'}
        self.response = requests.get(self.url, headers=self.user_agent)
        self.soup = BeautifulSoup(self.response.content, "lxml")

    def product_price(self):
        price = self.soup.find("span", {"class": "priceblock_ourprice"})
        if price is not None:
            return price.text
        else:
            return "price not found"
    def product_title(self):
        title = self.soup.find("span", {"id": "productTitle"})

        if title is not None:
            return title.text.strip()
        else:
            return "Title not found"


url = "https://www.amazon.in/Samsung-Storage-Snapdragon-Processor-Security/dp/B0H4L5T84X/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.O0j_TJJW8CA6qjlPWnS33Vr-wTvNZEoH9GX6H2XZi0ZX_s4WBQPD-SEuXOvLLvWxQyxpfz5kGJlKcp2qJHsQej74e9AmEIV7YyCviLjHDId9VDUthVKJPZGLd6pObunduL4nanZoWmY_-HNqpfNbpuVd5y_ffXWmt_8Tfo_hd6QJYYJeRNaoXN5G6wjBLaJRHJekCkeZMHOaADiq1WrQo0SFkmDTNTnPW_pwR3yK9B8.Ie3kUrvXXLqY5hOUJetIDnHS7IqlrEW4pSI_WdY-5JE&dib_tag=se&keywords=Samsung%2BGalaxy%2BS30&qid=1790771876&sr=8-1-spons&aref=JrOUhcgM27&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"

device =  PriceTracer(url=url)
print(device.product_title())
print(device.product_price())