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

with open('test_images/happy.jpg', 'rb') as image_file:
    image = image_file.read()
    r = requests.post(url='https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize',
                      headers=microsoft_emotion_headers,
                      data=image)

emotion_data = json.loads(r.text)

emotions = dict()
emotions['anger'] = emotion_data[0]['scores']['anger']
emotions['contempt'] = emotion_data[0]['scores']['contempt']
emotions['neutral'] = emotion_data[0]['scores']['neutral']
emotions['sadness'] = emotion_data[0]['scores']['sadness']
emotions['anger'] = emotion_data[0]['scores']['anger']
emotions['happiness'] = emotion_data[0]['scores']['happiness']
emotions['disgust'] = emotion_data[0]['scores']['disgust']
emotions['surprise'] = emotion_data[0]['scores']['surprise']
emotions['fear'] = emotion_data[0]['scores']['fear']


def get_dominant_emotion(d):
    d = dict(d)
    vals = list(d.values())
    keys = list(d.keys())

    return (keys[vals.index(max(vals))], max(vals))


print(get_dominant_emotion(emotions))
