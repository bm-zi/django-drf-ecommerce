# Packages

Django 5  
python-dotenv 1.0.1  
djangorestframework 3.15.1  
pytest 8.1.1  
pytest-django 4.8.0  
django-mptt
drf-spectacular
pytest-cov
coverage
pytest-factoryboy
pygments
sqlparse
pillow

# commands

django-admin startproject drfcommerce

./manage.py runserver

./manage.py shell

from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())

pip install --upgrade pip

coverage run -m pytest

./manage.py makemigrations

./manage.py migrate

./manage.py createsuperuser

## pytest

pytest -h # prints options _and_ config file settings
