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
        # try:
        #     service_data = json.loads(servicedata)  # Parse JSON string
        #     print(service_data)
        # except json.JSONDecodeError:
        #     return {"message": "Invalid JSON payload"}, 400

        
        # Handle file upload
        image = request.files.get('file')
        if not image:
            return {"message": "No image file provided"}, 400

        upload_folder = os.path.join(current_app.static_folder,'service')
        filename = secure_filename(image.filename)
        filepath = os.path.join(upload_folder, filename)
        image.save(filepath)
        servicedata = {
            'servicename':request.form.get('servicename'),
            'profession':request.form.get('profession'),
            'base_price':request.form.get('base_price'),
            'image_url':f"{request.host_url}static/service/{filename}"
        }

        #Validate payload using Marshmallow schema
        schema = ServiceRegisterSchema()
        try:
            service_data = schema.load(servicedata)
            print(service_data)
        except ValidationError as e:
            print(service_data)
            return {"message": e.messages}, 422


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
                image_url=service_data['image_url']
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
        
        print(service)
        return jsonify({'servicecount':servicecount,'services':service}),200

@blp.route('/updateservice')
class UpdateService(MethodView):
    @jwt_required()
    @access_allowed('Admin')
    def put(self):
        try:
            payload = request.get_json()  # Get JSON payload
            print(payload)

            if not payload:
                return jsonify({'message': 'Invalid payload'}), 400

            service_id = payload.get('service_id')
            print(service_id)
            service_name = payload.get('servicename')
            profession = payload.get('profession')
            base_price = payload.get('base_price')
            image_url = payload.get('image_url')

            service = Service.query.get(service_id)
            if service:
                service.servicename = service_name
                service.profession = profession
                service.base_price = base_price
                service.image_url = image_url
                db.session.commit()
                return jsonify({'message': 'Service updated successfully'}), 201
            else:
                return jsonify({'message': 'Service not found'}), 404

        except Exception as e:
            return jsonify({'message': str(e)}), 500