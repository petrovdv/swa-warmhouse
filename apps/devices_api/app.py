from flask import Flask, jsonify, request
from db.models import db, DeviceType, to_dict, Device
from utils.db_utils import init_db
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "postgresql://postgres:password@db:5432/devices")
db.init_app(app)
with app.app_context():
    init_db()

@app.route('/health')
def health():
    return jsonify({"Status": "OK"})

@app.route("/device_types", methods=["GET"])
def get_device_types():
    device_types = DeviceType.query.all()
    return jsonify([to_dict(dt) for dt in device_types]), 200

@app.route("/device_types/<int:id>", methods=["GET"])
def get_device_type(id):
    t = DeviceType.query.get(id)
    if t:
        return jsonify(to_dict(t))
    return jsonify({"error": "DeviceType not found"}), 404

@app.route("/device_types", methods=["POST"])
def create_device_type():
    data = request.get_json()
    if DeviceType.query.filter_by(name=data['name']).first():
        return jsonify({"error": "Device type already exists"}), 400
    t = DeviceType(name=data["name"])
    db.session.add(t)
    db.session.commit()
    return jsonify(to_dict(t)), 201

@app.route("/device_types/<int:id>", methods=["DELETE"])
def delete_device_type(id):
    t = DeviceType.query.get(id)
    if not t:
        return jsonify({"error": "DeviceType not found"}), 404
    db.session.delete(t)
    db.session.commit()
    return jsonify({"message": "Deleted successfully"})

@app.route("/devices", methods=["GET"])
def get_devices():
    devices = Device.query.all()
    return jsonify([to_dict(d) for d in devices])

@app.route("/devices/<int:id>", methods=["GET"])
def get_device(id):
    d = Device.query.get(id)
    if d:
        return jsonify(to_dict(d))
    return jsonify({"error": "Device not found"}), 404

@app.route("/devices", methods=["POST"])
def create_device():
    data = request.get_json()
    if not DeviceType.query.get(data["type_id"]):
        return jsonify({"error": "Invalid device_type_id"}), 400

    device = Device(
        name=data["name"],
        serial_number=data["serial_number"],
        type_id=data["type_id"],
        house_id=data["house_id"],
        location=data["location"],
        status=data["status"],
    )
    db.session.add(device)
    db.session.commit()
    return jsonify(to_dict(device)), 201

@app.route("/devices/<int:id>", methods=["PUT"])
def update_device(id):
    data = request.json
    device = Device.query.get(id)
    if not device:
        return jsonify({"error": "Device not found"}), 404

    device.name = data.get("name", device.name)
    device.serial_number = data.get("serial_number", device.serial_number)
    device.type_id = data.get("type_id", device.type_id)
    device.house_id = data.get("house_id", device.house_id)
    device.location = data.get("location", device.location)
    device.status = data.get("status", device.status)

    if not DeviceType.query.get(device.type_id):
        return jsonify({"error": "Invalid device_type_id"}), 400

    db.session.commit()
    return jsonify(to_dict(device))

@app.route("/devices/<int:id>", methods=["DELETE"])
def delete_device(id):
    device = Device.query.get(id)
    if not device:
        return jsonify({"error": "Device not found"}), 404
    db.session.delete(device)
    db.session.commit()
    return jsonify({"message": "Deleted successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083)