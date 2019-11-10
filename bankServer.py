from bottle import Bottle, route, run, template

app = Bottle()

@route('/hello')
def hello():
    return 'hello world'


run(host='localhost', port=8000)