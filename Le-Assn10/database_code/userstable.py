import csv
import sqlite3


class User:
    def __init__(self, userDictionary):
        for key in userDictionary:
            setattr(self, key, userDictionary[key])


con = sqlite3.connect("conference.sqlite")
cursor = con.cursor()

user_list = []

query = '''CREATE TABLE IF NOT EXISTS users
    (
        id          INTEGER PRIMARY KEY,
        username    TEXT,
        firstname   TEXT,
        lastname    TEXT,
        password    TEXT
    )'''

cursor.execute(query)
with open('database_code/users.csv') as csvInputFile:
    userReader = csv.DictReader(csvInputFile, delimiter=',')
    for user in userReader:
        this_user = User(user)
        user_list.append(this_user)

for person in user_list:
    cursor.execute(
        "INSERT INTO users "
        "(username, firstname, lastname, password)"
        "VALUES (?,?,?,?) ", person.username, person.firstname, person.lastname, person.password
    )
con.commit()
