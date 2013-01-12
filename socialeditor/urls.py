from django.conf.urls.defaults import *

urlpatterns = patterns('socialeditor.views',
    url(r'^$', 'home', name='home'),
    url(r'^new/$', 'create_profile', name="create_profile"),
    url(r'^(?P<short_name>\w+)/$', 'view_profile', name='view_profile'),
    url(r'^(?P<short_name>\w+)/delete/$', 'delete_profile', name="delete_profile"),
    url(r'^(?P<short_name>\w+)/new/$', 'create_routine', name="create_routine"),
    url(r'^(?P<short_name>\w+)/(?P<routine_id>\w+)/$', 'view_routine', name='view_routine'),
    url(r'^(?P<short_name>\w+)/(?P<routine_id>\w+)/edit/$', 'edit_routine', name='edit_routine'),
    url(r'^(?P<short_name>\w+)/(?P<routine_id>\w+)/edit/save/$', 'save_routine', name='save_routine'),
    url(r'^(?P<short_name>\w+)/(?P<routine_id>\w+)/edit/add-video/$', 'add_video', name='add_video'),
    url(r'^(?P<short_name>\w+)/(?P<routine_id>\w+)/edit/edit-video/(?P<video_id>\w+)/$', 'edit_video', name='edit_video'),
    url(r'^(?P<short_name>\w+)/(?P<routine_id>\w+)/edit/remove-video/(?P<video_id>\w+)/$', 'remove_video', name='remove_video'),
    url(r'^(?P<short_name>\w+)/(?P<routine_id>\w+)/edit/delete/$', 'delete_routine', name='delete_routine'),
)
