import re
from bs4 import BeautifulSoup
import requests
from pprint import pprint
response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
website =response.text

soup = BeautifulSoup(website,"html.parser")

list_element = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

#lIST OF LINKS

link_list = []
for element in list_element:
     link = element.find("a")
     link_list.append(link.get("href"))

#LIST OF ADDRESS

address_list = []
for element in list_element:
    address = element.find(name="address")
    address = [item.strip() for item in address if str(item)]
    address = address[0]
    address_list.append(address)

#LIST OF PRICES

price_list = []
for element in list_element:
    price = element.find(name="span", class_="PropertyCardWrapper__StyledPriceLine")
    pricestring= str(price.getText())
    s = pricestring
    s = re.sub(r'[\$\+,/]', '', s)
    # Extract numeric part
    num = re.findall(r'\d+', s)
    price_list.append(str(num[0]))


