django-base-project
===================
This is a base django project that comes with everything we need to get started on fun, innovative stuff.

## Features ##

By default, this project template includes:

Templating:

- django_compressor for compressing javascript/css/less/sass

Security:

- hashlib
- m2crypto

Background Tasks:

- Celery

Migrations:

- Django built-in migrations (Django >=1.7)

Caching:

- django-redis

Testing:

- pytest
- pytest-coverage

Authentication:

- python-social-auth for OAuth with social networks

Amazon:

- boto for integration with AWS

Any of these options can added, modified, or removed as you like after creating your project.

## Installation

Python 3.4 is required. If you don't have Python 3.4 or higher, download the appropriate package and install:

```
wget https://www.python.org/ftp/python/3.4.3/python-3.4.3-macosx10.6.pkg
```

Then install virtualenv:

```
sudo pip3 install virtualenv
```

Create a virtualenv:

```
virtualenv -p <PYTHON_3_PATH> ~/virtualenvs/django-base-project
source ~/virtualenvs/django-base-project/bin/activate
~/virtualenvs/django-base-project/bin/pip3 install -r requirements.txt
```

## Deployment

When running the project locally for the first time, you need to setup the database.

Activate your virtualenv:
```
source ~/virtualenvs/django-base-project/bin/activate
```

Setup the database. Locally, this will create a new sqllite database

```
cd django_base_project
python3 manage.py migrate
```

Load initial data. This will create a base admin user with `admin` as the username and `changeme` as the password.

```
cd django_base_project
python3 manage.py loaddata users.json
```

