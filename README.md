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
