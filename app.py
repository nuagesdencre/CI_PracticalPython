import os
from flask import Flask, render_template, request, redirect, flash, session, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.before_request
def session_status():
    # makes the session last unless requested otherwise
    session.permanent = True


@app.route('/')
def index():
    if 'username' in session:
        return render_template("index.html", page_title="Home", username=session['username'])
    return render_template("index.html", page_title="Home", username="...whoever you are")


@app.route('/drop')
def drop():
    session.pop('username', None)
    session.pop('color', None)
    session.pop('mystical', None)
    session.pop('time_start', None)
    session.pop('time_stop', None)
    session.pop('riddle_solved', None)
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template("about.html", page_title="About")


@app.route('/game')
def game():
    return render_template("game.html", page_title="Game")


@app.route('/leaderboard', methods=['GET', 'POST'])
def leaderboard():
    if request.method == 'GET':
        username = session['username'] if 'username' in session else 'Potato'
        color = session['color'] if 'color' in session else 'Magenta'
        mystical_beast = session['mystical'] if 'mystical' in session else 'Porcupine'
        riddle_solved = session['riddle_solved'] if 'riddle_solved' in session else 'Unsolved'
        time_start = session['time_start'] if 'time_start' in session else '---'
        time_stop = session['time_stop'] if 'time_stop' in session else '---'
        return render_template("leaderboard.html", page_title="Leaderboard", username=username, color=color,
                               mystical=mystical_beast, riddle_solved=riddle_solved, time_start=time_start,
                               time_stop=time_stop)

    # return render_template("leaderboard.html", page_title="Leaderboard", username='Nobody', color='green',
    #                                mystical='bear', riddle_solved='solved')
    # username, umbrella color, has a secret tattoo of, riddle solved, timestamp in/out
    # username, color, mystical_beast, riddle_solved, (duration)


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
        if 'time_start' in session:
            time_start = session['time_start']
        else:
            session['time_start'] = datetime.now().strftime('%Y/%m/%d, %H:%M:%S')
        color = request.form['color']
        session['color'] = color
        mystical_beast = request.form['mystical']
        session['mystical'] = mystical_beast
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
    session['attempts'] = 1
    return render_template("story/part3.html", page_title="Further in")


@app.route('/final', methods=['GET', 'POST'])
def final():
    session['answer'] = 'chessboard'
    session['time_stop'] = datetime.now().strftime('%Y/%m/%d, %H:%M:%S')
    answer_to_riddle = str(request.form['answer_to_riddle']).lower() if 'answer_to_riddle' in request.form else None
    if request.method == 'POST':
        session['attempts'] += 1
        if answer_to_riddle == session['answer']:
            session['riddle_solved'] = 'Solved'
            return render_template('story/final.html', attempts=session['attempts'], answer_to_riddle=answer_to_riddle,
                                   status="Spot on.")
        else:
            session['riddle_solved'] = 'Unsolved'
            return render_template('story/final.html', attempts=session['attempts'], answer_to_riddle=answer_to_riddle,
                                   status='Not quite.')

    return render_template("story/final.html", attempts=session['attempts'], status="What do you think?",
                           answer_to_riddle=answer_to_riddle, page_title="Elementary")


@app.errorhandler(404)
def page_not_found(err):
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
