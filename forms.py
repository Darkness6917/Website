from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import validators
from wtforms.fields.simple import PasswordField, SubmitField, BooleanField, EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class Registration(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    confirmPassword = PasswordField('Confirm Password',
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')
    
class Login(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign up')