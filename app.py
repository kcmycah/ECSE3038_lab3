from marshmallow import Schema, fields, ValidationError
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
from datetime import datetime as dt
from flask_cors import CORS
from json import loads
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_CONNECTION_STRING")
mongo = PyMongo(app) #creates an instance of PyMongo object
CORS(app)

db_tanks = mongo.db.tanks

#PROFILE DATABASE
global now
now= dt.now()

profileDB = {
  "success": True,
  "data": {
    "last_updated": now,
    "username": "goodgyalkai",
    "role": "BOSSLADY",
    "color": "Green"
    }
}

class TankSchema(Schema):
  location = fields.String(required=True)
  latitude  = fields.String(required=True)
  longitude = fields.String(required=True)
  percentage_full = fields.Integer(required=True)

@app.route("/")
def home():
  return "Welcome to da clubbb"

@app.route("/profile", methods=["GET", "POST", "PATCH"])
def getProfile():
  if request.method == "GET":
    return jsonify(profileDB)

  elif request.method == "POST":
    global now
    now= dt.now()

    profileDB["data"]["last_updated"] = (now)
    profileDB["data"]["username"] = (request.json["username"])
    profileDB["data"]["role"] = (request.json["role"])
    profileDB["data"]["color"] = (request.json["color"])

    return jsonify(profileDB)

  elif request.method == "PATCH":
    
    now = dt.now()
    request.json["last_updated"] = now
    attributes = request.json.keys()
    for i in attributes:
        profileDB[i] = request.json[i]

    return jsonify(profileDB)  


#DATA ROUTES
@app.route("/data", methods=["GET", "POST"])
def tankData():
  if request.method == "GET":
    newTanks = mongo.db.tanks.find()
    return jsonify(loads(dumps(newTanks)))  
    
  elif request.method == "POST":
    try:
      newTanks = TankSchema().load(request.json)
      mongo.db.tanks.insert_one(newTanks)
      return loads(dumps(newTanks))
      
    except ValidationError as e:
      return e.messages, 400   
 

@app.route('/data/<ObjectId:id>', methods=["PATCH", "DELETE"])
def tankId(id):
  if request.method == "PATCH":
    mongo.db.tanks.update_one({"_id": id}, {"$set": request.json})
    newTank = mongo.db.tanks.find_one(id)
    return loads(dumps(newTank))
  
  elif request.method == "DELETE":
    result = mongo.db.tanks.delete_one({"_id": id})
    if result.deleted_count == 1:
      return {
        "success": True
        }
    else:
      return {
        "success": False
        }, 400


if __name__ == '__main__':
  app.run(debug = True,port = 3000, host = "0.0.0.0" )