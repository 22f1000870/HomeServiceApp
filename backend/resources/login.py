from flask.views import MethodView
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt, jwt_required
from flask_smorest import Blueprint, abort
from db import db
from resources.RBAC import access_allowed
from models import Users, Professional, Service
from schemas import ProfessionalRegisterSchema, UserSchema , RefreshToken
from passlib.hash import pbkdf2_sha256

blp=Blueprint('login',__name__,description="Operation on Login")

@blp.route('/login')
class Login(MethodView):
    @blp.arguments(UserSchema)
    def post(self,user_data):
        user=Users.query.filter(Users.username==user_data['username']).first()

        if user and pbkdf2_sha256.verify(user_data['password'],user.password):
            access_token=create_access_token(identity=user.id,additional_claims={'role':user.type},fresh=True)
            refresh_token=create_refresh_token(identity=user.id,additional_claims={'role':user.type})
            return {"access_token":access_token,"refresh_token":refresh_token,"role":user.type},200
        
        abort(401,message="Invalid credentials ")

@blp.route('/register')
class ProfessionalRegister(MethodView):
    @blp.arguments(ProfessionalRegisterSchema)
    def post(self,user_data):

        if Users.query.filter(Users.username==user_data['username']).first():
            abort(409,message="A user with this username already exists")
        
        user=Users(username=user_data['username'],password=pbkdf2_sha256.hash(user_data['password']),type='professional')
        db.session.add(user)
        db.session.flush()

        professional=Professional(id=user.id,name=user_data['name'],profession=user_data['profession'],pincode=user_data['pincode'],experience=user_data['experience'],image=user_data['image'])
        db.session.add(professional)
        db.session.commit()
        return {"message":"User created successfully"},201
    

@blp.route('/refresh')
class Refresh(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        # Extract current user identity and role from the JWT
        current_user = get_jwt()
        identity = current_user.get('sub')  # 'sub' claim contains the user ID
        role = current_user.get('role')  # 'role' claim contains the user type (e.g., 'professional')

        # Ensure that the required claims are available
        if not identity or not role:
            abort(401, message="Invalid token: missing required claims.")

        # Generate a new access token without 'fresh' flag (so it's non-fresh)
        new_access_token = create_access_token(
            identity=identity,
            additional_claims={'role': role},
            fresh=False
        )

        return {"access_token": new_access_token}, 200

