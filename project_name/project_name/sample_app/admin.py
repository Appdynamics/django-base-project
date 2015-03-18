from django.contrib import admin
from {{ project_name }}.sample_app.models import Kid, Dog

admin.site.register(Dog)
admin.site.register(Kid)