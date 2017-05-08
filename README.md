A program that recognizes emotion from an image and finds a Spotify playlist to match it.

## Installation

```
$ git clone https://github.com/tallpants/spotimood.git
$ cd spotimood
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

## Maybe enhancements later

* Convert to web app
* Map emotions to Spotify's tunable track attributes
* Get seed tracks for personalized recommendations
* Use Spotify's recommendation API