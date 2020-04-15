import requests
from bs4 import BeautifulSoup
import time as t

url = 'https://www.bestbuy.ca/en-ca/product/nintendo-switch-console-with-neon-red-blue-joy-con/13817625'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

addToCartButton = soup.find_all("button", {"class": "addToCartButton"})
disableBtn = soup.find_all("button", {"class": "disabled_1VcOk"})

while(addToCartButton == disableBtn):
    print("No switches available at BestBuy :(")
    t.sleep(120);  # refresh every 2 mins

print("Switches available! Go! Go! Go!")
print("Program ended")
