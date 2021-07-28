from typing import cast
from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import os
import json

database_path = os.environ['SQLALCHEMY_DATABASE_URI']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
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
  director = db.Column(db.String(), nullable=False, unique=True)
  release_date = db.Column(db.String)
  desc = db.Column(db.String())
  cast = db.relationship('Cast', backref='movies', lazy='joined', cascade='all, delete')

  def __init__(self, title, director, release_date, desc):
    self.title = title
    self.director = director
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
      'director': self.title,
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
  surname = db.Column(db.String(), nullable=False)
  age = db.Column(db.Integer, nullable=False)
  gender = db.Column(db.String(), nullable=False)
  cast = db.relationship('Cast', backref='actors', lazy='joined', cascade='all, delete')

  def __init__(self, name, surname, age, gender):
    self.name = name
    self.surname = surname
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
      'name': self.surname,
      'age': self.age,
      'gender': self.gender
    }

'''
Cast
Movie Cast and role
'''
class Cast(db.Model):
  __tablename__ = 'cast'
  id = db.Column(db.Integer, primary_key=True)
  actor_id = db.Column(db.Integer, db.ForeignKey('actors.id'), nullable=False)
  movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
  role = db.Column(db.String(), nullable=False)

