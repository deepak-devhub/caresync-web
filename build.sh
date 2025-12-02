#!/bin/bash
set -e
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear --no-input
echo "Static files collected successfully"
