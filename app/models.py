from sqlalchemy.orm import relationship

from app import db

class Employee(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    position_code = db.Column(db.String(10), db.ForeignKey('position.code'), nullable=False)

    position = relationship("Position", backref="employee", foreign_keys=[position_code])

class Position(db.Model):
    code = db.Column(db.String(10), primary_key=True)


# class Employee(db.Model):
#     code = db.Column(db.Integer, primary_key=True)
#     full_name = db.Column(db.String(100), nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#     gender = db.Column(db.String(10), nullable=False)
#     address = db.Column(db.String(200), nullable=False)
#     phone = db.Column(db.String(20), nullable=False)
#     passport_data = db.Column(db.String(100), nullable=False)
#     position_code = db.Column(db.String(10), db.ForeignKey('position.code'), nullable=False)
#
# class Position(db.Model):
#     code = db.Column(db.String(10), primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     salary = db.Column(db.Float, nullable=False)
#     duties = db.Column(db.Text, nullable=False)
#     requirements = db.Column(db.Text, nullable=False)
#
# class AdvertisementType(db.Model):
#     code = db.Column(db.String(10), primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.Text, nullable=False)
#
# class AdditionalService(db.Model):
#     code = db.Column(db.String(10), primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.Text, nullable=False)
#     cost = db.Column(db.Float, nullable=False)
#
# class Location(db.Model):
#     code = db.Column(db.String(10), primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     location = db.Column(db.String(200), nullable=False)
#     type_code = db.Column(db.String(10), db.ForeignKey('advertisement_type.code'), nullable=False)
#     description = db.Column(db.Text, nullable=False)
#     cost = db.Column(db.Float, nullable=False)
#
# class Customer(db.Model):
#     code = db.Column(db.String(10), primary_key=True)
#     full_name = db.Column(db.String(100), nullable=False)
#     address = db.Column(db.String(200), nullable=False)
#     phone = db.Column(db.String(20), nullable=False)
#
# class Order(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     order_date = db.Column(db.Date, nullable=False)
#     start_date = db.Column(db.Date, nullable=False)
#     end_date = db.Column(db.Date, nullable=False)
#     customer_code = db.Column(db.String(10), db.ForeignKey('customer.code'), nullable=False)
#     location_code = db.Column(db.String(10), db.ForeignKey('location.code'), nullable=False)
#     service1_code = db.Column(db.String(10), db.ForeignKey('additional_service.code'))
#     service2_code = db.Column(db.String(10), db.ForeignKey('additional_service.code'))
#     service3_code = db.Column(db.String(10), db.ForeignKey('additional_service.code'))
#     cost = db.Column(db.Float, nullable=False)
#     payment_mark = db.Column(db.Boolean, nullable=False)
#     employee_code = db.Column(db.String(10), db.ForeignKey('employee.code'), nullable=False)
