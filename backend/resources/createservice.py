from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint
from marshmallow import ValidationError
from schemas import ServiceRegisterSchema
from resources.RBAC import access_allowed
from models import Service
from db import db
import os
from werkzeug.utils import secure_filename
from flask import app, current_app, json, jsonify, request
blp= Blueprint('createservice',__name__,description='Create Service')

@blp.route('/createservice')
class CreateService(MethodView):
    @jwt_required()
    @access_allowed('Admin')
    def post(self):
        servicedata = {
            'servicename':request.form.get('servicename'),
            'profession':request.form.get('profession'),
            'base_price':request.form.get('base_price'),
            'image':request.form.get('image')
        }
        
        # print("Request headers:", request.headers)
    
        if not servicedata:
            return {"message": "No service data provided"}, 400

        # try:
        #     service_data = json.loads(servicedata)  # Parse JSON string
        #     print(service_data)
        # except json.JSONDecodeError:
        #     return {"message": "Invalid JSON payload"}, 400

        #Validate payload using Marshmallow schema
        schema = ServiceRegisterSchema()
        try:
            service_data = schema.load(servicedata)
            print(service_data)
        except ValidationError as e:
            print(service_data)
            return {"message": e.messages}, 422

        # Handle file upload
        image = request.files.get('file')
        if not image:
            return {"message": "No image file provided"}, 400

        upload_folder = os.path.join(current_app.static_folder,'service')
        filename = secure_filename(image.filename)
        filepath = os.path.join(upload_folder, filename)
        image.save(filepath)

        # Check if service already exists
        exists = Service.query.filter_by(servicename=service_data['servicename']).first()
        if exists:
            return {"message": "Service already exists"}, 400

        # Add service to the database
        try:
            service = Service(
                servicename=service_data['servicename'],
                profession=service_data['profession'],
                base_price=service_data['base_price'],
                image=filename  # Save the filename
            )
            db.session.add(service)
            db.session.commit()
            return {"message": "Service created successfully"}, 201
        except Exception as e:
            current_app.logger.error(f"Error creating service: {e}")
            return {"message": "An internal error occurred"}, 500

@blp.route('/getservices')
class GetService(MethodView):
    @jwt_required()
    @access_allowed('Admin')
    def get(self):
        servicecount=Service.query.count()
        services=Service.query.all()
        service_schema=ServiceRegisterSchema(many=True)
        service=service_schema.dump(services)
        for ser in service:
            ser['image_url'] = f"{request.host_url}static/service/{ser['image']}"
        print(service)
        return jsonify({'servicecount':servicecount,'services':service}),200
