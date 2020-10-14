import flask
import pandas as pd
from flask import jsonify
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)

# De data wordt ingeladen

df = pd.read_json(
    r'/Users/milouvanlaarhoven/PycharmProjects/zomer2020/api/csvjson.json')

df.drop(df.loc[df["Hoe voel je je vandaag?"] == ""].index, inplace=True)

df["Hoe voel je je vandaag?"] = df["Hoe voel je je vandaag?"].astype(float)


@app.route('/analyse/average/feeling', methods=['GET'])
def average_student():

    average = df["Hoe voel je je vandaag?"].mean()

    return jsonify(average), 200


app.run()

# http://127.0.0.1:5000/analyse/average/feeling
