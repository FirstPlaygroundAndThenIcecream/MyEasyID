from bottle import get, post, request, run, template, static_file, error # or route
import databaseOperation
import jwt

def check_login(userEmail):
    user = databaseOperation.select_user_by_email(userEmail)
    print('check_login')
    print(user)
    if user == None:
        return None
    if userEmail == user[1]:
        return user

def validateToken(token, signature):
    try:
        decodedToken = jwt.decode(token, signature)
        return True, decodedToken
    except (jwt.InvalidSignatureError, jwt.exceptions.DecodeError):
        return False

@get('/get-form') # or @route('/login')
def getFormContent():
    return static_file("loginForm-bank.html", root="./html", mimetype='text/html')

@get('/get-user-balance')
def decodeAndSeachDB():
    token = request.query.token
    signature = 'example_key'
    result, decodedToken = validateToken(token, signature)
    if result:       
        userEmail = decodedToken['email']
        user = databaseOperation.select_user_by_email(userEmail)
        if user == None:
            return 'Sorry, can not find the user'
        else:
            balance = user[2]           
            msg_str = '<?xml version="1.0" encoding="UTF-8"?><bankInfo><name>%s</name><balance>%s</balance></bankInfo>'%(user[0], user[2])
            # msg = '''
            #     <?xml version="1.0" encoding="UTF-8"?>
            #     <bankInfo>
            #         <name>%s</name>
            #         <balance>%s</balance>
            #     </bankInfo>
            # '''%(user[0], user[2])
            return msg_str 
    else:
        return 'Sorry, you have no right to continue'

@get('/register') # or @route('/login')
def register():
    print("/register")
    return '''
        <form action="/register" method="POST">
            name: <input name="name" type="text" />
            email: <input name="email" type="text" />
            balance: <input name="balance" type="number" />
            <input value="Register" type="submit" />
        </form>'''

@post('/register') # or @route('/login', method='POST')
def do_register():
    name = request.forms.get("name")
    email = request.forms.get("email")
    balance = request.forms.get("balance")
    user_data = (name, email, int(balance))
    print(user_data)
    if check_login(email) == None:
        rowId = databaseOperation.insert_values(user_data)
        print(rowId)
        return template('{{name}} is registered', name=name)
    else:
        return "<p>User of this email is already exist.</p>"

@get('/get-all-users')
def print_all_users():
    users = databaseOperation.select_all_users()
    return template("users are {{users_data}}", users_data=users)


@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="POST">
            Email: <input name="email" type="text" />
            Password: <input name="password" type="password" />
           <input value="Login" type="submit" />
        </form>'''


#should fix: do_login doesn't work if the password field is taken away
@post('/login') # or @route('/login', method='POST')
def do_login():
    email = request.forms.get("email")
    print(email)
    user = check_login(email)
    print(user)
    if user != None:
        print(user)
        return template('Your information: {{user_data}}', user_data=user)
        # "<p>Your login information was correct.{{usernmae}}</p>"
    else:
        return "<p>Login failed.</p>"


@error(403)
def mistake_403(code):
    return 'The parameter you passed has the wrong format!'

@error(404)
def mistake_404(code):
    return "Can't find the page you are looking for, sorry!"


run(host='localhost', port=8000)