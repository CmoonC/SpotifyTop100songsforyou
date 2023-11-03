from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "e8dfa7b9b0764de9b56cc66e231c6bed"
CLIENT_SECRET = "601c654d3eec4653b270004da8a465a3"

USER_ID = "Castellss"
year = input("From which year you want to listen music? Type the date in format: YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{year}"

response = requests.get(url=URL)
content = response.text

top_100 = []

soup = BeautifulSoup(content, "html.parser")
songs = soup.find_all(name="h3", id="title-of-a-story", class_="u-line-height-125")
song_titles = [title.getText().strip("\n\t") for title in songs]
artists = soup.find_all(name="span", class_="u-max-width-330")
artist_names = [name.getText().strip("\n\t") for name in artists]
song_and_artist = dict(zip(song_titles, artist_names))
print(song_and_artist)

result = spotipy.oauth2.SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                     redirect_uri="http://example.com", scope="playlist-modify-private")

token = result.get_cached_token()["access_token"]
client = spotipy.client.Spotify(auth=token)
song_spotify = []
year = year.split("-")[0]
for (song, artist) in song_and_artist.items():
    try:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        uri = result["tracks"]["items"][0]["uri"]
        song_spotify.append(uri)
    except:
        print(f"track{song} artist:{artist}")
        print(f"This song: {song} does not in Spotify")
# playlist = client.user_playlist_create(user=client.current_user()["id"], name="Top100", public=False)
print(song_spotify)
# client.playlist_add_items(playlist_id=playlist["id"], items=song_spotify)
# print("New playlist  top_100 successfully created on Spotify!")

