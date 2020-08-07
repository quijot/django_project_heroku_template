==============================
django_project_heroku_template
==============================

*A Django project template ready for heroku*, using

- Python >=3.6 (because we love ``f-strings``)
- Django >=3.0,<4

:Usage: Just clone this repo and follow the instructions below...


.. contents:: Tools

Virtual Environment
-------------------

Enter the project directory and create a virtualenv with your favorite method:

::

    cd django_project_heroku_template
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Deployment
----------

- `heroku <https://www.heroku.com/>`_ (install heroku-cli)

- select some proper <<herokuapp_name>>

- edit ALLOWED_HOSTS in settings.py (change <<herokuapp_name>>, without << and >>, of course)

::

    heroku create <<herokuapp_name>>
    git push heroku master
    heroku run python manage.py migrate
    heroku run python manage.py createsuperuser
    heroku config:set DJANGO_SECRET_KEY='<<your-secret-key>>'

Get one here: `Django Secret Key Generator <https://www.miniwebtool.com/django-secret-key-generator/>`_

``heroku config:set DJANGO_DEBUG='False'``

... and that's it, you are ready for starting your own app.

