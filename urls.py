# -*- coding: utf-8 -*- 

from django.conf.urls   import patterns, include, url
from workshop.views     import homepage, show_map
# Uncomment the next two lines to enable the admin:
from django.contrib     import admin
from settings           import PRODUCTION, MEDIA_ROOT

admin.autodiscover()

from django.conf.urls.static         import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf                     import settings

urlpatterns = patterns('',
	('^$', homepage),
	(r'^accounts/', include('registration.backends.default.urls')),
    (r'^map/$'    , show_map),
    # Examples:
    # url(r'^$', 'maxawd.views.home', name='home'),
    # url(r'^maxawd/', include('maxawd.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()


if not PRODUCTION:   
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    )  

#(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/django/list/static'}),
