from django.conf.urls import url
from . import views

#app_name = 'movieapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<movie_id>[0-9]+)/$', views.info, name='info'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^movies/(?P<movie_genre>[-\w]+)/$', views.movies_by_genre, name='movies_by_genre'),
    url(r'^shows/(?P<city_name>[-\w]+)/$', views.shows_by_city, name='shows_by_city'),
    url(r'^buy/$', views.buy, name='buy'),
    url(r'^theatres/$', views.theatres, name='theatres'),
    url(r'^search/$', views.search, name='search'),
    #-------------------------------Pelkät toiminnot------------------------------------
    url(r'^buy_tickets/$', views.buy_tickets, name='buy_tickets'),
    url(r'^remove_ticket/(?P<ticket_id>[0-9]+)/$', views.remove_ticket, name='remove_ticket'),
    url(r'^login_view/$', views.login_view, name='login_view'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^post_comment/(?P<movie_id>[0-9]+)/$', views.post_comment, name='post_comment'),
    url(r'^change_password/$', views.change_password, name='change_password'),
]
