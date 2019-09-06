#数据库模型
from datetime import datetime
from sayhello import db

class Message(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String(20))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime,default=datetime.utcnow,index=True)