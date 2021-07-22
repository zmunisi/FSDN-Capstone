from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import os
import json

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["DATABASE_URL"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Movies
Have a title, release date and description
'''
class Movies(db.Model):  
  __tablename__ = 'movies'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(), nullable=False, unique=True)
  release_date = db.Column(db.String)
  desc = db.Column(db.String())

  def __init__(self, title, release_date, desc):
    self.title = title
    self.release_date = release_date
    self.desc = desc

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release_date': self.release_date,
      'description': self.desc
    }

'''
Actors
Have a title, release date and description
'''
class Actors(db.Model):
  __tablename__ = 'actors'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
  age = db.Column(db.Integer, nullable=False)
  gender = db.Column(db.String(), nullable=False)

  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender
    }