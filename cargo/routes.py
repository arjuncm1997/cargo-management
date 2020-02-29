import os 
from flask import Flask, flash, session
from flask import render_template, flash, redirect, request, abort, url_for
from cargo import app, db, bcrypt
from cargo.models import Login
from cargo.forms import Shipform
from flask_login import login_user, current_user, logout_user, login_required
from flask_login import login_user, current_user, logout_user, login_required
from PIL import Image
from random import randint
import random       


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/gallery')
def gallery():
    return render_template("gallery.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route("/uindex")
def uindex():
    return render_template("uindex.html")

@app.route('/sindex')
def sindex():
    return render_template("sindex.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = Login.query.filter_by(email=request.form['email'], usertype = 'user' ).first()
        user1 = Login.query.filter_by(email=request.form['email'],  usertype = 'ship').first()
        user2 = Login.query.filter_by(email=request.form['email'],  usertype = 'admin').first()
        if user and bcrypt.check_password_hash(user.password,request.form['password']):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect('/uindex')
        if user1 and bcrypt.check_password_hash(user1.password, request.form['password']):
            login_user(user1)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect('/sindex')
        if user2 and user2.password== form.password.data:
            login_user(user2, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect('/admin')

        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login')

@app.route('/userregister',methods=['GET','POST'])
def userregister():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        hashed_password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        new = Login(username = name,email=email,password=hashed_password,address ='',phone = '', usertype = 'user'   )

        try:
            db.session.add(new)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        return render_template('userregister.html')


@app.route('/shipregister',methods=['GET','POST'])
def shipregister():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        hashed_password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        new = Login(username = name,email=email,password=hashed_password,address ='',phone = '', usertype = 'ship'  )

        try:
            db.session.add(new)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        return render_template('shipregister.html')


@app.route('/sdetails')
def sdetails():
    return render_template("sdetails.html")


@app.route('/sprofile/<int:id>',methods=['GET','POST'])
def sprofile(id):
    form = Shipform()
    task = Login.query.get_or_404(id)
    if form.validate_on_submit():
        if form.pic.data:
            view = save_picture(form.pic.data)
            task.image = view
        task.username = form.name.data
        task.email = form.email.data
        task.address = form.add.data
        task.phone = form.phone.data
        db.session.commit() 
        return redirect("")

    elif request.method == 'GET':
        form.name.data = task.username
        form.email.data = task.email
        form.add.data = task.address
        form.phone.data = task.phone
    return render_template("sprofile.html",form=form)


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def save_picture(form_picture):
    random_hex = random_with_N_digits(14)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = str(random_hex) + f_ext
    picture_path = os.path.join(app.root_path, 'static/pics', picture_fn)
    
    output_size = (500, 500)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


@app.route('/sdetailsadd')
def sdetailsadd():
    return render_template("sdetailsadd.html")