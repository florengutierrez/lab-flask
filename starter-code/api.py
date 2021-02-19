from flask import Flask
from helpers.mongoConnection import read
from bson import json_util

app = Flask("hollywoodapi")

@app.route("/celebrities")
def celebrities():
    data = read({}, "celebrities", project={"name:1"})
    return json_util.dumps(data)


@app.route("/celebrities/details/<celebrity_id>")
def celebrities_details(celebrity_id):
    try:
        id_ = ObjectId(celebrity_id)
    except:
        return {"Error": "celebrity_id not valid!"}
    
    q = {"_id": id_}
    data = read(q,"celebrities")
    if len(data) == 0:
        return {"Error":"No celebrity with given id!"}
    return json_util.dumps(data)




app.run(debug=True)
