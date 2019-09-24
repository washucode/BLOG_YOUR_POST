from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
class User(UserMixin,db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer,primary_key= True)
    firstname = db.Column(db.String(255),nullable=False, unique=True)
    secondname = db.Column(db.String(255),nullable=False, unique=True)
    username = db.Column(db.String(255),nullable=False, unique=True)
    email = db.Column(db.String(255), nullable =False,unique=True)
    profile_img = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    posts = db.relationship('Post', backref = 'user', lazy = 'dynamic')
    password = db.Column(db.String(255),nullable = False)

    def save(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def set_password(self,password):
        password_hash = generate_password_hash(password)
        self.password = password_hash
        
    def check_password(self, password):
        return check_password_hash(self.password,password)
    
    def __repr__(self):
        return "User:%s"%str(self.username)




class Post(db.Model):
    __tablename__= 'posts'
    id = db.Column(db.Integer,primary_key= True)
    title = db.Column(db.String(255),nullable=False)
    content= db.Column(db.Text,nullable=False)
    author = db.Column(db.String(255),nullable=False)
    category = db.Column(db.String(255),nullable=False)
    date_posted = db.Column(db.DateTime, default = datetime.utcnow)   
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref = 'post', lazy = 'dynamic')

    def save_post(self):
        db.session.add(self)
        db.session.commit()
    def delete_post(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return "Post:%s"%str(self.title)

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    name =  db.Column(db.String(255),nullable=False)
    email = db.Column(db.String(255), nullable =False)
    content = db.Column(db.String(1000) )          
    date_posted = db.Column(db.DateTime, default = datetime.utcnow)    
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()


class Quotes:
  def __init__ (self,author,quote,permalink):
    self.author = author
    self.quote = quote
    self.permalink = permalinkdef
    

    
@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

