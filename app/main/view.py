from flask import Flask,render_template , url_for,request,redirect
from . import main
from flask_login import login_required,current_user
from app.models import User,Post,Comment
from .. import db,photos
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

@main.route('/profile/<username>')
@login_required
def profile(username):
    user = User.query.filter_by(username = username).first()
    return render_template('profile.html',title='Profile',user=user)

@main.route('/write_post/new')
@login_required
def write_post():
    
    return render_template('write_post.html',title='Write')

@main.route('/<username>/update/pic', methods = ['POST'])
@login_required
def update_profile_pic(username):
    user = User.query.filter_by(username = username).first()

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_img = path
        db.session.commit()

    return redirect(url_for('main.profile', username = username))







