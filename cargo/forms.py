from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, DateField, TimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from cargo.models import  Login, Shippingdetails
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import SelectField




class Shipform(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    pic = FileField('Upload Picture', validators=[FileAllowed(['jpg', 'png','jpeg'])])
   
    add = StringField('Address',
                           validators=[DataRequired(), Length(min=2, max=20)])
    phone = StringField('Phone',
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Submit')


class Shipdetailsform(FlaskForm):
    fromplace = StringField('From',
                           validators=[DataRequired(), Length(min=2, max=20)])
    to = StringField('To',
                        validators=[DataRequired()])
   
    date = DateField('Date',format='%m/%d/%Y',render_kw={"placeholder":"dd/mm/yyyy"})
    time = TimeField('Time - 24 hour format',render_kw={"placeholder":"hrs:mins"})
    desc = StringField('Description',
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Submit')


class Productaddform(FlaskForm):
    product = StringField('Product Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    weight = StringField('Weight',
                        validators=[DataRequired()])

    name = StringField('Delivery Name',validators=[DataRequired()])
    address = StringField('Delivery Address',validators=[DataRequired()])
    
    submit = SubmitField('Submit')

class Delivery(FlaskForm):
    status = StringField('Delivery Status',validators=[DataRequired()])
    
    submit = SubmitField('Submit')