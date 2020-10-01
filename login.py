import getpass
import requests
from bs4 import BeautifulSoup
import json
try:
    with open("config.json") as json_data_files:
        json_data = json.load(json_data_files)
        print("open file success")
    data = json_data["credentials"]
except:
    print("open file error")
    pass


def login():
    username = input("username : ")
    password = getpass.getpass()
    data["username"] = username
    data["password"] = password

    session = requests.Session()
    response = session.get(
        'https://sso.ugm.ac.id/cas/login')
    contents = (response.content)

    soup = BeautifulSoup(contents, "lxml")
    lt = soup.find("input", {'name': "lt"}).attrs['value']

    data["lt"] = lt

    response = session.post('https://sso.ugm.ac.id/cas/login',
                            data=data)
    success = BeautifulSoup(response.text, 'html.parser')
    div_success = success.find("div", attrs={"id": 'msg'})
    # print(div_success)
    if('alert alert-success' in str(div_success)):
        return True
    else:
        return False


if __name__ == "__main__":
    if(login()):
        print("You are logged in")
