from app import application,database

from flask import render_template, session

@application.route('/dashboard', methods=['GET'])
def dashboard():
    print(session['uid'])
    medicines = database.get_medicine()
    print(medicines['msg'])
    return render_template("dashboard.html", medicines = medicines['msg'])