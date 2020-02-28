import os 
from flask import Flask, flash, session
from flask import render_template, flash, redirect, request, abort, url_for
from cargo import app, db, bcrypt
from cargo.models import User, Ship
from flask_login import login_user, current_user, logout_user, login_required
from flask_login import login_user, current_user, logout_user, login_required


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
        user = User.query.filter_by(email=request.form['email'] ).first()
        user1 = Ship.query.filter_by(email=request.form['email']).first()
        if user and bcrypt.check_password_hash(user.password,request.form['password']):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect('/uindex')
        if user1 and bcrypt.check_password_hash(user1.password, request.form['password']):
            login_user(user1)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect('/sindex')

        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login')

@app.route('/userregister',methods=['GET','POST'])
def userregister():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        hashed_password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        new = User(username = name,email=email,password=hashed_password )

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
        new = Ship(username = name,email=email,password=hashed_password )

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