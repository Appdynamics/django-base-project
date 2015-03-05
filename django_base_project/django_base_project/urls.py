from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'django_base_project.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
)
