import csv
import sqlite3


con = sqlite3.connect("conference.sqlite")
cursor = con.cursor()

query = '''CREATE TABLE IF NOT EXISTS workshops
    (
        name        TEXT,
        session     INTEGER,
        roomnumber   TEXT,
        starttime    TEXT,
        endtime      TEXT
    )'''

cursor.execute(query)

workshop_list = []

with open('users.csv') as csvInputFile:
    workshopReader = csv.DictReader(csvInputFile, delimiter=',')
    for workshop in workshopReader:
        this_workshop = Workshop(workshop)
        workshop_list.append(this_workshop)

for workshop in workshop_list:
    cursor.execute(
        "INSERT INTO workshop"
        "(workshop_title, workshop_session, workshop_roomnumber, workshop_starttime, workshop_endtime)"
        "VALUES (?,?,?,?,?) ", workshop.title, workshop.session, workshop.roomnumber, workshop.starttime, workshop.endtime
    )
con.commit()
