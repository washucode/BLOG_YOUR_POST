from flask import Flask,render_template , url_for,request,redirect
from . import auth
from flask_login import login_required,current_user
from .forms import RegistrationForm, SignInForm
# import forms
# import models


@auth.route('/login')
def login():
    
    return render_template('login.html', title='Login')


@auth.route('/registration')
def register():
    return render_template('register.html',title='Register')
