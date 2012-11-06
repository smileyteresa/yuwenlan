from database import db
from datetime import datetime

class users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(45), unique = True)
    email = db.Column(db.String(45), unique = True)
    password = db.Column(db.String(32))
    birthday = db.Column(db.DateTime)
    city = db.Column(db.String(120))
    joinTime = db.Column(db.DateTime, default = datetime.utcnow)