from flask import Flask, request, jsonify
from db.models import db, User
from utils.db_utils import init_db
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "postgresql://postgres:password@db:5432/users")
db.init_app(app)
with app.app_context():
    init_db()

@app.route('/health')
def health():
    return jsonify({"Status": "OK"})

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already exists"}), 400
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users]), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict()), 200

@app.route('/users/<int:order_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    if 'name' in data:
        user.name = data['name']
    if 'email' in data:
        if User.query.filter(User.email == data['email'], User.id != user_id).first():
            return jsonify({"error": "Email already exists"}), 400
        user.email = data['email']

    db.session.commit()
    return jsonify({'message': 'User updated successfully'})

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(host='0.0.0.0', port=8082)