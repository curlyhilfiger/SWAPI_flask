import json

import requests

from flask import render_template, request

from app import app


@app.route("/")
def characters():
    """ Character page view """
    current = 'Characters'
    url = 'https://swapi.co/api/people/'
    res = []
    while url:
        req = requests.get(url)
        json_str = req.text
        data = json.loads(json_str)
        res.append(data['results'])
        url = data['next']
    return render_template(
        "public/templates/public_template.html",
        characters=res,
        current=current
    )

@app.route("/planets")
def planets():
    """ Planets view page """
    current = 'Planets'
    url = 'https://swapi.co/api/planets/'
    res = []
    while url:
        req = requests.get(url)
        json_str = req.text
        data = json.loads(json_str)
        res.append(data['results'])
        url = data['next']
    return render_template(
        "public/templates/planets.html", planets=res,
        current=current
    )

@app.route("/starships")
def starships():
    """ Starships view page """
    current = 'Starships'
    url = 'https://swapi.co/api/starships/'
    res = []
    while url:
        req = requests.get(url)
        json_str = req.text
        data = json.loads(json_str)
        res.append(data['results'])
        url = data['next']
    return render_template(
        "public/templates/starships.html", starships=res,
        current=current
    )
