import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json
from app import app

database_path = "postgres://vxeixurhhuzzmc:bf31bf678d244b3a7d0302bbbf7ff587172bcf34f8f1b85e8413a66d9cd9256e@ec2-54-205-232-84.compute-1.amazonaws.com:5432/dcnrfesiknuo7q"

db = SQLAlchemy()
db.init_app(APP)

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.app = app
    

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





