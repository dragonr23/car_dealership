from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, TextAreaField, BooleanField, DateTimeField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from flask import flash
from app.models import Maintenance, Product, Customer
from datetime import datetime




# class TitleForm(FlaskForm):
#     title = StringField('Title', validators=[DataRequired()])
#     submit =SubmitField('Change Title')



class ProductForm(FlaskForm):
    year = IntegerField('Year', validators=[DataRequired()])
    make = StringField('Make', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])


class MaintenanceForm(FlaskForm):
    vin = StringField('Vin', validators=[DataRequired()])
    work = TextAreaField('Work', validators=[DataRequired()])
    date_start = DateTimeField('Start Work Date')
    date_finished = DateTimeField('End Work Date')
    staff_id = IntegerField('Staff ID')
    submit = SubmitField('Send Maintenance Update')

class CustomerForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    submit = SubmitField("Search Customer")
