from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKeyConstraint,  UniqueConstraint
from app import db

# class Employee(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     position_code = db.Column(db.String(10), db.ForeignKey('position.code'), nullable=False)
#
#     position = relationship("Position", backref="employee", foreign_keys=[position_code])
#
# class Position(db.Model):
#     code = db.Column(db.String(10), primary_key=True)


class Employee(db.Model):
    code = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    passport_data = db.Column(db.String(100), nullable=False)
    position_code = db.Column(db.String(10), db.ForeignKey('position.code'), nullable=False)
    position = relationship("Position", backref="employee", foreign_keys=[position_code])

class Position(db.Model):
    code = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    duties = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=False)
#
class AdvertisementType(db.Model):
    code = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
#
class AdditionalService(db.Model):
    __table_name__ = "bly"
    code = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    cost = db.Column(db.Float, nullable=False)
#
class Location(db.Model):
    code = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    type_code = db.Column(db.String(10), db.ForeignKey('advertisement_type.code'), nullable=False)
    type_c = relationship("AdvertisementType", backref="Advertisement", foreign_keys=[type_code])
    description = db.Column(db.Text, nullable=False)
    cost = db.Column(db.Float, nullable=False)

class Customer(db.Model):
    code = db.Column(db.String(10), primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

# class Order(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     order_date = db.Column(db.Date, nullable=False)
#     start_date = db.Column(db.Date, nullable=False)
#     end_date = db.Column(db.Date, nullable=False)
#     customer_code = db.Column(db.String(10), db.ForeignKey('customer.code'), nullable=False)
#     customer = relationship("Customer", backref="customer", foreign_keys=[customer_code])
#     location_code = db.Column(db.String(10), db.ForeignKey('location.code'), nullable=False)
#     location = relationship("Location", backref="locations", foreign_keys=[location_code])
#     service1_code = db.Column(db.String(10), db.ForeignKey('bly.code'))
#     service2_code = db.Column(db.String(10))
#     service3_code = db.Column(db.String(10))
#     service = relationship("AdditionalService", backref="service_1", foreign_keys=[service1_code])
#     cost = db.Column(db.Float, nullable=False)
#     payment_mark = db.Column(db.Boolean, nullable=False)
#     employee_code = db.Column(db.String(10), db.ForeignKey('employee.code'), nullable=False)
#     employee = relationship("Employee", backref="employee", foreign_keys=[employee_code])


class Service(db.Model):
    code = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    cost = db.Column(db.Float, nullable=False)


class Syka(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_date = db.Column(db.Date, )
    start_date = db.Column(db.Date, )
    end_date = db.Column(db.Date, )
    customer_code = db.Column(db.String(10), db.ForeignKey('customer.code'), nullable=False)
    customer = relationship("Customer", backref="cust", foreign_keys=[customer_code])
    location_code = db.Column(db.String(10), db.ForeignKey('location.code'))
    location = relationship("Location", backref="loc", foreign_keys=[location_code])
    employee_code = db.Column(db.String(10), db.ForeignKey('employee.code'))
    employee = relationship("Employee", backref="emp", foreign_keys=[employee_code])
    service1_code = db.Column(db.String(10), db.ForeignKey('service.code'))
    service1 = relationship("Service", backref="service", foreign_keys=[service1_code])