from flask import current_app, Blueprint, request, jsonify
from .api_base import api_base_blueprint
from datetime import datetime

events_blueprint = Blueprint('events', __name__, url_prefix='/events')

events = []

def is_valid_date(date_value):
    try:
        datetime.strptime(date_value, '%Y-%m-%d')
        return True
    except ValueError:
        return False

@events_blueprint.route('/', methods=['POST'])
def create_event():
    event_data = request.get_json()
    
    if 'name' not in event_data or not isinstance(event_data['name'], str):
        current_app.logger.warning("Invalid or missing name")
        return jsonify({'error': 'Invalid or missing name'}), 400
    
    if 'date' not in event_data or not is_valid_date(event_data['date']):
        current_app.logger.warning("Invalid or missing date")
        return jsonify({'error': 'Invalid or missing date.', 'format': 'YYYY-MM-DD'}), 400
    
    events.append(event_data)
    return jsonify({'message': 'Event registered successfully'}), 201

@events_blueprint.route('/', methods=['GET'])
def list_events():
    current_app.logger.info("List events")
    return jsonify({'events': events}), 200