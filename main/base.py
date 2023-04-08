from flask import Flask, request, redirect,url_for, render_template
from pymongo import MongoClient
from uuid import uuid4
from constants import mongodb, client, database, users_collection

app = Flask(__name__)

class Music():
    def __init__(self, id, name, author, album, lenght):
        self.id = int(id)
        self.name = str(name)
        self.author = str(author)
        self.album = str(album)
        self.lenght = float(lenght)

base_id = int(0)
random_id = int(uuid4())

music = [
    Music(random_id, "Romantic Devil", "Coldin", "Romantic Devil(From Sematic Error)", 3.07),
    Music(random_id, "Gravity", "EXO", "LOVE SHOT", 3.54),
    Music(random_id, "Rush Hour", "Monsta X", "NO LIMIT", 3.22),
    Music(random_id, "Wish You Were Here", "SuperM","Super One", 3.12),
    Music(random_id, "You Calling My Name", "GOT7", "Call My Name", 3.14),
    Music(random_id, "You Problem", "Monsta X", "The Dreaming", 3.19),
    Music(random_id, "One (Monster & Infinity)", "SuperM", "Super One",3.41),
    Music(random_id, "Hair Cut - inst.", "Xdinary Heroes", "Overload",3.25),
    Music(random_id, "Teenager", "Got7", "7 for 7", 3.09)
]

new_music = {
   "_id": format(base_id),
   "name": "Romantic Devil",
   "author": "Coldin",
   "album": "Romantic Devil(From Sematic Error)",
   "lenght_minuts": 3,
   "lenght_seconds": 7
}

@app.route("/")
def index():
    return render_template("base.html", music=music)