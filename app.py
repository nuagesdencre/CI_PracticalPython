import os
from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = os.urandom(24)


#
# session ={}


@app.route('/')
def index():
    if 'username' in session:
        # logout??
        # def dropsession():
        #     session.pop('username', None)
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
def play():
    return render_template("play.html", page_title="Play")


# story path
@app.route('/story', methods=['GET', 'POST'])
def story():
    if request.method == 'POST':
        if 'username' in session:
            username = session['username']
        else:
            username = request.form['username']
            session['username'] = username
        color = request.form['color']
        mystical_beast = request.form['mystical']
        return render_template("story/story.html", page_title="story", username=username, color=color,
                               mystical=mystical_beast)


@app.route('/part1')
def part1():
    return render_template("story/part1.html", page_title="Entering the house")


@app.route('/part2')
def part2():
    return render_template("story/part2.html", page_title="First glance")


@app.route('/part3')
def part3():
    session['answer'] = 'chessboard'
    session['attempts'] = 1
    return render_template("story/part3.html", page_title="Further in")


@app.route('/final', methods=['GET', 'POST'])
def final():
    answer_to_riddle = ''
    if request.method == 'POST':
        if answer_to_riddle == session['answer']:
            session['riddle_solved'] = 'Solved'
            return render_template('story/final.html', status='Spot on.')
        elif answer_to_riddle != session['answer']:
            session['riddle_solved'] = 'Unsolved'
            session['attempts'] += 1
            return render_template('story/final.html', status='Not quite.')
        else:
            session['riddle_solved'] = 'Unsolved'
            return render_template('story/final.html', status='Go back and take another look.')
    return render_template("story/final.html", attempts=session['attempts'], answer_to_riddle=answer_to_riddle,
                           page_title="Elementary")


@app.errorhandler(404)
def page_not_found(err):
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
