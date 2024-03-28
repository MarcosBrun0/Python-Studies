import re

from bs4 import BeautifulSoup
import requests
from pprint import pprint
response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
website =response.text

soup = BeautifulSoup(website,"html.parser")
link_list = []
list_element = soup.find_all(href=re.compile("zillow"))
pprint(list_element)
# for element in list_element:
#     text = element.text
#     newsoup = BeautifulSoup(text,"html.parser")
#     link = newsoup.find(name="a")
#     link_list.append(link)
#
# print(link_list)