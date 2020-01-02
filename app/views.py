import json

import requests

from flask import render_template, request, redirect

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
    print(res)
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
    with app.open_resource('static/txts/starships.txt') as txt:
        json_str = txt.read()
        data = json.loads(json_str)
    return render_template(
        "public/templates/starships.html",
        starships=data,
        current=current
    )

@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    """ Sign up page (remove lately) """
    if request.method == "POST":
        req = request.form

        print(req)
        username = req["username"]
        email = req.get("email")
        password = request.form["password"]
        print(username, email, password)

        return redirect(request.url)

    return render_template("public/templates/sign_up.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    """ Search data in json txt """
    if request.method == "POST":
        req = request.form
        search_str = req["search"]
        print(search_str)
        with app.open_resource('static/txts/characters.txt') as txt:
            json_str = txt.read()
            data = json.loads(json_str) 
            for d in data:
                if search_str == d["name"]:
                    print(d)
                    return render_template("public/templates/public_template.html", 
                                           characters=d,
                                           current='Characters'
                                           )
                return render_template("public/templates/public_template.html", error="Not Found")
        return redirect(request.url)

    return render_template("public/templates/public_template.html")
