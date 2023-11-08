#!/bin/sh

# Check if the migrations folder exists
if [ ! -d "migrations" ]; then
    echo "Migrations directory not found, running 'flask db init'"
    flask db init
    flask db migrate -m "Initial migration."
fi

flask db upgrade
exec "$@"
