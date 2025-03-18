from db import db

class Professional_Req(db.Model):
    __tablename__='professional_req'
    username=db.Column(db.String,primary_key=True)
    password=db.Column(db.String,nullable=False)
    name=db.Column(db.String,nullable=False)
    pincode=db.Column(db.Integer,nullable=False)
    profession=db.Column(db.String,db.ForeignKey("service.profession"))
    experience=db.Column(db.Float(precision=1))
    image_url=db.Column(db.String)