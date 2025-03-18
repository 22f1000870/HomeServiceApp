from db import db

class Users(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String,unique=False,nullable=False)
    password=db.Column(db.String(300),unique=False,nullable=False)
    type=db.Column(db.String,nullable=True)

    professional=db.relationship("Professional",backref=db.backref('users',uselist=False))
    customer=db.relationship("Customer",backref=db.backref('users,uselist=False'))
