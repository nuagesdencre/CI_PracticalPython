import os
from flask import Flask, render_template, request, redirect, session, url_for
from leaderboard import Leaderboard
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)

game_leaderboard = Leaderboard()


@app.before_request
def session_status():
    """
    Makes the session last until the visitor decides otherwise ( via 'drop' option)
    """
    session.permanent = True


@app.route('/')
def index():
    """
    Home page
    Where the visitor is invited to start the game or to return to their current 'version' of the story
    """
    if 'username' in session:
        return render_template("index.html", page_title="Home", username=session['username'])
    return render_template("index.html", page_title="Home", username="...whoever you are")


@app.route('/drop')
def drop():
    """
    A way to get rid of the information in memory to trigger a 'new' version of the story, while registering
    the previously inputted user information for the leaderboard.
    """
    current_player = {"username": session.get('username'),
                      "riddle_status": session.get('riddle_solved'), 'color': session.get('color'),
                      'mystical': session.get('mystical'),
                      "time_start": session.get('time_start', '---'), "time_stop": session.get('time_stop', '---')}
    game_leaderboard.add_player(current_player)
    session.pop('username', None)
    session.pop('color', None)
    session.pop('mystical', None)
    session.pop('time_start', None)
    session.pop('time_stop', None)
    session.pop('riddle_solved', None)
    return redirect(url_for('index'))


@app.route('/about')
def about():
    """
    Where information about the type of game, the rules of the game and the contact information can be found
    """
    return render_template("about.html", page_title="About")


@app.route('/game')
def game():
    """
     Where game information is offered via a drop-down menu, letting the reader play, access the leaderboard
     or access the about page
    """
    return render_template("game.html", page_title="Game")


@app.route('/leaderboard')
def leaderboard():
    """
    Where the reader can track their details and progress in the story (i.e. session information and riddle status).
    The leaderboard will display maximum 4 records at a time, including the current player's details.
    The leaderboard's logic is in the leaderboard.py file.
    """
    username = session.get('username', 'Potato')
    color = session.get('color', 'purple')
    mystical_beast = session.get('mystical', 'flying pig')
    riddle_solved = session.get('riddle_solved', 'Unsolved')
    time_start = session.get('time_start', '---')
    time_stop = session.get('time_stop', '---')
    return render_template("leaderboard.html", page_title="Leaderboard", leaderboard=game_leaderboard.data,
                           leaders=game_leaderboard.get_leaders(), username=username,
                           color=color, mystical=mystical_beast, riddle_solved=riddle_solved, time_start=time_start,
                           time_stop=time_stop)


@app.route('/play')
def play():
    """
    Where the reader is invited to provide their information and begin the story or return to its current playthrough
    """
    if 'username' in session:
        return redirect(url_for('story'))
    else:
        return render_template("play.html", page_title="Play")


@app.route('/story', methods=['GET', 'POST'])
def story():
    """
    Where the reader begins the story and their details are included for a personalised experience
    """
    if 'username' in session:
        username = session.get('username')
        color = session.get('color')
        mystical_beast = session.get('mystical')
    else:
        username = request.form['username']
        session['username'] = username
        color = request.form['color'].lower()
        session['color'] = color
        mystical_beast = request.form['mystical'].lower()
        session['mystical'] = mystical_beast
    return render_template("story/story.html", page_title="story", username=username, color=color,
                           mystical=mystical_beast)


@app.route('/part1')
def part1():
    """
    The first part of the story, where the first timestamp is recorded
    """
    session['time_start'] = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    return render_template("story/part1.html", page_title="Entering the house")


@app.route('/part2')
def part2():
    """
    The second part of the story
    """
    return render_template("story/part2.html", page_title="First glance")


@app.route('/part3')
def part3():
    """
    The third part of the story
    """
    session['attempts'] = 1
    return render_template("story/part3.html", page_title="Further in")


@app.route('/final', methods=['GET', 'POST'])
def final():
    """
    Where the reader has to provide an answer to the riddle and the second timestamp is recorded
    - multiple answers are possible and the reader is either invited to start again or go to the leaderboard
    following their input
    """
    session['answer1'] = 'chessboard table'
    session['answer2'] = 'chessboard drawer'
    session['answer3'] = 'chess table'
    session['time_stop'] = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    answer_to_riddle = str(request.form['answer_to_riddle']).lower() if 'answer_to_riddle' in request.form else None
    if request.method == 'POST':
        session['attempts'] += 1
        if answer_to_riddle == session['answer1'] or answer_to_riddle == session['answer2'] \
                or answer_to_riddle == session['answer3']:
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
    """
    Custom error page
    """
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=int(os.environ.get('PORT', 5000)))
