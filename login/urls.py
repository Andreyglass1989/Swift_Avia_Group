from django.conf.urls import url
from login.views import login, logout, register, inkognito_pack
from django.contrib.auth.views import (
	password_reset, 
	password_reset_done, 
	password_reset_confirm, 
	password_reset_complete,
	)
from django.contrib.auth import views as auth_views

app_name = 'auth'

urlpatterns = [
    
    url(r'^inkognito/$', inkognito_pack),

    url(r'^login/$', login),
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', register),
    # url(r'^reset_password/$', password_reset, name='reset_password'),
    # url(r'^reset_password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset_password/complete/$', password_reset_complete, name='password_reset_complete'),
    # url(r'password_change/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html',success_url='/accounts/password_change_done')),
    # url(r'password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html')),
    # url(r'password_reset/$', auth_views.PasswordResetView.as_view(template_name='password_reset.html',email_template_name='password_reset_email.html',subject_template_name='password_reset_subject.txt',success_url='/accounts/password_reset_done/',from_email='support@yoursite.ma')),
    # url(r'password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html')),
    # url(r'password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',success_url='/accounts/password_reset_complete/')),
    # url(r'password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html')),
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    # url(r'^reset_password/complete/$', password_reset_complete, name='password_reset_complete'),
    url(r'^password_reset/$', auth_views.password_reset,{'email_template_name':'registration/password_reset_email.html',
                                                    'subject_template_name':'registration/password_reset_subject.txt',
                                                    'post_reset_redirect':'auth:password_reset_done',
                                                    'from_email':'accounts@django.com',
                                                    },name='password_reset'),
    # url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name': 'registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),

]
