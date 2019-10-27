import serial
import pymongo
import time

import fire_risk

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = client["fire"]

update_build = {}


def get_categories():
    data = db.data.find({
        "dataTypes": {"$exists": True}
    })

    try:
        return data[0]['dataTypes']
    except IndexError:
        return []


def add_category(category):
    data = db.data.find({
        "dataTypes": {"$exists": True}
    })

    try:
        current_types = data[0]['dataTypes']
    except Exception:
        current_types = [category]
        db.data.insert_one({"dataTypes": current_types})
        return

    current_types.append(category)
    db.data.update_one({ "dataTypes": { "$exists": True }},
                  { "$set": { "dataTypes": current_types }})


def handle_msg_rcv(msg):
    global update_build

    stamp = int(time.time())
    data = msg[2].split(".")

    for i in range(0, len(data), 2):
        if data[i] != "groveTemp" and data[i] != "sparkTVOC":
            update_build[data[i]] = int(data[i+1])
        if data[i] not in get_categories():
            add_category(data[i])

        db.data.insert_one({"timestamp": stamp, "sensorType": data[i], "sensorData": int(data[i+1])})

        if len(update_build) == 4:
            risk = 100 * fire_risk.calculate_risk(update_build['adaAlt'], update_build['adaTemp'],
                                                  update_build['adaBaro'], update_build['sparkCO2'])
            update_build = {}
            db.risk.update_one({"mostRecent": {"$exists": True}},
                               {"$set": {"score": risk}})




def main():
    ino = serial.Serial("/dev/ttyUSB0", 115200, timeout=1)

    while True:
        msg_in = ino.readline().decode("UTF-8").strip('\n')
        if len(msg_in) < 2:
            continue
        if msg_in[0] == '-' and msg_in[1] == '>':
            print(msg_in)
            continue
        msg_in = msg_in.split(":")

        if msg_in[0] == 'msgRcv':
            handle_msg_rcv(msg_in)


if __name__ == "__main__":
    main()
