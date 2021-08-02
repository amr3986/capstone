import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json
from app import APP

database_path = "postgres://fsvrjzejayvqat:1a9444214bc3afcb1e686f9cd770f4ae35424870de8002bb1aa2db73257a5826@ec2-54-205-232-84.compute-1.amazonaws.com:5432/d210h6pl1reh9o"

db = SQLAlchemy()
db.init_app(APP)

def setup_db(APP, database_path=database_path):
    APP.config["SQLALCHEMY_DATABASE_URI"] = database_path
    APP.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.app = APP
    

class Actor(db.Model):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)

    def __init__(self, name, gender,age):
        self.name = name
        self.gender = gender
        self.age = age
        

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'age': self.age
        }


class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(db.Integer, primary_key=True)
    title = Column(db.String(50), nullable=False)
    release_date = Column(db.String(4), nullable=False)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def format(self):
        return{
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }





