from bottle import get, post, request, run, template, static_file, error # or route
import databaseOperation
import jwt
import getForm


def check_login(user_email):
    user = databaseOperation.select_user_by_email(user_email)
    if user == None:
        print("check None")
        return user
    if user_email == user[1]:
        print("check True")
        return user

def validateToken(token):
    signature = 'secret'
    try:
        decoded_token = jwt.decode(token, signature)
        return True
    except (jwt.InvalidSignatureError, jwt.exceptions.DecodeError):
        return False

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
    # user = databaseOperation.select_user_by_email('a@a.com')
    # print(user[1], user[2])
    return '''
        <form action="/login" method="POST">
            Email: <input email="email" type="text" />
            Password: <input password="password" type="password" />
            <input value="Login" type="submit" />
        </form>'''


#password has no use here, bc it is not in sqlite database, therefore 
#this route will give you user information asa the email adress is founded
@post('/login') # or @route('/login', method='POST')
def do_login():
    email = request.forms.get("email")
    password = request.forms.get("password")
    user = check_login(email)
    if user != None:
        print(user)
        return template('Your information: {{user_data}}', user_data=user)
        # "<p>Your login information was correct.{{usernmae}}</p>"
    else:
        return "<p>Login failed.</p>"

@get('/get-user-balance') # or @route('/login')
def send_token():
    return '''
        <form action="/get-user-balance" method="POST">
            username: <input name="username" type="text" />
            token: <input name="token" type="text" />
            <input value="send" type="submit" />
        </form>'''

@post('/get-user-balance')
def check_token():
    username = request.forms.get("username")
    token = request.forms.get("token")
    if validateToken(token) == True:
        user = databaseOperation.select_user_by_email(username)
        if user == None:
            return template("User {{thisUser}} is not found.", thisUser=username)
        else:
            return template("User {{thisUser}} has balance {{balance}}.", thisUser=username, balance=user[2])
    else:
        return "<p>sorry, can't find your information</p>"

# https://w3certified.com/easyid/easyid-form.php
# http://80.210.70.4:3333/easyid-form.php
@get('/get-form') # or @route('/login')
def getFormContent():
    return static_file("loginForm.html", root="./static", mimetype='text/html')
    # return '''
    # <body>
    # <h1 id="demo"> SKAT </h1><br>
    # <iframe src="http://80.210.70.4:3333/easyid-form.php" width="300" height="350" frameborder="0" allowfullscreen>
    # </iframe>
    # <p id="customerMsg"></p>
    # </body>

    # <script>
    #     if (window.addEventListener) {
    #         window.addEventListener("message", onMessage, false);        
    #     } 
    #     else if (window.attachEvent) {
    #         window.attachEvent("onmessage", onMessage, false);
    #     }

    #     function onMessage(event) {
    #         // Check sender origin to be trusted
    #         if (event.origin !== "http://80.210.70.4:3333") return;

    #         var data = event.data;

    #         if (typeof(window[data.func]) == "function") {
    #             window[data.func].call(null, data.message);
    #         }
    #     }

    #     // Function to be called from iframe
    #     function parentFunc(message) {
    #         alert(message);
    #         loadDoc(message);
    #     }

    #     function loadDoc(message) {
    #         document.getElementById("customerMsg").innerHTML = message;
    #     }

    # </script>
    # '''

@get('/test-js')
def testJs():
    return static_file("testHtml.html", root="./static")

@error(403)
def mistake(code):
    return 'The parameter you passed has the wrong format!'

run(host='localhost', port=8000)