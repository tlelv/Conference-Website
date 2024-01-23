import csv
import sqlite3

class Nominee:
    def __init__(self, nomDictionary):
        for key in nomDictionary:
            setattr(self, key, nomDictionary[key])

con = sqlite3.connect("conference.sqlite")
cursor = con.cursor()

nominee_list = []

query = '''CREATE TABLE IF NOT EXISTS nominees
    (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        name        TEXT,
        description TEXT,
        image_file  TEXT,
        total_votes INTEGER
    )'''

cursor.execute(query)
with open('database_code/awards.csv') as csvInputFile:
    nomReader = csv.DictReader(csvInputFile, delimiter=',')
    for nom in nomReader:
        this_nominee = Nominee(nom)
        nominee_list.append(this_nominee)

for person in nominee_list:
    cursor.execute(
        "INSERT INTO nominees "
        "(name, description, image_file, total_vote)"
        "VALUES (?,?,?,?) ", person.name, person.description, person.image_file, person.total_vote
    )
con.commit()

