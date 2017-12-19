from django.conf.urls import url, include
from LK.api.views import (
    PackList_vputi_APIView,
    PackProductListAPIView,
    PackList_consolidation_APIView,
    PackList_NaSklade_APIView,
    PackList_Dostavlen_APIView,
    PackDetailAPIView,
    SearchPackAPIView,
    SearchParcelAPIView,
    )

urlpatterns = [

    url(r'^dostavlen/$', PackList_Dostavlen_APIView.as_view(), name='dostavlen'),
    url(r'^v_puti/$', PackList_vputi_APIView.as_view(), name='v_puti'),
    url(r'^consolidation/$', PackList_consolidation_APIView.as_view(), name='consolidation'),
    url(r'^na_sklade/$', PackList_NaSklade_APIView.as_view(), name='na_sklade'),

    url(r'^(?P<pack_number>\d+)/$', PackDetailAPIView.as_view(), name='pack_detail'),
    url(r'^pack_product/(?P<pack_id>\d+)/$', PackProductListAPIView.as_view(), name='packproduct_detail'),
    url(r'^search/(?P<pack_number>\d+)/$', SearchPackAPIView.as_view(), name='search_pack'),
    url(r'^search_parcel/(?P<parcel_number>\d+)/$', SearchParcelAPIView.as_view(), name='search_parcel'),
]
