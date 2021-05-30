from flask import Flask, redirect, url_for, render_template, request, session
from flask import render_template

app = Flask(__name__)


@app.route('/main', methods=['PUT', 'POST', 'GET'])
@app.route('/', methods=['GET', 'POST', 'DELETE', 'PUT'])
def home():
    return render_template('cv.html')

MyUsers = {
    "Tal123": {"firstName": "Tal", "lastName": "Elbaz", "email": "talel@gmail.com", "password": "1111"},
    "Dana123": {"firstName": "Dana", "lastName": "Briga", "email": "danabr@gmail.com", "password": "1212"},
    "Gal123": {"firstName": "Gal", "lastName": "Briga", "email": "galbr@gmail.com", "password": "1313"},
    "Ran123": {"firstName": "Ran", "lastName": "Briga", "email": "ranbr@gmail.com", "password": "1414"},
    "Ido123": {"firstName": "Ido", "lastName": "Perchik", "email": "idoper@gmail.com", "password": "1515"}
}

@app.route('/ContactList.html', methods=['GET', 'POST', 'DELETE', 'PUT'])
def my_contactList():
    return render_template('ContactList.html')

@app.route('/assignment8.html', methods=['GET', 'POST', 'DELETE', 'PUT'])
def my_assignment8():
    contact_user = {'firstname': 'Ran', 'lastname': 'Briga'}
    hobbies=['FreeDiving', 'Football', 'Guitar']
    return render_template('assignment8.html',
                           hobbies=hobbies,
                           contact_user=contact_user)

@app.route('/assignment9', methods=['GET', 'POST', 'DELETE', 'PUT'])
def assignment9():
    if 'loggedIn' not in session:
        session['loggedIn'] = False
        session['username'] = ''
    if request.method == 'GET':
        if request.args:
            if "username" in request.args:
                SearchUser = request.args["username"]
                if SearchUser != '' and SearchUser in MyUsers:
                    return render_template("assignment9.html", username=SearchUser, users=MyUsers[SearchUser], found=True, search=True)
                elif SearchUser != '' and SearchUser not in MyUsers:
                    return render_template("assignment9.html", found=False, search=True)
                else:
                    return render_template("assignment9.html", users=MyUsers, search=True)
            else:
                return render_template("assignment9.html", search=False)
        else:
            return render_template("assignment9.html")
    elif request.method == 'POST':
        if request.form['username'] not in MyUsers:
            MyUsers[request.form['username']] = {"firstName": request.form['firstname'], "email": request.form['email'],
                                                  "password": request.form['password']}
            session['loggedIn'] = True
            session['username'] = request.form['username']
            return render_template("assignment9.html")
        else:
            session['loggedIn'] = False
            return render_template("assignment9.html", exists=True)

if __name__ == '__main__':
    app.run()
