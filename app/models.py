from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
class User(UserMixin,db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer,primary_key= True)
    firstname = db.Column(db.String(255),nullable=False, unique=True)
    secondname = db.Column(db.String(255),nullable=False, unique=True)
    username = db.Column(db.String(255),nullable=False, unique=True)
    email = db.Column(db.String(255), nullable =False,unique=True)
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

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)
