from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm():
    firstname = StringField('Firstname',validators= [DataRequired(),Length(min=2,max=20)])
    secondname = StringField('Secondname', validators=[DataRequired(),Length(min=2,max=30)])
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class SignInForm():
    
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    
    password = PasswordField('Password', validators=[DataRequired()])
    
    submit = SubmitField('Sign In')
    