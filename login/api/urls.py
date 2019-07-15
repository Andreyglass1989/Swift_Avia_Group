from django.conf.urls import url
from django.contrib import admin

from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
    UserDetailAPIView,
    UserProfileDetailAPIView,

    CustomerRecipientsListAPIView,
    CustomerRecipientsDetailAPIView,
    CustomerRecipientsCreateAPIView,
    CustomerRecipientsUpdateAPIView,
    CustomerRecipientsDeleteAPIView,

    ReviewsListAPIView,
    ReviewsCreateAPIView,
    ReviewsUpdateAPIView,
    ReviewsDeleteAPIView,

    CalculatorListAPIView,
    BuyoutAPIView,
    AirDataUploadFrom1CAPIView,
    AirDataUploadFrom1CUpdateAPIView
    )

urlpatterns = [

    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^detail/(?P<username>[\w-]+)/$', UserDetailAPIView.as_view(), name='about_user'),
    url(r'^profile_detail/(?P<user_id>\d+)/$', UserProfileDetailAPIView.as_view(), name='profile_user'),


    url(r'^recipients_list/$', CustomerRecipientsListAPIView.as_view(), name='recipients_list'),
    url(r'^recipient/detail/(?P<pk>\d+)/$', CustomerRecipientsDetailAPIView.as_view(), name='recipient-detail'),
    url(r'^recipient/create/$', CustomerRecipientsCreateAPIView.as_view(), name='recipients-create'),
    url(r'^recipient/edit/(?P<cr_id>\d+)/$', CustomerRecipientsUpdateAPIView.as_view(), name='recipients-edit'),
    url(r'^recipient/delete/(?P<cr_id>\d+)/$', CustomerRecipientsDeleteAPIView.as_view(), name='recipients-delete'),

    url(r'^reviews_list/$', ReviewsListAPIView.as_view(), name='reviews_list'),
    url(r'^reviews/create/$', ReviewsCreateAPIView.as_view(), name='reviews-create'),
    url(r'^reviews/edit/(?P<id>\d+)/$', ReviewsUpdateAPIView.as_view(), name='reviews-edit'),
    url(r'^reviews/delete/(?P<id>\d+)/$', ReviewsDeleteAPIView.as_view(), name='reviews-delete'),

    url(r'^calculator/$', CalculatorListAPIView.as_view(), name='calculator '),
    url(r'^list_buyout/$', BuyoutAPIView.as_view({'get': 'list'}), name='list_buyout'),
    url(r'^create_buyout/$', BuyoutAPIView.as_view({'post': 'create'}), name='create_buyout'),

    url(r'^list_data_1C/$', AirDataUploadFrom1CAPIView.as_view(), name='list_data_1c'),
    url(r'^list_data_1C/edit/(?P<id>\d+)/$', AirDataUploadFrom1CUpdateAPIView.as_view(), name='data-1C-edit'),

]
