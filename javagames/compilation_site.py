from flask import Flask, render_template, redirect, url_for

import game_manager

from random import choice

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('game', id=choice(game_manager.get_valid_game_ids())))

@app.route('/game/<int:id>')
def game(id):
    if int(id) not in game_manager.get_valid_game_ids():
        return "Game ID not found", 404
    return render_template('game.html', game_id=id)

if __name__ == '__main__':
    app.run(debug=True)
