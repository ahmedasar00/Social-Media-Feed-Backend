import os
from django.core.wsgi import get_wsgi_application

# تأكد إنه نفس الـ settings اللي في manage.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

application = get_wsgi_application()
