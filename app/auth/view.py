from flask import render_template,redirect,url_for,flash,request
from . import auth
from flask_login import login_required,current_user



# import forms
# import models


@auth.route('/login',methods=['GET','POST'])
def login():
    
    
    
    return render_template('login.html', title='Login')


@auth.route('/registration', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        form = request.form
        firstname = form.get("firstname")
        secondname = form.get("secondname")
        username = form.get("username")
        email = form.get("email")
        password = form.get("password")
        confirm_password = form.get("confirm_password")
        if username==None or password==None or confirm_password==None or email==None:
            error = "username,password and email are required"
            return render_template('signup.html', error=error)
        if password != confirm_password:
            error = "Not a match"
            return render_template('signup.html',error=error)
        else:
            user = User.query.filter_by(username= username).first()
            if user!= None:
                error = "Username exitsts"
                return render_template('signup.html', error = error)
            user = User.query.filter_by(email=email).first()
            if user!= None:
                error = "Email exits"
                return render_template('signup.html', error = error)

            user = User(username=username,email=email)
            user.set_password(password)
            user.save()
            return redirect(url_for("auth.login"))
    
    
    return render_template('register.html',title='Register')
