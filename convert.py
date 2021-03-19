import pprint
import spotipy
import spotipy.util as util
import re
from apiclient.discovery import build

YOUTUBE_API_KEY = 'AIzaSyAggIO9G7DiSz9lMfsddbB7Vs-zMxbibt0'
username = 'e0gqy0t4edd27782g8r930bto'

print('')
print('Please Input Mixtape URL')
video_url = input('>> ')
print('')

pattern = r'(?:https?:\/\/)?(?:[0-9A-Z-]+\.)?(?:youtube|youtu|youtube-nocookie)\.(?:com|be)\/(?:watch\?v=|watch\?.+&v=|embed\/|v\/|.+\?v=)?([^&=\n%\?]{11})'
video_id_temp = re.findall(pattern, video_url,)
video_id = video_id_temp[0]

class Spotify_token:
    def __init__(self, username):
        self.username = username
        self.scope = 'playlist-modify-public'

    def set(self):
        token = util.prompt_for_user_token(self.username, self.scope)
        return token

ST = Spotify_token(username)
token = ST.set()

sp = spotipy.Spotify(auth=token)
sp.trace = False

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

track_ids = []

video_response = youtube.videos().list(
    part = 'snippet',
    id = video_id,
).execute()

playlist_name = video_response['items'][0]['snippet']['title']
description = video_response['items'][0]['snippet']['description']

playlists = sp.user_playlist_create(username, playlist_name)
playlist_id = playlists['id']

results = re.findall(r'([a-zA-Z][a-zA-Z0-9_()?!  \"\'’,.]+ [-–] [a-zA-Z0-9_()?!  \"\'’,.]+[a-zA-Z])', description)

for result in results:
    current_word = result
    search_str = re.sub(r' [-–] ', ' ', result)
    result = sp.search(search_str, limit=1)

    if result['tracks']['total'] == 0:
        print(f'❌ Not Found   : {current_word}')
    else:
        print(f'⭕ Add Success : {current_word}')

    for item in result['tracks']['items']:
        track_id = item['id']
        track_ids.append(track_id)

print('')

if sp.user_playlist_add_tracks(username, playlist_id, track_ids):
    print("📢 Playlist Convert Success 📢")
else:
    print("Error")

print('')