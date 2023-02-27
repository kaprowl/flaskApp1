from app import db
from sqlalchemy_serializer import SerializerMixin
import pytz
from datetime import datetime

class BlogEntry(db.Model, SerializerMixin):
    __tablename__ = "Blog"

    timezone = pytz.timezone('Asia/Bangkok')
    current_time = datetime.now(timezone)
    formatted_time = current_time.strftime('%d %B %Y %H:%M:%S')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    message = db.Column(db.String(280))
    email = db.Column(db.String(50))
    date_created = db.Column(db.DateTime)
    date_updated = db.Column(db.DateTime)
    currentID = db.Column(db.Integer)

    def __init__(self, name, message, email, owner_id):
        self.currentID = owner_id
        self.name = name
        self.message = message
        self.email = email
        timezone = pytz.timezone('Asia/Bangkok')
        current_time = datetime.now(timezone)
        formatted_time = current_time.strftime('%d %B %Y %H:%M:%S')
        self.date_created = formatted_time
        self.date_updated = formatted_time


    def update(self, name, message, email):
        self.name = name
        self.message = message
        self.email = email
        timezone = pytz.timezone('Asia/Bangkok')
        current_time = datetime.now(timezone)
        formatted_time = current_time.strftime('%d %B %Y %H:%M:%S')
        self.date_updated = formatted_time