import os
from flask import Flask, render_template, request, redirect, session, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.before_request
def session_status():
    # makes the session last unless requested otherwise
    session.permanent = True


@app.route('/')
# home page
# where the visitor is invited to start the game or to return to the current playthrough
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


@app.route('/leaderboard')
def leaderboard():
    username = session.get('username', 'Potato')
    color = session.get('color', 'purple')
    mystical_beast = session.get('mystical', 'flying pig')
    riddle_solved = session.get('riddle_solved', 'Unsolved')
    time_start = session.get('time_start', '---')
    time_stop = session.get('time_stop', '---')
    return render_template("leaderboard.html", page_title="Leaderboard", username=username, color=color,
                           mystical=mystical_beast, riddle_solved=riddle_solved, time_start=time_start,
                           time_stop=time_stop)


@app.route('/play')
def play():
    if 'username' in session:
        return redirect(url_for('story'))
    else:
        return render_template("play.html", page_title="Play")


# story path
@app.route('/story', methods=['GET', 'POST'])
def story():
    if 'username' in session:
        username =session.get('username')
        color = session.get('color')
        mystical_beast = session.get('mystical')
    else:
        username = request.form['username']
        session['username'] = username
        color = request.form['color']
        session['color'] = color
        mystical_beast = request.form['mystical']
        session['mystical'] = mystical_beast
    session['time_start'] = datetime.now().strftime('%Y/%m/%d, %H:%M:%S')
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
    session['answer1'] = 'chessboard table'
    session['answer2'] = 'chessboard drawer'
    session['time_stop'] = datetime.now().strftime('%Y/%m/%d, %H:%M:%S')
    answer_to_riddle = str(request.form['answer_to_riddle']).lower() if 'answer_to_riddle' in request.form else None
    if request.method == 'POST':
        session['attempts'] += 1
        if answer_to_riddle == session['answer1'] or answer_to_riddle == session['answer2']:
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
            port=int(os.environ.get('PORT', 5000)))
