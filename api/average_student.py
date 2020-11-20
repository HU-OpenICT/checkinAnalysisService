import flask
from flask import jsonify, request
from flask_cors import CORS


app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)


@app.route("/analyse/average", methods=["POST"])
def average():
    data = request.json

    total_feeling = 0
    feeling_count = 0

    team_ids = []
    team_temporary = {}

    # verzamel alle team ids
    for checkin in data:
        if checkin["Welke squad zit je?"] not in team_ids:
            team_ids.append(checkin["Welke squad zit je?"])

    # initieer alle team data op 0
    for team_id in team_ids:
        team_temporary[team_id] = {"total": 0, "count": 0}

    # loop door alle checkins heen
    for checkin in data:
        # onthoud het team id
        team_id = checkin["Welke squad zit je?"]
        # tel gevoel van deze checkin bij team waarde op
        team_temporary[team_id]["total"] = team_temporary[team_id]["total"] + checkin["Hoe voel je je vandaag?"]
        # hoog het aantal van dit team op met één
        team_temporary[team_id]["count"] = team_temporary[team_id]["count"] + 1

    # gemiddelde van alle checkins
    for checkin in data:
        total_feeling = total_feeling + checkin["Hoe voel je je vandaag?"]
        feeling_count = feeling_count + 1

    average_feeling = total_feeling / feeling_count

    return jsonify({"average_feeling": average_feeling})


@app.route("/analyse/average/team", methods=["POST"])
def average_team():
    data = request.json

    total_feeling = 0
    feeling_count = 0

    team_feeling = []
    team_ids = []
    team_temporary = {}

    # verzamel alle team ids
    for checkin in data:
        if checkin["Welke squad zit je?"] not in team_ids:
            team_ids.append(checkin["Welke squad zit je?"])

    # initieer alle team data op 0
    for team_id in team_ids:
        team_temporary[team_id] = {"total": 0, "count": 0}

    # loop door alle checkins heen
    for checkin in data:
        # onthoud het team id
        team_id = checkin["Welke squad zit je?"]
        # tel gevoel van deze checkin bij team waarde op
        team_temporary[team_id]["total"] = team_temporary[team_id]["total"] + checkin["Hoe voel je je vandaag?"]
        # hoog het aantal van dit team op met één
        team_temporary[team_id]["count"] = team_temporary[team_id]["count"] + 1

    # gemiddelde van alle checkins
    for checkin in data:
        total_feeling = total_feeling + checkin["Hoe voel je je vandaag?"]
        feeling_count = feeling_count + 1

    # voor alle teams het gemiddelde uitrekeken
    for team_id, team_temp in team_temporary.items():
        # gemiddelde is total/count
        average_team_feeling = team_temp["total"] / team_temp["count"]
        # sla het gemiddelde op in lijst van feelings
        team_feeling.append({"team_id": team_id, "team_feeling": average_team_feeling})

    average_feeling = total_feeling / feeling_count

    return jsonify({"average_feeling": average_feeling, "team_feeling": team_feeling})


app.run()
# http://127.0.0.1:5000/analyse/average
