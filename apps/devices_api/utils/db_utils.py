from db.models import db, DeviceType

PREDEFINED_DEVICE_TYPES = (
    "Heating",
    "Cooling",
    "Lighting",
    "Video",
    "Gates"
)

def populate_db():
    for type_name in PREDEFINED_DEVICE_TYPES:
        if not DeviceType.query.filter_by(name=type_name).first():
            device_type = DeviceType(name=type_name)
            db.session.add(device_type)
    db.session.commit()


def init_db():
    db.create_all()
    populate_db()