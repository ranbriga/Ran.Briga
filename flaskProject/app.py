from flask import Flask, redirect, url_for, render_template, request, session, jsonify
from flask import render_template

app = Flask(__name__)


@app.route('/main', methods=['PUT', 'POST', 'GET'])
@app.route('/', methods=['GET', 'POST', 'DELETE', 'PUT'])
def home():
    return render_template('cv.html')

app.secret_key ='6595'

MyUsers = {
    "Tal123": {"firstName": "Tal", "lastName": "Elbaz", "email": "talel@gmail.com"},
    "Dana123": {"firstName": "Dana", "lastName": "Briga", "email": "danabr@gmail.com"},
    "Gal123": {"firstName": "Gal", "lastName": "Briga", "email": "galbr@gmail.com"},
    "Ran123": {"firstName": "Ran", "lastName": "Briga", "email": "ranbr@gmail.com"},
    "Ido123": {"firstName": "Ido", "lastName": "Perchik", "email": "idoper@gmail.com"}
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

@app.route('/assignment9.html', methods=['GET', 'POST', 'DELETE', 'PUT'])
def my_assignment9():
    if request.method == 'GET':
        if request.args:
            if "username" in request.args:
                SearchUser = request.args["username"]
                if SearchUser in MyUsers and SearchUser != '':
                    return render_template("assignment9.html", username=SearchUser, users=MyUsers[SearchUser], found=True, search=True)
                elif SearchUser not in MyUsers and SearchUser != '':
                    return render_template("assignment9.html", found=False, search=True)
                else:
                    return render_template("assignment9.html", users=MyUsers, search=True)
            else:
                return render_template("assignment9.html", search=False)
        else:
            return render_template("assignment9.html")
    elif request.method == 'POST':
        if not session.get('loggedIn'):
            if request.form['username'] not in MyUsers:
                MyUsers[request.form['username']] = {"firstName": request.form['firstname'], "lastName": request.form['lastname'],
                                                     "email": request.form['email']}
                session['loggedIn'] = True
                session['username'] = request.form['username']
                return render_template("assignment9.html", exists=False)
            if request.form['username'] in MyUsers:
                session['loggedIn'] = False
                return render_template("assignment9.html", exists=True)
        else:
            session['loggedIn'] = False
            return render_template("assignment9.html")


from assignment10.assignment10 import assignment10, interact_db

app.register_blueprint(assignment10)


# assigment 11

@app.route('/assignment11/users', methods=['GET'])
def assignment11():
    query = "SELECT * FROM userss "
    query_result = interact_db(query, query_type='fetch')
    return jsonify(users=query_result)


@app.route('/assignment11/users/selected/', defaults={'SOME_USER_ID': 1})
@app.route('/assignment11/users/selected/<int:SOME_USER_ID>')
def get_user(SOME_USER_ID):
    if SOME_USER_ID:
        query = "SELECT * FROM users WHERE id='%s'" % SOME_USER_ID
        query_result = interact_db(query, query_type='fetch')
        if len(query_result) != 0:
            return jsonify(query_result)
    return jsonify({'success': False, 'error': 'Unfortunately the user is not exist'})


if __name__ == '__main__':
    app.run()
