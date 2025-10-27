from flask import Flask, jsonify, request
from db.models import db, TelemetryData
from utils.db_utils import init_db
import os
import requests

TEMPERATURE_API_URL = os.getenv("TEMPERATURE_API_URL", "http://temperature-api:8081")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "postgresql://postgres:password@db:5432/telemetry")
db.init_app(app)
with app.app_context():
    init_db()

@app.route('/health')
def health():
    return jsonify({"Status": "OK"})

@app.route('/telemetry', methods=['POST'])
def create_telemetry():
    data = request.get_json()
    if not data or not all(k in data for k in ('device_id', 'value', 'unit')):
        return jsonify({"error": "Missing fields"}), 400

    telemetry = TelemetryData(
        device_id=data['device_id'],
        value=data['value'],
        unit=data['unit'],
        location = data['location'],
        status = data['status'],
    )
    db.session.add(telemetry)
    db.session.commit()
    return jsonify(telemetry.to_dict()), 201

@app.route('/telemetry', methods=['GET'])
def get_all_telemetry():
    records = TelemetryData.query.order_by(TelemetryData.created_at.desc()).all()
    return jsonify([r.to_dict() for r in records])

@app.route('/telemetry/<int:id>', methods=['GET'])
def get_telemetry(id):
    record = TelemetryData.query.get_or_404(id)
    return jsonify(record.to_dict())

@app.route('/telemetry/device/<int:device_id>', methods=['GET'])
def get_telemetry_by_device(device_id):
    records = TelemetryData.query.filter_by(device_id=device_id).all()
    if not records:
        return jsonify({'message': f'No telemetry data found for device_id {device_id}'}), 404
    return jsonify([r.to_dict() for r in records])

@app.route('/telemetry/device/<int:device_id>/latest', methods=['GET'])
def get_latest_device_telemetry(device_id):
    """ Читает сервис эмуляции датчика температуры, сохраняет значение в БД
    и возвращает объект телеметрии пользователю"""
    populate_telemetry(device_id)
    record = TelemetryData.query.filter_by(device_id=device_id).order_by(TelemetryData.created_at.desc()).first()
    if not record:
        return jsonify({"error": "No telemetry data found"}), 404
    return jsonify(record.to_dict())


def populate_telemetry(device_id):
    try:
        response = requests.get(f"{TEMPERATURE_API_URL}/temperature/{device_id}", timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Failed to fetch from external service: {str(e)}'}), 500

    json_data = response.json()

    record = TelemetryData(
        device_id=json_data['sensor_id'],
        value=json_data['value'],
        unit=json_data['unit'],
        location=json_data['location'],
        status=json_data['status']
    )
    db.session.add(record)
    db.session.commit()
    return jsonify(record.to_dict()), 201

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(host='0.0.0.0', port=8084)