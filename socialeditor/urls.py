from django.conf.urls.defaults import *

urlpatterns = patterns('socialeditor.views',
    url(r'^$', 'home', name='home'),
)
