from cargo import db, app, login_manager
from flask_login import UserMixin
from flask_table import Table, Col, LinkCol
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer



@login_manager.user_loader
def load_user(id):
    return Login.query.get(int(id))

class Login(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(100),nullable=False)
    phone = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(80), nullable=False)
    image= db.Column(db.String(20), nullable=False, default='default.jpg')
    usertype = db.Column(db.String(80), nullable=False)



class Gallery(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200))
    image = db.Column(db.String(20), nullable=False, default='default.jpg')

class Shippingdetails(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    ownerid = db.Column(db.String(120))
    ownername = db.Column(db.String(120))
    fromplace = db.Column(db.String(120), nullable=False)
    toplace = db.Column(db.String(100),nullable=False)
    date = db.Column(db.Date(),nullable=False)
    time = db.Column(db.Time(), nullable=False)
    desc= db.Column(db.String(200), nullable=False)

class Contact(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    subject = db.Column(db.String(200))
    message = db.Column(db.String(200))
    usertype = db.Column(db.String(200))


class Productadd(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    ownerid = db.Column(db.String(120))
    detailsid = db.Column(db.String(120))
    pdtname = db.Column(db.String(120))
    weight = db.Column(db.String(120))
    delname = db.Column(db.String(120))
    deladdress = db.Column(db.String(120))
    shipid = db.Column(db.String(120))
    shipname = db.Column(db.String(120))
    fromplace = db.Column(db.String(120), nullable=False)
    toplace = db.Column(db.String(100),nullable=False)
    date = db.Column(db.Date(),nullable=False)
    time = db.Column(db.Time(), nullable=False)
    desc= db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(200), nullable=False)
    delstatus = db.Column(db.String(200), nullable=False)
    productid = db.Column(db.String(200), nullable=False)