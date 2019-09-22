from flask import Flask,render_template , url_for,request,redirect
from . import main
from flask_login import login_required,current_user
# import forms
# import models


@main.route('/')
def home():
    
    return render_template('index.html')


@main.route('/about')
def about():
    return render_template('about.html',title='About')


@main.route('/subscribe')
def subscribe():
    return render_template('subcription.html',title='Subscribe')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html',title='Profile')

@main.route('/write_post')
@login_required
def write_post():
    return render_template('write_post.html',title='Profile')






