from django.conf.urls.defaults import *

urlpatterns = patterns('socialeditor.views',
    # home
    url(r'^$', 'home', name='home'),

    # profiles
    url(r'^user/(\w+)/$', 'view_profile', name='view_profile'),
    url(r'^user/(\w+)/edit/$', 'edit_profile', name='edit_profile'),

    # friends
    url(r'^add-friend/(\w+)/$', 'add_friend', name='add_friend'),     
    url(r'^remove-friend/(\w+)/$', 'remove_friend', name='remove_friend'),

    # groups
    url(r'^create-group/', 'create_group', name='create_group'),
    url(r'^group/(\w+)/', 'view_group', name='view_group'),
    url(r'^group/(\w+)/edit/', 'edit_group', name='edit_group'),
    url(r'^group/(\w+)/add/(\w+)/', 'add_member', name='add_member'),
    url(r'^group/(\w+)/leave/', 'leave_group', name='leave_group'),

    # routines
    url(r'^create-routine/$', 'create_routine', name='create_routine'),
    url(r'^routine/(\w+)/$', 'view_routine', name='view_routine'),
    url(r'^routine/(\w+)/edit/$', 'edit_routine', name='edit_routine'),
    url(r'^routine/(\w+)/edit/save/$', 'save_routine', name='save_routine'),
    url(r'^routine/(\w+)/edit/delete/$', 'delete_routine', name='delete_routine'),

    # videos
    url(r'^routine/(\w+)/edit/add-video/$', 'add_video', name='add_video'),
    url(r'^routine/(\w+)/edit/edit-video/(\w+)/$', 'edit_video', name='edit_video'),
    url(r'^routine/(\w+)/edit/remove-video/(\w+)/$', 'remove_video', name='remove_video'),
)
