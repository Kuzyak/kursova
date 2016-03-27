from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^foto/(?P<pk>[0-9]+)/$', views.foto_view, name='foto_view'),
    url(r'^foto/(?P<pk>[0-9]+)/edit/$', views.foto_edit, name='foto_edit'),
    url(r'^finish/$', views.foto_out, name='foto_out'),
]
