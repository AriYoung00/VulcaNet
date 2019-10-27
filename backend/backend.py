from flask import Flask
from flask import request
from flask_pymongo import PyMongo

import json

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/fire"
mongo = PyMongo(app)


# endpoint that lists available sensors
@app.route("/sensors/list", methods=["POST", "GET"])
def sensors_list():
    data = mongo.db.data.find({
        "dataTypes": {"$exists": True}
    })

    try:
        return json.dumps({'dataTypes': data[0]['dataTypes']})
    except IndexError:
        return json.dumps({'dataTypes': []})

# this gets information for all values of any sensor of type <sensor>
@app.route("/sensors/get_sensor/<sensor>", methods=["GET"])
def get_sensor(sensor):
# check if post request body has a cutoff for values to return
    try:
        min_date = request.data['min_date'];
    except KeyError:
        min_date = ""

    try:
        max_date = request.data['max_date']
    except KeyError:
        max_date = ""

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


@app.route("/sensors/add_data/<sensor>", methods=(["POST"]))
def add_data(sensor):
    data = mongo.db.data.sensorTypes.find({'sensor': sensor})
    timeReceived = request.json['timeReceived']
    values = request.json['values']

    return json.dumps({''})


@app.route("/fire/get_prob/", methods=(["GET"]))
def get_prob():
    data = mongo.db.data.find({'fireProbability'})
    res = json.dumps({'fireProbability': data['fireProbability']})
    return res


@app.route("/fire/update_prob/", methods=(["POST"]))
def update_prob():
    data = mongo.db.data
    prob = request.json['fireProbability']
    prob_id = data.update({'fireProbability', prob})
    return json.dumps({'result': prob})

