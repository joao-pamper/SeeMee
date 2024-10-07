from flask_sqlalchemy import SQLAlchemy
from models import Planner, Event, Vote
from main import db


# Example function to create a new planner
def create_planner(group_name):
    new_planner = Planner(group_name=group_name)
    db.session.add(new_planner)
    db.session.commit()


def get_events(planner_id):
    """
    returns a list of events.
    """
    events = Event.query.filter_by(planner_id=planner_id).all()

    return events
