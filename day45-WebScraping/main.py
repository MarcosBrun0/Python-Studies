import requests
import bs4


response = requests.get("https://news.ycombinator.com/")
web_page =response.text
soup =bs4.BeautifulSoup(web_page,"html.parser")

var = soup.find(name="a",class_ = "storylink")

print(a)
