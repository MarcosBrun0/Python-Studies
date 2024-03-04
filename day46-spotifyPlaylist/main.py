from bs4 import BeautifulSoup
import requests,pprint

date = input("What year you want to travel? format YYYY-MM-DD:")
#https://www.billboard.com/charts/hot-100/2024-03-09/ example of how the site adress works, after the slash is the date
billboards_website = "https://www.billboard.com/charts/hot-100/"

response = requests.get(url=f"{billboards_website}{date}/")
html_page = response.text

soup = BeautifulSoup(html_page,"html.parser")
titles = soup.find_all(name="h3",id="title-of-a-story")

pprint.pprint(titles)