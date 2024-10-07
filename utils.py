def Get_planner_data(planner_id):
    """
    Will give all planned events in planner with their respective information
    """
    response = "json with all parameters needed"
    status_code = 1  # int with status of operation
    return response, status_code


def Create_event(request):
    """
    Will create event with id, name, date, created_by, description, votes_for, votes_against
    """
    response = "json with all parameters needed"
    status_code = 1  # int with status of operation
    return response, status_code


def Create_vote(request):
    """
    Will create vote with email, for, against.

    If vote breaks the threshold for event, send calendar events

    If new vote comes in after threshold, update event for other members
    """
    response = "json with all parameters needed"
    status_code = 1  # int with status of operation
    return response, status_code


def publish_event_calendar(event_emails, event_date, event_name, event_description):
    """
    Post event on google calendar of registered emails.
    """


def modify_event_calendar():
    """
    Modify calendar event once more people join the event.
    """
