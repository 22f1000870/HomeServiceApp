from marshmallow import Schema, fields

class UserSchema(Schema):
    id=fields.Int(dump_only=True)
    username=fields.Str(required=True)
    password=fields.Str(required=True,load_only=True)

class ProfessionalRegisterSchema(UserSchema):
    name=fields.Str(required=True)
    profession=fields.Str(required=True)
    pincode=fields.Int(required=True)
    experience=fields.Int()
    image_url=fields.Str()

class ServiceRegisterSchema(Schema):
    serviceid=fields.Int(dump_only=True)
    servicename=fields.Str(required=True)
    profession=fields.Str(required=True)
    base_price=fields.Float(required=True)
    image=fields.Str()
    
class RefreshToken(Schema):
    refresh_token=fields.Str(required=True)

class CustomerRegisterSchema(UserSchema):
    id=fields.Int(dump_only=True)
    name=fields.Str(required=True)
    pincode=fields.Int(required=True)
    image=fields.Str()


