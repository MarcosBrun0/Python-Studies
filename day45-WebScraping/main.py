import requests
import bs4

response = requests.get("https://news.ycombinator.com/news")
web_page = response.text
soup = bs4.BeautifulSoup(web_page, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
articles_text = []
articles_links = []

for item in articles:
    text = item.getText()
    articles_text.append(text)
    links = item.__getattribute__("href")
    articles_links.append(links)

article_upvote = [score.getText() for score in  soup.find_all(name="span", class_="score")]

print( article_upvote, articles_links, articles_text)
# I need to finish this day soon.
