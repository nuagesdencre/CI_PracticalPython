import os
import json
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


def write_to_file(filename, data):
    with open(filename, "a") as file:
        file.writelines(data)


@app.route('/')
def index():
    username = 'Visitor'
    return render_template("index.html", page_title="Home", username=username)


@app.route('/about')
def about():
    return render_template("about.html", page_title="About")


@app.route('/game')
def game():
    return render_template("game.html", page_title="Game")

@app.route('/play')
def play():
    return render_template("play.html", page_title="Play")


@app.route('/rules')
def rules():
    return render_template("rules.html", page_title="Rules")


@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html", page_title="Leaderboard")


@app.route('/login')
def login():
    return render_template("login.html", page_title="Login")


@app.route('/logged')
# live session
def logged():
    username = request.args.get('username')
    return render_template("logged.html", page_title="Logged", username=username)


@app.route('/contact')
def contact():
    return render_template("contact.html", page_title="Contact")


@app.errorhandler(404)
def page_not_found(err):
    return render_template("404.html"),404


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
