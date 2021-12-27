from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route('/')
def lvl1():
    return render_template('index.html', num=3, color="blue")


@app.route('/game')
def game_time():
    return render_template('game.html')


@app.route('/list')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name': 'Michael', 'age': 35},
        {'name': 'John', 'age': 30},
        {'name': 'Mark', 'age': 25},
        {'name': 'KB', 'age': 27}
    ]
    return render_template("list.html", random_numbers=[3, 1, 5], students=student_info)


if __name__ == "__main__":
    app.run(debug=True)
