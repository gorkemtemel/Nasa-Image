from django.db import models

# Create your models here.
import urllib.request
import json


def nasa_default_image():
    apodurl = 'https://api.nasa.gov/planetary/apod?api_key=FFTQm4LdbwOtOk8lDjfG5qhMNbYBJKpzG6Vojhs6'

    apodurlobj = urllib.request.urlopen(apodurl)

    apodread = apodurlobj.read()

    decodeapod = json.loads(apodread.decode('utf-8'))

    return decodeapod['url']