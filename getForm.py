import requests
from bs4 import BeautifulSoup

def getContent():
    URL = "https://w3certified.com/easyid/easyid-form.php"
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, "html5lib")
    # print(soup.prettify())

    # return (soup.prettify())

getContent()