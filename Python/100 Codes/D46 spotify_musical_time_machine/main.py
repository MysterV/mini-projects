import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

# You're gonna need to create file called 'api_key.txt' and put client ID and secret as separate lines in the file
# ===== Config =====
date = input('What date do you want? (YYYY-MM-DD): ')
URL = f'https://www.billboard.com/charts/hot-100/{date}'


# ===== get Billboard titles =====
# Get website content
response = requests.get(url=URL, timeout=5.0, headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
response.raise_for_status()

# Make a soup and scrape titles
site_soup = BeautifulSoup(response.text, 'html.parser')
titles = [i.get_text().strip() for i in site_soup.select('li.o-chart-results-list__item > h3#title-of-a-story')]
authors = [i.get_text().strip() for i in site_soup.select('li.o-chart-results-list__item > h3#title-of-a-story + span')]


# ===== make a Spotify playlist =====

# Connect to Spotify
scope = 'playlist-modify-public'
redirect_uri = 'https://example.com/'
with open('api_key.txt') as f:
    client_id = f.readline().strip()
    client_secret = f.readline().strip()

spot = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope,
    redirect_uri=redirect_uri,
    client_id=client_id,
    client_secret=client_secret,
    show_dialog=True,
    cache_path='token.txt'))

user_id = spot.current_user()["id"]

# Get music URIs
songs_uri = []
for i in range(len(titles)-48):
    # result = spot.search(q=f'track:{titles[i]}  artist:{authors[i]}', type='track')
    result = spot.search(q=f'track:{titles[i]} year:{date.split('-')[0]}', type='track')
    try:
        result_uri = result['tracks']['items'][0]['uri']
        songs_uri.append(result_uri)
    except IndexError:
        print(f"{titles[i]} not found, skipped")

# Create playlist
playlist = spot.user_playlist_create(user=user_id, name=f'{date} Top Music', public=True)
pprint(playlist)
playlist_id = playlist['id']

# Add music
print(songs_uri)
print(len(songs_uri))
spot.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=songs_uri)
