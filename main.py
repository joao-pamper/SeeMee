from flask import Flask, render_template, request
from utils import Get_planner_data, Create_event, Create_vote
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Set up the database URI (SQLite for now)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///seemee.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the app with the SQLAlchemy database
db = SQLAlchemy(app)


# # Create the tables before the first request
# @app.before_first_request
# def create_tables():
#     db.create_all()


@app.route("/")
def landing_page():
    return render_template("home.html")


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


# Handle any unexpected server errors
@app.errorhandler(500)
def internal_error(error):
    return {"error": "An internal error occurred"}, 500
