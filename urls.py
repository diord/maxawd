from django.conf.urls import patterns, include, url

from workshop.views import homepage

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	('^$', homepage),
    # Examples:
    # url(r'^$', 'maxawd.views.home', name='home'),
    # url(r'^maxawd/', include('maxawd.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
