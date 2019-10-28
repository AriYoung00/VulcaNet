from flask import Flask
from flask import request
from flask_pymongo import PyMongo

import json

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/fire"
mongo = PyMongo(app)


# endpoint that lists available sensors
@app.route("/sensors/list/", methods=["POST", "GET"])
def sensors_list():
    data = mongo.db.data.find({
        "dataTypes": {"$exists": True}
    })

    try:
        return json.dumps({'dataTypes': data[0]['dataTypes']})
    except IndexError:
        return json.dumps({'dataTypes': []})

# this gets information for all values of any sensor of type <sensor>
@app.route("/sensors/get_sensor/<sensor>", methods=["POST"])
def get_sensor(sensor):
    # check if post request body has a cutoff for values to return
    stuff = json.loads(request.data.decode("UTF-8"))
    try:
        min_date = int(stuff['min_date'])
    except KeyError or ValueError:
        min_date = "1"

    data = mongo.db.data.find({
        "sensorType": sensor,
        "timestamp": {
            "$gte": min_date
        }
    })

    dict_arr = []
    for thing in data:
        temp = dict(thing)
        dict_arr.append(thing)

    for blah in dict_arr:
        blah.pop("_id")

    return json.dumps({"dataValues": dict_arr})


@app.route("/sensors/active_num/")
def active_sensors():
    data = mongo.db.risk.find({
        "numNodes": {"$exists": True}
    })

    return data[0]['numNodes']


@app.route("/fire/get_prob/", methods=(["POST"]))
def get_prob():
    data = mongo.db.risk.find({"mostRecent": {"$exists": True}})

    return "%.2f" % data[0]['score']


