from bottle import post, request, run
import jwt


@post("/username/:name")
def log():
    name = request.body.read()
    print(name)

def importTest(text):
    print(text)

def test(a):
    if a == 1:
        return "hI"
    else:
        return "Ho"

print(test(1))
print(test(2))