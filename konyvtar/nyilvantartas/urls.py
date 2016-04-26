from django.conf.urls import url

from . import views

app_name = 'nyilvantartas'
urlpatterns = [
    # ex: /nyilvantartas/
    url(r'^$', views.index, name='index'),
    # ex: /nyilvantartas/5/
    url(r'^(?P<lending_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /nyilvantartas/kolcsonzes/
    url(r'^kolcsonzes/$', views.lending, name='lending'),
]