from flask import current_app, Blueprint, request, jsonify
from datetime import datetime
from .models import Event
from .extensions import db

events_blueprint = Blueprint('events', __name__)

def is_valid_date(date_value):
    current_app.logger.debug("validating date `%s`", date_value)
    try:
        datetime.strptime(date_value, '%Y-%m-%d')
        return True
    except ValueError:
        return False

@events_blueprint.route('/events', methods=['POST'])
def create_event():
    event_data = request.get_json()
    current_app.logger.debug("creating event, raw data `%s`", event_data)
    
    if 'name' not in event_data or not isinstance(event_data['name'], str):
        current_app.logger.warning("Invalid or missing name")
        return jsonify({'error': 'Invalid or missing name'}), 400
    
    if 'date' not in event_data or not is_valid_date(event_data['date']):
        current_app.logger.warning("Invalid or missing date")
        return jsonify({'error': 'Invalid or missing date.', 'format': 'YYYY-MM-DD'}), 400
    
    new_event = Event(name=event_data['name'], date=datetime.strptime(event_data['date'], '%Y-%m-%d'))
    current_app.logger.debug("creating event, new_event data `%s`", new_event)
    db.session.add(new_event)
    db.session.commit()
    current_app.logger.info("Event registered successfully")
    return jsonify({'message': 'Event registered successfully'}), 201

@events_blueprint.route('/events', methods=['GET'])
def list_events():
    events = Event.query.all()
    events_list = [{"name": event.name, "date": event.date.strftime('%Y-%m-%d')} for event in events]
    current_app.logger.info("List events")
    return jsonify({'events': events_list}), 200