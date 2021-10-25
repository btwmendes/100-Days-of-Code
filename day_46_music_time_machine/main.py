import requests
from bs4 import BeautifulSoup
import spotipy
# from spotipy import SpotifyClientCredentials
from spotipy import SpotifyOAuth

# --------------------------------Billboard Data----------------------------
billboard_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{billboard_date}"
SPOTIFY_CLIENT_ID = "afdb653cefaf4a5aa490ff7f88fad1bd"
SPOTIFY_CLIENT_SECRET = "2271cf98a64e459e8274a8f8b202be0e"

response = requests.get(url=URL)
billboard_data = response.text

soup = BeautifulSoup(billboard_data, "html.parser")

song_title_data = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

songs = [song.getText() for song in song_title_data]
print(songs)

# --------------------------------Spotipy----------------------------

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


# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
#
# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])
#
# for album in albums:
#     print(album['name'])