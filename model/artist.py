__author__ = 'yamit'
import os

from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask

__author__ = 'yamit'

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

#db = SQLAlchemy(app)

class Artist():
    #id = db.Column(db.Integer, primary_key=True)
    #name = db.Column(db.String(80))
    #email = db.Column(db.String(120), unique=True)
    #pictureUrl=db.Column(db.String(120))
    #description=db.Column(db.String(400))
    id =''
    name =''
    email =''
    pictureUrl =''
    description =''

    def __init__(self, name='', email='',pictureUrl='',description=''):
        self.name = name
        self.email = email
        self.pictureUrl = pictureUrl
        self.description = description

    def __repr__(self):
        return '<Name %r>' % self.name