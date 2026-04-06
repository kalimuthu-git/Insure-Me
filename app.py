from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///policy.db'
db = SQLAlchemy(app)

# Model
class Policy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(50))
    amount = db.Column(db.Float)

# Create DB & preload data
with app.app_context():
    db.create_all()
    if not Policy.query.first():
        db.session.add(Policy(name="Health Plan A", type="Health", amount=5000))
        db.session.add(Policy(name="Car Plan B", type="Vehicle", amount=8000))
        db.session.commit()

# ✅ Serve Frontend (index.html)
@app.route('/')
def home():
    return send_file('index.html')

# ✅ Contact Form API
@app.route('/contact', methods=['POST'])
def contact():
    data = request.form
    print("Contact:", data)
    return "Message received"

# Create Policy
@app.route('/createPolicy', methods=['POST'])
def create_policy():
    data = request.json
    policy = Policy(**data)
    db.session.add(policy)
    db.session.commit()
    return jsonify({"message": "Policy created"}), 201

# Update Policy
@app.route('/updatePolicy/<int:id>', methods=['PUT'])
def update_policy(id):
    policy = Policy.query.get(id)
    if not policy:
        return jsonify({"error": "Policy not found"}), 404

    data = request.json
    policy.name = data['name']
    policy.type = data['type']
    policy.amount = data['amount']
    db.session.commit()
    return jsonify({"message": "Updated"})

# View Policy
@app.route('/viewPolicy/<int:id>', methods=['GET'])
def view_policy(id):
    policy = Policy.query.get(id)
    if not policy:
        return jsonify({"error": "Policy not found"}), 404

    return jsonify({
        "id": policy.id,
        "name": policy.name,
        "type": policy.type,
        "amount": policy.amount
    })

# Delete Policy
@app.route('/deletePolicy/<int:id>', methods=['DELETE'])
def delete_policy(id):
    policy = Policy.query.get(id)
    if not policy:
        return jsonify({"error": "Policy not found"}), 404

    db.session.delete(policy)
    db.session.commit()
    return jsonify({"message": "Deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)