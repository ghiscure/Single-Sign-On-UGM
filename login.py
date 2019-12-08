import getpass
import requests
from bs4 import BeautifulSoup
import json
try:
    with open("config.json") as json_data_files:
        json_data = json.load(json_data_files)
        print("open file success")
    data = json_data["credentials"]
    headers_2 = json_data["headers_2"]
    headers_1 = json_data["headers_1"]
except:
    print("open file error")
    pass
username = name = input("username : ")
password = getpass.getpass()
data["username"] = username
data["password"] = password


session = requests.Session()
response = session.get(
    'https://sso.ugm.ac.id/cas/login', headers=headers_1)
cookies = session.cookies.get_dict()
contents = (response.content)

soup = BeautifulSoup(contents, "lxml")
lt = soup.find("input", {'name': "lt"}).attrs['value']

data["lt"] = lt


response = session.post('https://sso.ugm.ac.id/cas/login',
                        headers=headers_2, cookies=cookies, data=data)
print(response.content)
soup = BeautifulSoup(response.content, "lxml")
