#!/bin/sh

# Wait for the database to be ready (optional)
# sleep 10

# Run migrations and collect static files (if needed)
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Then execute the container's main command
exec "$@"
