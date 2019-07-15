from django.conf.urls import url
from django.views.generic import TemplateView

from .views import  BoxListView #, GeneratePDF

urlpatterns = [
    # url(r'^pdf/$', GeneratePDF.as_view()),
    # url(r'^box/$', TemplateView.as_view(template_name="box_ukr.html")),
    url(r'^box/$', BoxListView.as_view()),

    
]
