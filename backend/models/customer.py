from db import db

class Customer(db.Model):
    __tablename__='customer'
    id=db.Column(db.Integer,db.ForeignKey('users.id'),primary_key=True)
    name=db.Column(db.String,nullable=False)
    pincode=db.Column(db.Integer,nullable=False)
    image_url=db.Column(db.String)
    email=db.Column(db.String)