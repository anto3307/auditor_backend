from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# -------------------------
# App configuration
# -------------------------
app = Flask(__name__)
CORS(app)  # allow frontend to talk to backend

app.config['SECRET_KEY'] = 'secret123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -------------------------
# Home route (test)
# -------------------------
@app.route('/')
def home():
    return "Auditor App Backend Running"

# -------------------------
# LOGIN API (TEMP / DUMMY)
# -------------------------
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    # Temporary hardcoded check
    if email == "test@example.com" and password == "1234":
        return jsonify({
            "status": "success",
            "message": "Login successful"
        }), 200
    else:
        return jsonify({
            "status": "error",
            "message": "Invalid email or password"
        }), 401

# -------------------------
# Run app
# -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
