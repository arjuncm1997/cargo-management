from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from cargo.models import  Login
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