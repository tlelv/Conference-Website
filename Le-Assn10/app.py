# Main python file

import sqlite3
import csv
import datetime
from functools import wraps

import app
from flask import Flask, render_template, request, session

app.secret_key = '@#$%sdf34587#$%asdfeFSv'

app = Flask(__name__)


@app.route('/activities')
def display_activities():
    return render_template("activities.html")

def status(func):
    @wraps (func)
    def wrapper_status(*args, **kwargs):
        if 'logged_in' in session:
            print("Logged in")
            return func(*args, **kwargs)
        else:
            return "Sorry, but you cannot access the admin page unless you log in"
    return wrapper_status

@app.route('/admin')
@status
def admin():
    return render_template("admin.html")


@app.route('/awards', methods=['POST','GET'])
def awards():
    thank_you = "Thank you for voting"
    if request.method == 'POST':
        return render_template("awards.html", message=thank_you)
    else:
        return render_template("awards.html")


@app.route('/')
def display_index():
    return render_template("index.html")


@app.route('/keynote')
def display_keynote():
    return render_template("keynote.html")

@app.route('/login', methods=['POST','GET'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    con = sqlite3.connect("conference.sqlite")
    cur = con.cursor()

    cur.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user_data = cur.fetchone()
    if user_data:
        session['logged_in'] = True
        return render_template("admin.html")
    else:
        return render_template("login.html", error="Invalid login")

@app.route('/meals')
def display_meals():
    return render_template("meals.html")


@app.route('/poll')
def poll():
    return render_template("poll.html")


@app.route('/registration', methods=['POST','GET'])
def registration():
    if request.method == 'POST':
        con = sqlite3.connect("conference.sqlite")
        first_name = request.form.get("firstname")
        last_name = request.form.get("lastname")
        address1 = request.form.get("address1")
        address2 = request.form.get("address2")
        city = request.form.get("city")
        state = request.form.get("state")
        zipcode = request.form.get("zipcode")
        telephone = request.form.get("telephone")
        email = request.form.get("email")
        web = request.form.get("web")
        position = request.form.get("position")
        company = request.form.get("company")
        meal = request.form.get("meal")
        billing_first_name = request.form.get("billingfirstname")
        billing_last_name = request.form.get("billinglastname")
        card_type = request.form.get("cardtype")
        card_number = request.form.get("cardnumber")
        ccv_number = request.form.get("ccv")
        exp_year = request.form.get("expyear")
        exp_month = request.form.get("expmonth")
        session1 = request.form.get("session1")
        session2 = request.form.get("session2")
        session3 = request.form.get("session3")

        with open('database_code/registrant_data', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            now = datetime.datetime.now()
            writer.writerow([now.date(),first_name,last_name,address1,address2,city,state,zipcode,telephone,email,web,
                             position,company,meal,billing_first_name,billing_last_name,card_type,card_number,ccv_number,
                             exp_year,exp_month,session1,session2,session3])


        return render_template("thankyou.html", fname=first_name, lname=last_name, address1=address1,
                           address2=address2, city=city, state=state, zip=zipcode, telephone=telephone, email=email,
                           web=web, position=position, company=company, meal=meal, billingfname=billing_first_name,
                           billinglname=billing_last_name, cardtype=card_type, cardnum=card_number, ccv=ccv_number,
                           expyear=exp_year, expmonth=exp_month, session1=session1, session2=session2, session3=session3)
    else:
        return render_template("registration.html")


@app.route('/workshopschedule')
def display_workshopschedule():
    return render_template("workshopschedule.html")


if __name__ == '__main__':
    app.run()
