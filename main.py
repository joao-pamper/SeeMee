from flask import Flask, render_template, request
from utils import Get_planner_data, Create_event, Create_vote


app = Flask(__name__)


@app.route("/")
def landing_page(planner_id):
    return render_template("landing.html")


@app.route("/planner/<int:planner_id>")
def planner_page(planner_id):
    return render_template("planner.html")


@app.get("/api/planner/<int:planner_id>")
def get_planner_data(planner_id):
    response, status_code = Get_planner_data(planner_id)
    return response, status_code


@app.post("/api/event/")
def create_event():
    response, status_code = Create_event(request.json)
    return response, status_code


@app.post("/api/vote/")
def create_vote():
    response, status_code = Create_vote(request.json)
    return response, status_code
