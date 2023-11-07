from flask import Flask
from .api_base import api_base_blueprint
from .events import events_blueprint

def create_app():
    app = Flask(__name__)
    
    api_base_blueprint.register_blueprint(events_blueprint)
    app.register_blueprint(api_base_blueprint)
        
    return app
