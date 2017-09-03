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
from LK.views import index, about_us, contacts, if_delivery, all_cargo

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('login.urls')),
    url(r'^$', index),
    url(r'^about/$', about_us, name='about_us'),
    url(r'^contacts/$', contacts, name='contacts'),
    url(r'^if/$', if_delivery, name='if_delivery'),
    url(r'^all_cargo/$', all_cargo, name='all_cargo'),
    url(r'^LK/', include('LK.urls')),
]
