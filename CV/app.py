from flask import Flask, url_for, redirect
from flask import render_template

app = Flask(_name_)

@app.route('/', methods=['GET', 'POST', 'DELETE', 'PUT'])
def home():
    return render_template('cv.html')

@app.route('/ContactList', methods=['GET', 'POST', 'DELETE', 'PUT'])
def my_contactList():
    return render_template('ContactList.html')

@app.route('/HomeWork8', methods=['GET', 'POST', 'DELETE', 'PUT'])
def hello_HomeWork8():
    return render_template('HomeWork8.html',
                           user={'name': "Ran Briga"},
                           hobbies=['FreeDiving', 'Football', 'Guitar'])

@app.route('/howAreYou')
def hay():
    return 'hello there! how are you? '
    
@app.route('/nicetomeetyou')
def hello():
    return redirect('/howAreYou')

@app.route('/goHome')
def goMain():
 return redirect(url_for('main'))

if _name_ == '_main_':
    app.run()
