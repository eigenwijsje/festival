from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail

from models import Event
from views import register, site_detail

event_info = {
    'queryset': Event.objects.all(),
    'template_object_name': 'event',
}

urlpatterns = patterns('',
    url(r'^$',
        object_list,
        event_info,
        name='event-list'),
    url(r'^(?P<slug>[\w-]+)/$',
        object_detail,
        dict(event_info, slug_field='slug'),
        name='event-detail'),
)

urlpatterns += patterns('',
    url(r'^(?P<event_slug>[\w-]+)/(?P<site_slug>[\w-]+)/$',
        site_detail,
        name='site-detail'),
    url(r'^(?P<event_slug>[\w-]+)/(?P<site_slug>[\w-]+)/register/$',
        register,
        name='register'))
