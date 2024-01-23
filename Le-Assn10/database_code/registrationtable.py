# Registration table

import csv
import sqlite3


class Registrant:
    def __init__(self, regDictionary):
        for key in regDictionary:
            setattr(self, key, regDictionary[key])


con = sqlite3.connect("conference.sqlite")
cur = con.cursor()

registrants_list = []

with open('registrant_data.csv') as csvInputFile:
    regReader = csv.DictReader(csvInputFile, delimiter=',')
    for reg in regReader:
        this_registrant = Registrant(reg)
        registrants_list.append(this_registrant)

for person in registrants_list:
    cur.execute("INSERT INTO registrants ('date','title','firstname','lastname','address1','address2',"
                "'city','state','zipcode','telephone','email','web','position','company','meal','billingfirstname',"
                "'billinglastname','cardtype','cardnumber','ccv','expyear','expmonth','session1','session2','session3')"
                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (person.registration_date, person.title,
                                                                               person.firstname, person.lastname,
                                                                               person.address1, person.address2,
                                                                               person.city,
                                                                               person.state, person.zipcode,
                                                                               person.telephone,
                                                                               person.email, person.web,
                                                                               person.position,
                                                                               person.company, person.meal,
                                                                               person.billingfirstname,
                                                                               person.billinglastname, person.cardtype,
                                                                               person.cardnumber, person.ccv,
                                                                               person.expyear,
                                                                               person.expmonth, person.session1,
                                                                               person.session2,
                                                                               person.session3))
con.commit()
