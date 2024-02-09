import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/Sony-PS5-Digital-Standalone/dp/B0BSNHFVL4/ref=sr_1_2?keywords=ps5&sr=8-2'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1"
}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

# Extracting the title
title_element = soup2.find(id='productTitle')
title = title_element.get_text(strip=True) if title_element else "Title not found"

# Extracting the price
price_element = soup2.find(id='priceblock_ourprice')
price = price_element.get_text(strip=True) if price_element else "Price not found"

print("Title:", title)
print("Price:", price)

import datetime

today = datetime.date.today()
    
import csv 

header = ['Title', 'Price', 'Date']
data = [title, price, today]

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)