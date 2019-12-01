# Our Backend for the App!
# Built with Flask

# Import Flask
import flask
import requests
import json

# Create the application
app = flask.Flask(__name__)

current_user = ''

@app.route('/', methods=['GET'])
def welcome():
    return flask.render_template('login.html')

@app.route('/login', methods=['post'])
def login():

    global current_user

    data = flask.request.form

    username = data['username']
    password = data['password']

    if username is "" or password is "":
        return flask.render_template('badlogin.html')

    with open('accounts.json') as json_file:
        accounts = json.load(json_file)

    for account in accounts:
        if account['username'] == username and account['password'] == password:

            current_user = username

            friend_list = account['friends']

            friend_expenses = {}

            friend_expenses[username] = account['expenses']

            for friend in friend_list:
                for acct in accounts:
                    if acct['username'] == friend:
                        friend_expenses[friend] = acct['expenses']

            return flask.render_template('main.html', friends=friend_expenses)

    return flask.render_template('badlogin.html')


@app.route('/logout', methods=['post'])
def logout():
    global current_user

    current_user = ''

    return flask.render_template('login.html')


@app.route('/addexpense', methods=['post'])
def addexpense():
    global current_user

    data = flask.request.form

    expense = data['addexpense']

    if expense == '':
        return flask.render_template('main.html')

    with open('accounts.json') as json_file:
        accounts = json.load(json_file)

    for account in accounts:
        if account['username'] == current_user:
            account['expenses'] += int(expense)

            with open('accounts.json', 'w') as json_file:
                json.dump(accounts, json_file)

            friend_list = account['friends']

            friend_expenses = {}

            friend_expenses[current_user] = account['expenses']

            for friend in friend_list:
                for acct in accounts:
                    if acct['username'] == friend:
                        friend_expenses[friend] = acct['expenses']

            return flask.render_template('main.html', friends=friend_expenses)

@app.route('/removeexpense', methods=['post'])
def removeexpense():
    global current_user

    data = flask.request.form

    expense = data['removeexpense']

    if expense == '':
        return flask.render_template('main.html')

    with open('accounts.json') as json_file:
        accounts = json.load(json_file)

    for account in accounts:
        if account['username'] == current_user:
            if (account['expenses'] - int(expense)) < 0:
                account['expenses'] = 0
            else:
                account['expenses'] -= int(expense)

            with open('accounts.json', 'w') as json_file:
                json.dump(accounts, json_file)

            friend_list = account['friends']

            friend_expenses = {}

            friend_expenses[current_user] = account['expenses']

            for friend in friend_list:
                for acct in accounts:
                    if acct['username'] == friend:
                        friend_expenses[friend] = acct['expenses']

            return flask.render_template('main.html', friends=friend_expenses)


if __name__ == '__main__':
    app.run(debug=True)
