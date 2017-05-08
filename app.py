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

print(r.text)
