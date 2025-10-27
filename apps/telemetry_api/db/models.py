from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

class TelemetryData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)

    def to_dict(self):
        return {"id": self.id, "device_id": self.device_id, "value": self.value, "unit": self.unit,
                "location": self.location, "status": self.status, "created_at": self.created_at}