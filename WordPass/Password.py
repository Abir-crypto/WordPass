import json
import os


global password

password = {}

if os.path.getsize('data.txt') != 0:
    with open('data.txt') as file:
        password = json.load(file)


def add_password(name, paswrd):
    password.update({name: paswrd})
    with open("data.txt", "w") as file:
        json.dump(password, file)


def find_password(name):
    passfound = 0
    for word, pswd in password.items():
        if word == name:
            passfound =1
            return pswd

    if passfound == 0:
        return "No Password"

