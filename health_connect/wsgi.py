import os
import sys
from django.core.management import call_command

# Add project directory to path
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'health_connect.settings')

# Collect static files on first import (Vercel deployment)
if os.environ.get('VERCEL'):
    print("Running on Vercel - collecting static files...")
    import django
    django.setup()
    call_command('collectstatic', '--noinput', '--clear')
    print("Static files collected!")

from django.core.wsgi import get_wsgi_application


app = get_wsgi_application()
