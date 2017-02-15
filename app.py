#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from flask import Flask, render_template
from flask_pymongo import PyMongo
from bson.json_util import dumps


app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'bank_db'
app.config['MONGO_USERNAME'] = 'yourUserNameHere'
app.config['MONGO_PASSWORD'] = 'yourPasswordHere'

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/projects')
def projects():
    collection = mongo.db.bank_col
    result = collection.aggregate( [  
     { "$group" : { "_id" : { "project": "$project_name", "country":  "$countryname", "cost": "$lendprojectcost", "code": "$countrycode" }} },
     #{ "$match": { "_id.country": "Republic of Kenya"}},
     #{ "$limit": 5}  
      ] )
    return dumps(result)

@app.route('/one')
def one():
    collection = mongo.db.bank_col
    result = collection.find_one()
    return dumps(result)

if __name__ == '__main__':
    app.run(debug=True)