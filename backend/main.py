import os
from app import create_app
from app.extensions import db
from flask_migrate import Migrate

app = create_app()
db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    debug_mode = os.getenv('DEBUG_MODE', 'False') == 'True'
    app.run(debug=debug_mode)