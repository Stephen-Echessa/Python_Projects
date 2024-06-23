import requests
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

SPOTIFY_REDIRECT_URI = "https://example.com"
SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=SPOTIFY_REDIRECT_URI,
                                               scope=scope))

user_results = sp.current_user()
spotify_display_name = user_results["display_name"]
spotify_id = user_results["id"]

print(spotify_id)
print(spotify_display_name)

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")

billboard_link = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(billboard_link)

song_titles = []
songs_uri = []

soup = BeautifulSoup(response.text, "html.parser")
soup_titles = soup.find_all(id="title-of-a-story",
                            class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 "
                                   "lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 "
                                   "u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 "
                                   "u-max-width-230@tablet-only")

for song_title in soup_titles:
    song_title = song_title.text.strip()
    song_titles.append(song_title)
    track_result = sp.search(song_title)
    try:
        songs_uri.append(track_result["tracks"]['items'][0]['uri'])
    except IndexError:
        songs_uri.append("Track Uri not available")

print(song_titles)
print(songs_uri)

created_playlist = sp.user_playlist_create(user=spotify_id, name=f"{date} Billboard 100", public=False)
playlist_id = created_playlist["id"]
added_songs = sp.playlist_add_items(playlist_id, songs_uri)
print(added_songs)
