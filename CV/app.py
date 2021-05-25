from flask import Flask, url_for, redirect
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'DELETE', 'PUT'])
def home():
    return render_template('cv.html')

@app.route('/ContactList', methods=['GET', 'POST', 'DELETE', 'PUT'])
def my_contactList():
    return render_template('ContactList.html')

@app.route('/assignment8', methods=['GET', 'POST', 'DELETE', 'PUT'])
def my_assignment8():
    return render_template('assignment8.html',
                           user={'name': "Ran Briga"},
                           hobbies=['FreeDiving', 'Football', 'Guitar'])


if __name__ == '__main__':
    app.run()
