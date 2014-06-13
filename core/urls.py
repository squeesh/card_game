from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$',                          'core.views.index',         name='index'),
    url(r'^create/$',                   'core.views.create_game',   name='core.create_game'),
    url(r'^join/(?P<game_id>\d+)/$',    'core.views.join_game',     name='core-join_game'),
    url(r'^admin/', include(admin.site.urls)),
)
