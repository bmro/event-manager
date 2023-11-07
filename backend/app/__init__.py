import os
from flask import Flask, jsonify
from flask_cors import CORS
from .api_base import api_base_blueprint
from .events import events_blueprint


def create_app():
    app = Flask(__name__)
    CORS(app)
    
    log_level = os.getenv('LOG_LEVEL', 'ERROR').upper()
    app.logger.setLevel(log_level)
    
    @app.errorhandler(404)
    def not_found_error(error):
        app.logger.warning("Not found")
        return jsonify({'error': 'Resource not found'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        app.logger.error("Internal server error")
        return jsonify({'error': 'Internal server error'}), 500

    api_base_blueprint.register_blueprint(events_blueprint)
    app.register_blueprint(api_base_blueprint)
    
    return app