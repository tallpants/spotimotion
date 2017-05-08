import json
import random
import requests
import sys
import webbrowser


try:
    with open('keys.json') as data:
        keys = json.load(data)
except IOError as e:
    print("Couldn't find keys.json")
    print(e)
    sys.exit(1)

try:
    microsoft_emotion_headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': keys['MicrosoftEmotionAPI']
    }
except KeyError as e:
    print("Couldn't find the required keys in keys.json.")
    sys.exit(1)

with open(sys.argv[1], 'rb') as image_file:
    image = image_file.read()
    r = requests.post(url='https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize',
                      headers=microsoft_emotion_headers,
                      data=image)

if r.text == '[]':
    print("The API failed to recognize a face")
    exit(1)

emotion_data = json.loads(r.text)
emotions = dict(emotion_data[0]['scores'])

keys = list(emotions.keys())
vals = list(emotions.values())

dominant_emotion = keys[vals.index(max(vals))]
certainty_score = max(vals)

print(dominant_emotion, certainty_score)

spotify_query_params = {
    'q': dominant_emotion,
    'type': 'playlist',
    'limit': 50
}

r = requests.get(url='https://api.spotify.com/v1/search',
                 params=spotify_query_params)

spotify_response = json.loads(r.text)

playlists = {item['name']: item['external_urls']['spotify']
             for item in spotify_response['playlists']['items']}

random_playlist = random.choice(list(playlists.keys()))

webbrowser.open(playlists[random_playlist])
