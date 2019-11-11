from bottle import get, post, request, run, template # or route
import databaseOperation
import jwt

@get('/login') # or @route('/login')
def login():
    # bottleTest.importTest("Test import module..")
    user = databaseOperation.select_user_by_email('a@a.com')
    print(user[1], user[2])
    return '''
        <form action="/login" method="POST">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>'''

def check_login(usernanme, password):
    if usernanme == 'lei' and password == '123':
        return True
    else:
        return False

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get("username")
    password = request.forms.get("password")
    if check_login(username, password):
        print(username)
        return template('Your information: {{name}}', name=username)
        # "<p>Your login information was correct.{{usernmae}}</p>"
    else:
        return "<p>Login failed.</p>"

@get('/token') # or @route('/login')
def send_token():
    return '''
        <form action="/token" method="POST">
            username: <input name="username" type="text" />
            token: <input name="token" type="text" />
            <input value="send" type="submit" />
        </form>'''

def validateToken(token):
    signature = 'secret'
    try:
        decoded_token = jwt.decode(token, signature)
        return True
    except jwt.InvalidSignatureError:
        return False

@post('/token')
def check_token():
    username = request.forms.get("username")
    token = request.forms.get("token")
    if validateToken(token):
        user = databaseOperation.select_user_by_email(username)
        return template("User {{thisUser}} has balance {{balance}}.", thisUser=username, balance=user[2])
    else:
        return template("sorry, can't find your information")
    


run(host='localhost', port=8000)