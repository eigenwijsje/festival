from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.static import serve

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^accounts/', include('registration.urls')),
    (r'^contact/', include('contact_form.urls')),
    (r'^installfest/', include('installfest.urls')),
    (r'^sitemedia/(.*)', serve, {'document_root': 'sitemedia'}),
)
