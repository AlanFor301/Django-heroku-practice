# Django-heroku-practice
## General
+ Install django(on Windows system, if easy_install django does not work, use pip install django) and check django version by using command: python -c "import django; print(django.get_version())"
* I found some installation error when using easy_install on a Chinese Windows system (FIX-ME: fix dir name error).
* Run server by using command: python manage.py runserver
## File explanation:
* Manage.py: comes with the Django(access to database: create user, etc.)
* __init__.py: make the package a python package.
* setting.py : setting and configuration for the package.
* url.py     : table content for the website.
* wsgi.py    : web server gateway.
## url:
* In each app url.py file, '$' is use for default app name.
## Migration:
* When running the server, if there is a line says you have # unapplied migrations, run command: python manage.py migrate
* When create a new unit in models.py, use command python manage.py makemigrations <class_name>; then migrate again
## models.py:
* Each class created in models.py, the database will create a column.
