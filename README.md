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

Python 3.4 is required. 

You must have `pip` and `virtualenv` installed. These may already be installed for you. If not, install `pip` with:

```
sudo easy_install pip
```

And then use `pip` to install `virtualenv`:

```
sudo pip install virtualenv
```

Create a virtualenv:

```
virtualenv -p <PYTHON_3_PATH> ~/virtualenvs/django-base-project
source ~/virtualenvs/django-base-project/bin/activate
~/virtualenvs/django-base-project/bin/pip3 install -r requirements.txt
```
