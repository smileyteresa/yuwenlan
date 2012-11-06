from database import db
from datetime import datetime

class talk(db.Model):
    def __init__(self, user_id, content):
        self.user_id = user_id
        self.content = content
        
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    content = db.Column(db.Text)
    addTime = db.Column(db.DateTime, default = datetime.utcnow)