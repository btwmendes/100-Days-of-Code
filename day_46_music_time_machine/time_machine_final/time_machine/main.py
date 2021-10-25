import requests
from bs4 import BeautifulSoup
import spotipy
# from spotipy import SpotifyClientCredentials
from spotipy import SpotifyOAuth

# --------------------------------Billboard Data----------------------------
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url=URL)
billboard_data = response.text

soup = BeautifulSoup(billboard_data, "html.parser")

song_title_data = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

songs = [song.getText() for song in song_title_data]
print(songs)

# --------------------------------Spotipy----------------------------

SPOTIFY_CLIENT_ID = 
SPOTIFY_CLIENT_SECRET = 
SPOTIPY_REDIRECT_URI = "http://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
print(user_id)

#--------------------------------Searching Spotify for songs by title--------------------------------
song_uris = []
year = date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#--------------------------------Creating a new private playlist in Spotify--------------------------------
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#--------------------------------Adding songs found into the new playlist--------------------------------
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
