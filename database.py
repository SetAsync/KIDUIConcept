from datetime import timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "DevKey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Accounts(db.Model):
    id = db.Column("id", db.Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    role = db.Column("role", db.Integer, nullable=False)

class Codes(db.Model):
    id = db.Column("id", db.Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    account = db.relationship('Accounts', backref=db.backref('codes', lazy=True))

class Logs(db.Model):
    id = db.Column("id", db.Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    record = db.Column("record", db.Text, nullable = False)

with app.app_context():
    db.create_all()