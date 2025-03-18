from db import db

class Service(db.Model):
    __tablename__='service'
    service_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    servicename=db.Column(db.String,nullable=False)
    profession=db.Column(db.String,nullable=False)
    image=db.Column(db.String)
    base_price=db.Column(db.Integer,nullable=False)

    serviceman=db.relationship("Professional",backref=db.backref('service'),lazy='dynamic')