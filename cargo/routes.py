import os 
from flask import Flask, flash, session
from flask import render_template, flash, redirect, request, abort, url_for
from cargo import app




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

@app.route('/userregister')
def userregister():
    return render_template("userregister.html")

@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/shipregister')
def shipregister():
    return render_template("shipregister.html")