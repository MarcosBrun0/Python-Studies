from bs4 import BeautifulSoup
import Config,spotipy,requests
from spoti  py.oauth2 import SpotifyOAuth

date = input("What year you want to travel? format YYYY-MM-DD:")
#https://www.billboard.com/charts/hot-100/2024-03-09/ example of how the site adress works, after the slash is the date
billboards_website = "https://www.billboard.com/charts/hot-100/"

response = requests.get(url=f"{billboards_website}{date}/")
html_page = response.text

soup = BeautifulSoup(html_page,"html.parser")
titles = soup.select("li ul li h3")

music_list = [music.getText().strip() for music in titles]
print(music_list)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id= Config.SpotifyClientID,
        client_secret=Config.SpotifyClientSecret,
        show_dialog=True,
        cache_path="token.txt",
        username="Aster",
    )
)
user_id = sp.current_user()["id"]

musics_urls=[]
#MUSIC SEARCH
year = date.split("-")[0]
for music in music_list:
    result = sp.search(q=f"track:{music} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        musics_urls.append(uri)
    except IndexError:
        print(f"{music} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=musics_urls)
