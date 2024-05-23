from flask import render_template, jsonify
from sqlalchemy import case, select, literal

from app import app
from app.models import *
from sqlalchemy.orm import aliased
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


@app.route('/locations')
def locations():
    results = db.session.query(
        Location.name.label('location_name'),
        Location.location,
        Location.description.label('location_description'),
        Location.cost,
        AdvertisementType.name.label('ad_type_name'),
        AdvertisementType.description.label('ad_type_description')
    ).join(AdvertisementType, Location.type_code == AdvertisementType.code).all()

    return render_template('locations.html', results=results)


@app.route('/orders', methods=['GET'])
def get_orders():
    orders = db.session.query(
        Order.id,
        Order.order_date,
        Order.start_date,
        Order.end_date,
        Customer.full_name.label('customer_name'),
        Location.name.label('location_name'),
        Employee.full_name.label('employee_name'),
        AdditionalService.name.label('service1_name'),
        case([(Order.service2_code != None, AdditionalService.name)], else_=literal("None")).label('service2_name'),
        case([(Order.service3_code != None, AdditionalService.name)], else_=literal("None")).label('service3_name'),
        Order.cost,
        Order.payment_mark
    ).join(Customer, Order.customer_code == Customer.code
    ).join(Location, Order.location_code == Location.code
    ).join(Employee, Order.employee_code == Employee.code
    ).outerjoin(AdditionalService, Order.service1_code == AdditionalService.code
    ).all()

    orders_list = []
    for order in orders:
        orders_list.append({
            'id': order.id,
            'order_date': order.order_date,
            'start_date': order.start_date,
            'end_date': order.end_date,
            'customer_name': order.customer_name,
            'location_name': order.location_name,
            'employee_name': order.employee_name,
            'service1_name': order.service1_name,
            'service2_name': order.service2_name,
            'service3_name': order.service3_name,
            'cost': order.cost,
            'payment_mark': order.payment_mark
        })

    return jsonify(orders_list)

@app.route('/check_orders')
def check_orders():
    results = db.session.query(
        Syka.id,
        Customer.full_name.label("name"),
        Location.name.label("bla"),
        Employee.full_name.label("qqq"),
        AdditionalService.name.label("qeer"),
    ).join(Customer, Syka.customer_code == Customer.code)\
        .join(Location, Syka.location_code == Location.code)\
        .join(Employee, Syka.employee_code == Employee.code)\
        .outerjoin(AdditionalService, Syka.service1_code == AdditionalService.code).all()
    print(results)
    return render_template('check.html', results=results, title='Заказы')
