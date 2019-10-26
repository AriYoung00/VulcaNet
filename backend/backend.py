from flask import Flask
from flask import request
from flask_pymongo import PyMongo

import json

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/fire"
mongo = PyMongo(app)


@app.route("/sensors/list", methods=["POST", "GET"])
def sensors_list():
    data = mongo.db.data.find({
        "dataTypes": {"$exists": True}
    })

    try:
        return json.dumps({'dataTypes': data[0]['dataTypes']})
    except IndexError:
        return json.dumps({'dataTypes': []})


@app.route("/sensors/get_sensor/<sensor>", methods=["POST"])
def get_sensor(sensor):
    try:
        min_date = request.data['min_date'];
    except KeyError:
        min_date = ""

    try:
        max_date = request.data['']

    data = mongo.db.data.find({
        "sensorType": sensor
    })
    dict_arr = []
    for thing in data:
        temp = dict(thing)
        dict_arr.append(thing)

    for blah in dict_arr:
        blah.pop("_id")
    # for item in data:
    #     i += 1
    # return json.dumps({"dataVals": [item for item in data]})

    return json.dumps({"dataValues": dict_arr})

