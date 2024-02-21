from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Services(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  service_title = db.Column(db.String(150))
  description = db.Column(db.String(10000))
  cost = db.Column(db.Integer)
  date = db.Column(db.DateTime(timezone=True), default=func.now())
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  first_name = db.Column(db.String(150))
  last_name = db.Column(db.String(150))
  dateofbirth = db.Column(db.DateTime)
  address = db.Column(db.String(300))
  phone_num = db.Column(db.Integer, unique=True)
  services = db.relationship('Services')
  profile_pic = profile_pic = db.Column(db.String(), nullable=True)