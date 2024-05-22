from flask import render_template
from app import app
from app.models import *

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/staff')
def staff():
    results = db.session.query(
        Employee.full_name,
        Employee.age,
        Employee.gender,
        Employee.address,
        Employee.phone,
        Employee.passport_data,
        Position.name.label('position_name'),
        Position.salary
    ).join(Position, Employee.position_code == Position.code).all()

    return render_template('staff.html', results=results)