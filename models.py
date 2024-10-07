from flask_sqlalchemy import SQLAlchemy
from main import db


# Define the Planner model
class Planner(db.Model):
    __tablename__ = "Planners"

    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(20), nullable=False)

    # Relationship to Events
    events = db.relationship("Event", backref="planner", lazy=True)


# Define the Event model
class Event(db.Model):
    __tablename__ = "Events"

    id = db.Column(db.Integer, primary_key=True)
    planner_id = db.Column(db.Integer, db.ForeignKey("Planners.id"), nullable=False)
    name = db.Column(db.String(16), nullable=False)
    date = db.Column(db.String(16), nullable=False)
    author = db.Column(db.String(16), nullable=False)
    description = db.Column(db.String(16), nullable=True)
    votes_for = db.Column(db.Integer, default=0)
    votes_against = db.Column(db.Integer, default=0)
    status = db.Column(db.String(16), nullable=False)

    # Relationship to Votes
    votes = db.relationship("Vote", backref="event", lazy=True)


# Define the Vote model
class Vote(db.Model):
    __tablename__ = "Votes"

    event_id = db.Column(db.Integer, db.ForeignKey("Events.id"), primary_key=True)
    email = db.Column(db.String(16), primary_key=True)
    for_vote = db.Column(db.Integer, default=0)
    against_vote = db.Column(db.Integer, default=0)
