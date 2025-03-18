
import os
from flask import current_app, jsonify, request
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint
from flask.views import MethodView
from werkzeug.utils import secure_filename
from db import db
from models import Service, Users , Professional_Req,Professional
from schemas import ProfessionalRegisterSchema
from resources.RBAC import access_allowed
from passlib.hash import pbkdf2_sha256
blp = Blueprint('prof_info',__name__,description='Create Professional')

@blp.route('/prof_info')
class ProfInfo(MethodView):
    def get(self):
        unique_professions = [row[0] for row in Service.query.with_entities(Service.profession).distinct().all()]
        return jsonify({"professions": unique_professions})

    def post(self):

        prof_req= {
            'name':request.form.get('name'),
            'username':request.form.get('username'),
            'password':request.form.get('password'),
            'experience':request.form.get('experience'),
            'pincode':request.form.get('pincode'),
            'image':request.form.get('image'),
            'profession':request.form.get('profession') }
        
        user= Users.query.filter_by(username=prof_req['username']).first()
        if user:
            return {"message": "Username Already exists, Try unique Username"},400
        
        try:
            # Handle file upload
            image = request.files.get('file')
            if not image:
                return {"message": "No image file provided"}, 400

            upload_folder = os.path.join(current_app.static_folder,'professional')
            filename = secure_filename(image.filename)
            filepath = os.path.join(upload_folder, filename)
            image.save(filepath)
            prof=Professional_Req (
                username=prof_req['username'],
                name=prof_req['name'],
                password=prof_req['password'],
                pincode=prof_req['pincode'],
                experience=prof_req['experience'],
                image_url= f"{request.host_url}static/professional/{filename}",
                profession=prof_req['profession'])
            db.session.add(prof)
            db.session.commit()
            return {"message": " Professional Registration Successfull"}, 201
        except Exception as e:
            current_app.logger.error(f"Error creating service: {e}")
            return {"message": "An internal error occurred"}, 500
    
    


@blp.route('/professionals')
class ALL_Professional(MethodView):
    @jwt_required()
    @access_allowed('Admin','Customer')
    def get(self):
        prof_count=Professional.query.count()
        prof=Professional.query.all()
        schema=ProfessionalRegisterSchema(many=True)
        profs=schema.dump(prof)
        prof_req_count=Professional_Req.query.count()
        prof_req=Professional_Req.query.all()
        req_schema=ProfessionalRegisterSchema(many=True)
        prof_reqs=req_schema.dump(prof_req)
        return jsonify({'professionalcount':prof_count,'professionals':profs,'professional_request':prof_reqs,
                        'professional_request_count':prof_req_count}),200


@blp.route('/professional/reject/<string:username>')
class RejectProf(MethodView):
    @jwt_required()
    @access_allowed('Admin')
    def delete(self,username):
        prof=Professional_Req.query.filter(Professional_Req.username==username).first()
        db.session.delete(prof)
        db.session.commit()
        return {'message':"Professional Rejected !!"},200
        

@blp.route('/professional/accept/<string:username>')
class AceeptProf(MethodView):
    @jwt_required()
    @access_allowed('Admin')
    def post(self,username):
        prof=Professional_Req.query.filter(Professional_Req.username==username).first()
        user=Users(username=username,password=pbkdf2_sha256.hash(prof.password), type='Professional')
        db.session.add(user)
        db.session.flush()

        new_prof=Professional(id=user.id,name=prof.name,pincode=prof.pincode,experience=prof.experience,
                              profession=prof.profession,image_url=prof.image_url
                              )
        db.session.add(new_prof)
        db.session.delete(prof)
        db.session.commit()
        return {"message":"Professional Accepted" },201