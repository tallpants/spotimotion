import json
import requests

try:
    with open('keys.json') as data:
        keys = json.load(data)
except IOError as e:
    print("Couldn't find keys.json")
    print(e)

microsoft_emotion_headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': keys['MicrosoftEmotionAPI']
}

with open('test_images/happy.jpg', 'rb') as image_file:
    image = image_file.read()
    r = requests.post(url='https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize',
                      headers=microsoft_emotion_headers,
                      data=image)

print(r.text)
