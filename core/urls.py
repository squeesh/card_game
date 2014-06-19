from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$',                          'core.views.index',         name='index'),
    url(r'^create/$',                   'core.views.create_game',   name='core.create_game'),
    url(r'^join/(?P<game_id>\d+)/$',    'core.views.join_game',     name='core-join_game'),
    url(r'^hand/$',                     'core.views.view_hand',     name='core-view_hand'),
    url(r'^draw-deck/$',                'core.views.draw_deck',     name='core-deck_draw'),
    url(r'^draw-pile/$',                'core.views.draw_pile',     name='core-draw_pile'),
    url(r'^discard/(?P<card_pos>\d+)/$','core.views.discard',       name='core-discard'),
    url(r'^pile/$',                     'core.views.view_pile',     name='core-view_pile'),
    url(r'^swap/(?P<pos_a>\d+)/(?P<pos_b>\d+)/$',
                                        'core.views.card_pos_swap', name='core-card_pos_swap'),

    url(r'^admin/', include(admin.site.urls)),
)
