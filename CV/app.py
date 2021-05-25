from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/main', methods=['PUT', 'POST', 'GET'])
@app.route('/', methods=['GET', 'POST', 'DELETE', 'PUT'])
def home():
    return render_template('cv.html')

@app.route('/ContactList.html', methods=['GET', 'POST', 'DELETE', 'PUT'])
def my_contactList():
    return render_template('ContactList.html')

@app.route('/assignment8', methods=['GET', 'POST', 'DELETE', 'PUT'])
def my_assignment8():
    contact_user = {'firstname': 'Ran', 'lastname': 'Briga'}
    hobbies=['FreeDiving', 'Football', 'Guitar']
    return render_template('assignment8.html',
                           hobbies=hobbies,
                           contact_user=contact_user)


if __name__ == '__main__':
    app.run(debug=True)
