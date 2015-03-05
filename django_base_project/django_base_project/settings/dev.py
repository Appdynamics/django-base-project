from django_base_project.settings.common import *

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': os.environ['RDS_DB_NAME'],
		'USER': os.environ['RDS_USERNAME'],
		'PASSWORD': os.environ['RDS_PASSWORD'],
		'HOST': os.environ['RDS_HOSTNAME'],
		'PORT': os.environ['RDS_PORT'],
	}
}