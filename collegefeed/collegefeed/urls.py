from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'collegefeed.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #renders api for results
    url(r'^api/results/(?P<category>[0-9]+)$', 'api.views.results',name='results'),
    #renders api for dubeatContent
    url(r'^api/duNews/(?P<category>[0-9]+)$', 'api.views.duNews',name='duNews'),

)
