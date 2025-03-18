from db import db

class Professional(db.Model):
    __tablename__='serviceprofessional'
    id=db.Column(db.Integer,db.ForeignKey("users.id"),primary_key=True,unique=True)
    name=db.Column(db.String,nullable=False)
    pincode=db.Column(db.Integer,nullable=False)
    profession=db.Column(db.String,db.ForeignKey("service.profession"))
    experience=db.Column(db.Float(precision=1))
    image_url=db.Column(db.String)
    
    

