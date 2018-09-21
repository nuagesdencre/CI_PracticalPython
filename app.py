import os
from flask import Flask, render_template, request, redirect, flash, session, url_for


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    if 'username' in session:
        return render_template("index.html", page_title="Home", username=session['username'])
    return render_template("index.html", page_title="Home", username="...whoever you are")


@app.route('/about')
def about():
    return render_template("about.html", page_title="About")


@app.route('/game')
def game():
    return render_template("game.html", page_title="Game")


@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html", page_title="Leaderboard")


@app.route('/play')
# , methods=['POST', 'GET']
def play():
    # if request.method == 'POST':
    #     session['username'] = request.form['username']
    #     session['color'] = request.form['color']
    #     session['mystical_beast'] = request.form['mystical_beast']
    return render_template("play.html", page_title="Play")


# story path
@app.route('/story/story')
def story():
    username = request.args.get('username')
    color = request.args.get('color')
    mystical_beast = request.args.get('mystical')
    return render_template("story/story.html", page_title="story", username=username, color=color, mystical=mystical_beast)


@app.route('/story/part1')
def part1():
    return render_template("story/part1.html", page_title="Entering the house")

#
# @app.route('/part2')
# def part2():
#     return render_template("part2.html", page_title="First glance")
# @app.route('/part3')
# def part3():
#     return render_template("part3.html", page_title="Further in")
# @app.route('/final')
# def final():
#     return render_template("final.html", page_title="Elementary")

@app.errorhandler(404)
def page_not_found(err):
    return render_template("404.html"),404


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
