import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project_heroku_template.settings')

application = get_wsgi_application()
