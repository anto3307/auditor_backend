from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/app.db'

db = SQLAlchemy(app)

@app.route('/')
def home():
    return "Auditor App Backend Running"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)

