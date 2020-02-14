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


def get_nasa_search():
    nasaurl = 'https://images-api.nasa.gov/search?q=moon'

    nasaurlobj = urllib.request.urlopen(nasaurl)

    nasaread = nasaurlobj.read()

    decodenasa = json.loads(nasaread.decode('utf-8'))

    res = []
    for index in range(0, len(decodenasa["collection"]["items"])):
        if decodenasa["collection"]["items"][index]["data"][0]["media_type"] != 'image':
            continue
        href = decodenasa["collection"]["items"][index]["links"][0]["href"]
        desc = decodenasa["collection"]["items"][index]["data"][0]["description"]
        title = decodenasa["collection"]["items"][index]["data"][0]["title"]
        res.append({"href": href, "description": desc, "title": title})

    return res