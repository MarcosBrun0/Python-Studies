import requests
from bs4 import BeautifulSoup

website = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=website)
text = response.text
soup = BeautifulSoup(text,"html.parser")

data =soup.find_all(name="h3" ,class_="title")

movietitles = [movie.getText() for movie in data]
print(movietitles)

