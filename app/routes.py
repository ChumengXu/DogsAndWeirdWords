# coding: utf-8
from flask import render_template
from app import app
import random
import requests

FunnyWords = [
                "Lickety-split — ASAP",
                "Mollycoddle — To treat someone in a pampered manner.",
                "Mugwump — A person who is aloof or truly independent in political matters.",
                "Collop — A slice of roasted meat.",
                "Namby-pamby — A person lacking energy and courage.",
                "Ornery — Crabby.",
                "Pettifogger — An inferior lawyer with dubious practices.",
                "Rigmarole — A long, rambling statement.",
                "Collywobbles — Anxiety and stomach queasiness.",
                "Smellfungus — A habitual fault-finder."
            ]

@app.route('/')
@app.route('/health')
def healthCheck():
    return "All good."

@app.route('/dogsmakepeoplehappy')
def dogsMakePeopleHappy():
    caption = getCaption()
    img = getImage()
    print(img)
    return render_template('index.html', caption = caption, img = img)

def getImage():
    headers = {'content-type': 'application/json'}
    response = requests.get("https://dog.ceo/api/breeds/image/random", headers = headers, timeout = 1 )
    if response.status_code == requests.codes.ok:
        print(response.json())
        return response.json()["message"]
    return ""

def getCaption():
    captionIndex = random.randint(0,9)
    return FunnyWords[captionIndex]
    