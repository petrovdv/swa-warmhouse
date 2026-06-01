from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DeviceType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    serial_number = db.Column(db.String(100), unique=True, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey("device_type.id"), nullable=False)
    house_id = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)

def to_dict(obj):
    if isinstance(obj, DeviceType):
        return {"id": obj.id, "name": obj.name}
    elif isinstance(obj, Device):
        return {
            "id": obj.id,
            "name": obj.name,
            "serial_number": obj.serial_number,
            "type_id": obj.type_id,
            "house_id": obj.house_id,
            "location": obj.location,
            "status": obj.status,
        }