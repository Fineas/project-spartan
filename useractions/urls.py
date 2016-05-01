from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^submit/$', views.create_post, name='submit'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^spartan/$', views.spartan, name='spartan'),
    url(r'^general/$', views.profileGeneral, name='profilGeneral')
]
