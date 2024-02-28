import requests
import bs4


response = requests.get("https://news.ycombinator.com/")
web_page =response.text
soup =bs4.BeautifulSoup(web_page,"html.parser")

articles = soup.find_all(name="a",class_ = "storylink")
articles_text = []
articles_links =[]
for article_tag in articles:
    article_text = article_tag.getText()
    articles_text.append(article_text)
    article_link = article_tag.get("href")
    articles_links.append(article_text)
    article_upvote = soup.find_all(name="span", class_= "score").getText()


print(article_tag,article_upvote,article_link,article_text)
#I need to finish this day soon.

≈
