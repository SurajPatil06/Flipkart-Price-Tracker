from urllib import response
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

# Getting prize
url = "https://www.flipkart.com/asus-vivobook-go-15-2025-office-2024-m365-basic-intel-core-i3-n305-8-gb-512-gb-ssd-windows-11-home-e1504ga-nj3322ws-e1504ga-bq1225ws-thin-light-laptop/p/itm4bbb136e0a623?pid=COMH9SJ9ZVTH69GM&lid=LSTCOMH9SJ9ZVTH69GMCONYQO&marketplace=FLIPKART&q=laptop&store=6bo%2Fb5g&srno=s_1_19&otracker=search&otracker1=search&fm=organic&iid=6daa48c5-b9fd-4694-aa8d-97b8d9c5260b.COMH9SJ9ZVTH69GM.SEARCH&ppt=clp&ppn=electronics-republic-day-sale-dt-store&ssid=u465wg4ccw0000001768912017619&qH=312f91285e048e09#/"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
price = soup.find_all("div", class_="hZ3P6w bnqy13")[0].text
price_int = int(price.replace("₹", "").replace(",", ""))

# Storing time
now_date = datetime.now()
date = now_date.strftime("%x")

# Storing in csv
data = [date, price_int]
file_path = "data.csv"

with open(file_path, mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(data)

print("Successful!!")
print(date, price)