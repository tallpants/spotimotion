# Spotimotion

Detect the emotion of a human face in an image and find a Spotify playlist based on that emotion.

## Installation

```
$ git clone https://github.com/tallpants/spotimotion.git
$ cd spotimotion
$ pip install -r requirements.txt
```

## Usage

Because the program uses the [Microsoft Cognitive Services Emotion API](https://www.microsoft.com/cognitive-services/en-us/emotion-api), you'll need a key to access it. You can get one for free from the page linked.

Store the key in a file called `keys.json` with the format:

```json
{
  "MicrosoftEmotionAPI": "xxxxxx"
}
```

Run the program using Python and pass in the file path of the image as an argument:

```
$ python app.py test_images/happy.jpg
```

![happy.jpg](test_images/happy.jpg)

could give you:

![screenshot](test_images/screenshot.png)

## TODO

* Installation with `setuptools`
