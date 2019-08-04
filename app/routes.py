from app import app, db
from flask import render_template, url_for, redirect, flash
from app.forms import MaintenanceForm, ProductForm, CustomerForm
from app.models import Maintenance, Product, Customer
from flask_login import current_user, login_user, logout_user, login_required

@app.route('/')
@app.route('/index')
@app.route('/index/', methods=['GET', 'POST'])
def index():
    form = ProductForm()

    products = Product.query.all()

    return render_template('index.html', title='Inventory', form=form, products=products)


@app.route('/customer', methods=['GET', 'POST'])
def customer():
    form = CustomerForm()


    first_name = form.first_name.data,
    last_name = form.last_name.data




    # customer = Customer.query.all()

    customer = Customer.query.all()
    return render_template('customer.html', form=form, title='Customer', customer=customer, first_name=first_name)

@app.route('/maintenance', methods=['GET', 'POST'])
def maintenance():

    form = MaintenanceForm()

    if form.validate_on_submit():

        work_complete = Maintenance(
            vin = form.vin.data,
            work = form.work.data,
            date_start = form.date_start.data,
            date_finished = form.date_finished.data,
            staff_id = form.staff_id.data
        )

        db.session.add(work_complete)
        db.session.commit()

        flash("Thanks for sending in a job well done!")
        return redirect(url_for('index'))

    return render_template('maintenance.html', form=form, title='Maintenance')
