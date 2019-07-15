"""swift_avia_group URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from LK.views import (
    index, 
    about_us, 
    contacts, 
    search_link,
    if_delivery, 
    all_cargo, 
    service,
    partner
)
from rest_framework_jwt.views import obtain_jwt_token
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^MDBootstrap/$', TemplateView.as_view(template_name='MDBootstrap.html'), name=''),

    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('login.urls', namespace='auth')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', index),
    url(r'^about/$', about_us, name='about_us'),
    url(r'^service/$', service, name='service'),
    url(r'^contacts/$', contacts, name='contacts'),
    url(r'^partner/$', partner, name='partner'),
    url(r'^if/$', if_delivery, name='if_delivery'),
#
    url(r'^all_cargo/$', all_cargo, name='all_cargo'),
    url(r'^search-link/$', search_link),
    url(r'^parcel-ua/$', TemplateView.as_view(template_name='WarehouseUA.html')),
#
    url(r'^LK/', include('LK.urls', namespace='LK')),
    url(r'^api/auth/token', obtain_jwt_token),
    url(r'^api/users/', include('login.api.urls', namespace='users-api')),
    url(r'^api/LK/', include('LK.api.urls', namespace='LK-api')),
    url(r'^Izrael/', include('Izrael.urls', namespace='Izrael')),
    url(r'^ManagerAdmin/', include('ManagerAdmin.urls', namespace='ManagerAdmin')),

    url(r'^sitemaps\.xml$', TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml')),
    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots_file"),

]
