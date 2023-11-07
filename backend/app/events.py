from flask import Blueprint, request, jsonify
from .api_base import api_base_blueprint

events_blueprint = Blueprint('events', __name__, url_prefix='/events')

events = []

@events_blueprint.route('/', methods=['POST'])
def create_event():
    event_data = request.get_json()
    events.append(event_data)
    return jsonify({'message': 'Event registered successfully'}), 201

@events_blueprint.route('/', methods=['GET'])
def list_events():
    return jsonify({'events': events}), 200