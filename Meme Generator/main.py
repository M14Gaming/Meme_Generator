import os
from flask import Flask, request, render_template, redirect, jsonify, json
from flask_sqlalchemy import SQLAlchemy
import json
import util

# get current app directory
basedir = os.path.abspath(os.path.dirname(__file__))

# create a Flask instance
app = Flask(__name__)
# define SQLAlchemy URL
app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False\

# instantiate db object
db = SQLAlchemy(app)

class Image(db.Model):
    __tablename__ = 'memeImages'
    id = db.Column(db.Integer, primary_key=True)
    imagePath = db.Column(db.String)

@app.route('/')
def home():
    # home page
    return render_template('home.html')

@app.route('/create')
def create():
    # meme creation page
    db.drop_all()
    db.create_all()
    # generate sample images for database
    sampleImage1 = Image(imagePath = "/static/images/sample1.png")
    sampleImage2 = Image(imagePath = "/static/images/sample2.png")
    sampleImage3 = Image(imagePath = "/static/images/sample3.png")
    sampleImage4 = Image(imagePath = "/static/images/sample4.png")
    sampleImage5 = Image(imagePath = "/static/images/sample5.png")
    sampleImage6 = Image(imagePath = "/static/images/sample6.png")
    sampleImage7 = Image(imagePath = "/static/images/sample7.png")
    sampleImage8 = Image(imagePath = "/static/images/sample8.png")
    # commit changes:
    db.session.add_all([sampleImage1, sampleImage2, sampleImage3, sampleImage4, sampleImage5, sampleImage6, sampleImage7, sampleImage8])
    db.session.commit()
    print(Image.query.all())
    return render_template('create.html', log_html=Image.query.all())

@app.route('/meettheteam')
def meettheteam():
    # meet the team page
    return render_template('meettheteam.html')

if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)

