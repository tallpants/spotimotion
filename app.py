import json
import requests
import sys

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

emotion_data = json.loads(r.text)
emotions = dict(emotion_data[0]['scores'])

keys = list(emotions.keys())
vals = list(emotions.values())

dominant_emotion = keys[vals.index(max(vals))]
certainty_score = max(vals)

print(dominant_emotion, certainty_score)
