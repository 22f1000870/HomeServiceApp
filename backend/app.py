from datetime import timedelta
import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager, get_jwt, jwt_required
from db import db
from models import Users
from flask_smorest import Api
from passlib.hash import pbkdf2_sha256
from resources import LoginBlueprint
from resources import CreateServiceBlueprint , ProfessionInfo, Customer
from flask_cors import CORS
from functools import wraps
import redis

from resources import LoginBlueprint, CreateServiceBlueprint

def create_app():
    app = Flask(__name__)
    load_dotenv()

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = 'HOME REST API'
    app.config['API_VERSION'] = 'v1'
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config['OPENAPI_URL_PREFIX'] = '/docs'  # Swagger UI path is prefixed with /docs
    app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'  # This is the actual Swagger UI path
    app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist@latest/'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = "junaid"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=10)  # Access token expires in 5 seconds for testing
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=7)     # Refresh token expires in 7 days
    app.config['JWT_CSRF_PROTECT'] = False
    app.config["API_SPEC_OPTIONS"] = {
    "components": {
        "securitySchemes": {
            "BearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",  # Inform Swagger this uses JWT format
            }
        }
    },
    "security": [{"BearerAuth": []}],  # Apply BearerAuth globally to all endpoints
}


    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'static')
    db.init_app(app)
    CORS(app, resources={r"/*": {"origins": "*"}})
    # CORS(app)
    api = Api(app)  # Initialize Api without 'docs' argument
    jwt = JWTManager(app)

    # Initialize the database and create the admin user if necessary
    with app.app_context():
        db.create_all()
        if not Users.query.filter(Users.username == 'admin').first():
            admin = Users(username='admin', password=pbkdf2_sha256.hash('123'), type='Admin')
            db.session.add(admin)
            db.session.commit()

    # Register your blueprints with a unique name to avoid conflict
    api.register_blueprint(LoginBlueprint)
    api.register_blueprint(CreateServiceBlueprint)  # Set a unique name
    api.register_blueprint(ProfessionInfo)
    api.register_blueprint(Customer)
    return app
