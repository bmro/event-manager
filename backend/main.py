import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    debug_mode = os.getenv('DEBUG_MODE', 'False') == 'True'
    app.run(debug=debug_mode)
