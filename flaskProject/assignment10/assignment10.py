from flask import Flask, render_template, request, redirect, Blueprint, session
import mysql.connector

app = Flask(__name__)
app.secret_key = '6595'

assignment10 = Blueprint('assignment10', __name__,
                         static_url_path='/assignment10',
                         template_folder='templates')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='root',
                                         database='assignment10')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit': 
        connection.commit()
        return_value = True
    if query_type == 'fetch': 
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@assignment10.route('/get_users', methods=['GET', 'POST'])
def return_users():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', AllUsers=query_result, GET=True)


@assignment10.route('/insert_user', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        TableQuery = "select username from users"
        TableUsers = interact_db(query=TableQuery, query_type='fetch')
        user_name = request.form['username']
        exist = False
        for v in TableUsers :
            if v[0] == user_name:
                exist = True
        if not exist:
            username = request.form['username']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            query = "INSERT INTO users(username, firstName, lastName, email) VALUES ('%s', '%s', '%s', '%s');" \
                    % (username, first_name, last_name, email)
            interact_db(query=query, query_type='commit')
            return render_template('assignment10.html', req_method=request.method, Inserted=True)
        elif exist:
            return render_template('assignment10.html', req_method=request.method, Inserted=False)


@assignment10.route('/delete_user', methods=['POST'])
def delete_user():
    TableQuery = "select username from users"
    TableUsers = interact_db(query=TableQuery, query_type='fetch')
    user_name = request.form['username']
    exist = False
    for v in TableUsers:
        if v[0] == user_name:
            exist = True
    if not exist:
        return render_template('assignment10.html', req_method=request.method, Deleted=False)
    elif exist:
        check = "SELECT username FROM users WHERE username='%s';" % user_name
        if len(check) != 0:
            query = "DELETE FROM users WHERE username='%s';" % user_name
            interact_db(query=query, query_type='commit')
            return render_template('assignment10.html', req_method=request.method, Deleted=True)
        elif len(check) == 0:
            return render_template('assignment10.html', req_method=request.method, Deleted=False)


@assignment10.route('/update_user', methods=['GET', 'POST'])
def update_user():
    if request.method == 'POST':
        TableQuery = "select username from users"
        TableUsers = interact_db(query=TableQuery, query_type='fetch')
        exist = False
        for v in TableUsers:
            if v[0] == request.form['username']:
                exist = True
        if exist:
            check = "SELECT username FROM users WHERE username='%s';" % request.form['username']
            if len(check) != 0:
                query = "UPDATE users SET firstName='%s', lastName='%s', email='%s' WHERE username='%s';" % \
                        (request.form['first_name'], request.form['last_name'], request.form['email'], request.form['username'])
                interact_db(query=query, query_type='commit')
                return render_template('assignment10.html', req_method=request.method, Updated=True)
        elif not exist:
            return render_template('assignment10.html', req_method=request.method, Updated=False)


@assignment10.route('/assignment10.html')
def my_assignment10():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', TableUsers=query_result)
