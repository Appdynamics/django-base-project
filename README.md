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

## Structure/Organization

This template follows the default folder structure recommended by Django:

```
django-base-project/
|---ansible/
|   |---plugins/
|   |---roles/
|   |   |---webserver/ <-- setup Nginx
|   |---site.yml
|   |---webserver.yml
|   |
|---django-base-project/ <-- remember to change the name!
|   |---.rcfile <-- config for your pylint needs.
|   |---docs/
|   |   |---_build <-- autogenerated by Makefile.
|   |   |---_static
|   |   |---_templates
|   |   |---conf.py <-- edit this file for default doc values.
|   |   |---Makefile
|   |---sample_app/ 
|   |   |---__init__.py
|   |  	|---models/ 
|   |  	|   |---sample_model.py <-- each model should be its own file.
|   |  	|---static/ <-- all app specific static assets go here.
|   |  	|   |---css/
|   |  	|   |---images/
|   |  	|   |---js/
|   |  	|---tests <-- all tests for sample_app should go here.
|   |  	|   |---test_sample_app.py
|   |   |---urls.py
|   |   |---views.py
|   |-- settings/
|	|	|---__init__.py
|	|	|---common.py <-- common settings shared by all environments.
|	|	|---local.py
|	|	|---dev.py
|	|	|---qa.py
|	|	|---staging.py
|	|	|---production.py
|	|---static_common/ <-- (optional) shared static assets by different apps go here.
|	|	|---css/
|	|	|---images/
|	|	|---js/
|   |---manage.py
|   |---requirements.txt <-- all required packages for your Django project to work.
|   |---user-data.json <-- fixture to create your admin user.
```

### Philosophy

This folder structure enables us to follow Django's principle of an application:
> The term **application** describes a Python package that provides some set of features. Applications may be *reused* in various projects.

This means that every application should be self contained, and pluggable into any Django project. This is why each app will have it's own `static` and `tests` folder. In the event that you have static assets that can be shared between two more or more applications, you can move either keep separate copies in each app, or move them one level higher into the `static-commons` folder.

## Code Quality

### Pylint

This Django project comes with a pre-defined rcfile for linting purposes. Edit it to your liking. The project should already be free of any PEP8 warnings or errors.

To lint, just run:

```shell
cd django-base-project
pylint --rcfile=.rcfile *
```

## Documentation

This project comes with a pre-configured `Spinx` Makefile. You can edit the conf.py to fit your documentation purposes. 

To autogenerate documentation for your project:

```shell
cd django-base-project/docs
make html
```

You should see the following output:

```shell
sphinx-build -b html -d _build/doctrees   . _build/html
Running Sphinx v1.3
making output directory...
loading pickled environment... not yet created
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 1 source files that are out of date
updating environment: 1 added, 0 changed, 0 removed
reading sources... [100%] index                                                                                                                                                                                                               
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [100%] index                                                                                                                                                                                                                
generating indices... genindex
writing additional pages... search
copying static files... done
copying extra files... done
dumping search index in English (code: en) ... done
dumping object inventory... done
build succeeded.

Build finished. The HTML pages are in _build/html.
```

As noted in the above console, your documentation will be built into the _build folder.

For more information on Spinx and how to host your documentation, go to:
1. [http://sphinx-doc.org/tutorial.html](http://sphinx-doc.org/tutorial.html)
2. [http://bash-shell.net/blog/2014/apr/19/private-read-docs-private-github-repo/](http://bash-shell.net/blog/2014/apr/19/private-read-docs-private-github-repo/)

## Installation

Python 3.4 is required. If you don't have Python 3.4 or higher, download the appropriate package and install:

```shell
wget https://www.python.org/ftp/python/3.4.3/python-3.4.3-macosx10.6.pkg
```

Then install virtualenv:

```shell
sudo pip3 install virtualenv
```

Create a virtualenv:

```shell
virtualenv -p <PYTHON_3_PATH> ~/virtualenvs/django-base-project
source ~/virtualenvs/django-base-project/bin/activate
~/virtualenvs/django-base-project/bin/pip3 install -r requirements.txt
```

# Deployment

## Local 
When running the project locally for the first time, you need to setup the database.

Activate your virtualenv:
```shell
source ~/virtualenvs/django-base-project/bin/activate
```

Setup the database. Locally, this will create a new sqllite database

```shell
cd django_base_project
python3 manage.py migrate
```

Load initial data. This will create a base admin user with `admin` as the username and `changeme` as the password.

```shell
cd django_base_project
python3 manage.py loaddata user-data.json
```

## Ansible
If you want to deploy this Django app onto an EC2 instance, you can use the provided ansible playbook to do so:

```shell
ansible-playbook -i ec2.py -l<ec2_hostname>
```

## AWS Elastic Beanstalk

This project is ready to deploy in Elastic Beanstalk. All you need is to set your AWS credentials like so:

```shell
export AWS_ACCESS_KEY_ID="<your_aws_access_key>"
export AWS_SECRET_KEY="<your_aws_secret_key>"
```

Next, initialize your project for Elastic Beanstalk:

```
eb init
```

Finally, deploy your code!

```
eb deploy
```

For more information on deploying a Django app into Elastic Beanstalk, you can visit AWS's documentation here: http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_Python_django.html

# Testing

In the provided sample app `sample_app`, there's a tests directory that implements some sample test cases that show how different test classes can be leveraged by the Django application. 

To start the tests, simply run:
```shell
python3 manage.py test
```

You should see the following output:

```shell
python3 manage.py test
Creating test database for alias 'default'...
...
----------------------------------------------------------------------
Ran 3 tests in 3.049s

OK
Destroying test database for alias 'default'...
```

## Selenium Testing

This project also provides the `selenium` so you can quickly spin up your site (on a different port) and test it against various browsers.

```shell
python3 manage.py test django_base_project.sample_app.SampleSeleniumTests
```

## Code Coverage

