from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# DB config (use env variable later for RDS)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DB_URL", "sqlite:///policy.db"
)

db = SQLAlchemy(app)

class Policy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(50))
    amount = db.Column(db.Float)

with app.app_context():
    db.create_all()

# Home page
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# Health check
@app.route('/health')
def health():
    return {"status": "ok"}

# Create Policy
@app.route('/createPolicy', methods=['POST'])
def create_policy():
    data = request.json
    policy = Policy(**data)
    db.session.add(policy)
    db.session.commit()
    return jsonify({"message": "Policy created"}), 201

# View Policy
@app.route('/viewPolicy/<int:id>', methods=['GET'])
def view_policy(id):
    policy = Policy.query.get(id)
    if not policy:
        return jsonify({"error": "Not found"}), 404

    return jsonify(policy.__dict__)

# Update Policy
@app.route('/updatePolicy/<int:id>', methods=['PUT'])
def update_policy(id):
    policy = Policy.query.get(id)
    if not policy:
        return jsonify({"error": "Not found"}), 404

    data = request.json
    policy.name = data['name']
    policy.type = data['type']
    policy.amount = data['amount']
    db.session.commit()
    return jsonify({"message": "Updated"})

# Delete Policy
@app.route('/deletePolicy/<int:id>', methods=['DELETE'])
def delete_policy(id):
    policy = Policy.query.get(id)
    if not policy:
        return jsonify({"error": "Not found"}), 404

    db.session.delete(policy)
    db.session.commit()
    return jsonify({"message": "Deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)