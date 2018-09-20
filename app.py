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
    # to be updated once live session username provided!
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


@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html", page_title="Leaderboard")


# story path
@app.route('/story')
def story():
    username = request.args.get('username')
    color = request.args.get('color')
    mystical=request.args.get('mystical')
    return render_template("story.html", page_title="story", username=username, color=color, mystical=mystical)


@app.route('/part1')
def part1():
    return render_template("part1.html", page_title="Entering the house")


@app.errorhandler(404)
def page_not_found(err):
    return render_template("404.html"),404


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
