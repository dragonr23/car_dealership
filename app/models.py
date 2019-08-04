from app import app, db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Product(db.Model):
    car_id = db.Column(db.Integer)
    year = db.Column(db.Integer)
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    color = db.Column(db.String(50))
    id = db.Column(db.Integer,primary_key = True)




class Customer(db.Model):
    customer_id = db.Column(db.Integer,primary_key = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    phone_num = db.Column(db.String(20))
    vehichles = db.relationship('Customer_Car', backref=db.backref('customer', lazy='joined'))


class Customer_Car(db.Model):
    cc_id = db.Column(db.Integer, primary_key = True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    vin = db.Column(db.String(17))





class Maintenance(db.Model):
    maintenance_id = db.Column(db.Integer, primary_key = True)
    vin = db.Column(db.String(17))
    work = db.Column(db.String(500))
    date_start = db.Column(db.DateTime, default=datetime.now().date())
    date_finished = db.Column(db.DateTime, default=datetime.now().date())
    staff_id = db.Column(db.Integer)

        #need to make vin a foreign key



# @login.user_loader
# def load_user(id):
#     return User.query.get(int(id))
