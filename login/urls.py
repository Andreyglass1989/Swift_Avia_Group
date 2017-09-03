from django.conf.urls import url
from login.views import login, logout, register
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^register/$', register),
    url(r'^reset_password/$', password_reset, name='reset_password'),
    url(r'^reset_password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset_password/complete/$', password_reset_complete, name='password_reset_complete'),
]
