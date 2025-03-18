from flask import current_app, request
from flask.views import MethodView
from flask_smorest import Blueprint
from marshmallow import ValidationError
from models import Customer, Users
from passlib.hash import pbkdf2_sha256
from db import db

blp=Blueprint('customer',__name__,description="Operation to create Customer")
from schemas import CustomerRegisterSchema
@blp.route('/createcustomer')
class CreateCustomer(MethodView):
    def post(self):
        customer={
            'username':request.form.get('username'),
            'password':request.form.get('password'),
            'name':request.form.get('name'),
            'pincode':request.form.get('pincode'),
            'image':request.form.get('image')
        }

        exists=Users.query.filter_by(username=customer['username']).first()

        if exists:
            return {'message':'Username Already in use, try different username'},400
        
        schema= CustomerRegisterSchema()
        
        try:
            service_data = schema.load(customer)
            print(service_data)
        except ValidationError as e:
            print(service_data)
            return {"message": e.messages}, 422
        
        try:
            user=Users(username=customer['username'],password=pbkdf2_sha256.hash(customer['password']),type='Customer')
            db.session.add(user)
            db.session.flush()
            custom=Customer(id=user.id,name=customer['name'],pincode=customer['pincode'],image=customer['image'])
            db.session.add(custom)
            db.session.commit()
            return {'message':'Customer created successfully'},201
        except Exception as e :
            current_app.logger.error(f"Error creating service: {e}")
            return {"message": "Failed to register new customer"}, 500