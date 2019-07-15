from django.conf.urls import url, include
from LK.api.views import (
    PackList_vputi_APIView,
    PackProductListAPIView,
    PackList_All_APIView,
    PackList_consolidation_APIView,
    PackList_NaSklade_APIView,
    PackList_Dostavlen_APIView,
    PackDetailAPIView,
    SearchPackAPIView,
    SearchParcelAPIView,
    AirParcelAPIView,
    ParcelHistoryAPIView,
    PackProductAPIView,
    ParcelPackProductAPIView,
    AddressAPIView,
    SearchPlombaAPIView,
    ParcelUaDataCreateAPIView,
    AirListFlyView,
    GetParcelUaDataApiView,
    ClientPackAPIView,
    PackCreateView,
    CustomerListView,
    InkognitoCustomerListView,
    warehouse_ua_view,
    get_data_1C,
    MobileAppPackCreateAPIView,
    PackToMobileSlavaListView,
    CreatePlombaDimensionAPIView,
    PlombaDimensionUpdateAPIView,
    pack_today_Slava,
    parcel_consolidation_data_plomb,
    )
# from rest_framework.documentation import include_docs_urls

urlpatterns = [

    url(r'^dostavlen/$', PackList_Dostavlen_APIView.as_view(), name='dostavlen'),
    url(r'^v_puti/$', PackList_vputi_APIView.as_view(), name='v_puti'),
    url(r'^consolidation/$', PackList_consolidation_APIView.as_view(), name='consolidation'),
    url(r'^na_sklade/$', PackList_NaSklade_APIView.as_view(), name='na_sklade'),
    url(r'^all/$', PackList_All_APIView.as_view(), name='all_pack'),

    url(r'^(?P<pack_number>\d+)/$', PackDetailAPIView.as_view(), name='pack_detail'),
    url(r'^pack_product/(?P<pack_id>\d+)/$', PackProductListAPIView.as_view(), name='packproduct_detail'),
    url(r'^search/(?P<pack_number>\d+)/$', SearchPackAPIView.as_view(), name='search_pack'),
   
    #-- 26.01.19 --- for mobile app Ukraine warehouse
    url(r'^search_parcel/(?P<parcel_number>\d+)/$', SearchParcelAPIView.as_view(), name='search_parcel'),
    url(r'^search_plomba/(?P<plomba_id>\d+)/$', SearchPlombaAPIView.as_view()),
    url(r'^create_parceluadata/$', ParcelUaDataCreateAPIView.as_view()),
    url(r'^search_client/(?P<parcel_number>\d+)/$', ClientPackAPIView.as_view()),
    # url(r'^search_client2/$', hello_world),
    url(r'^get_parcel_ua/(?P<air_id>\d+)/$', GetParcelUaDataApiView.as_view()),

    #----------------------------------- for WEB Ukraine warehouse
    url(r'^warehouse_ua/(?P<parcel_number>\d+)/$', warehouse_ua_view),
    url(r'^Slava_pack_today/(?P<date>[\w\-]+)/$', pack_today_Slava),

# clientAPI
    #-- 13.03.18 ---
    url(r'^parcel/(?P<parcel_id>\d+)/$', AirParcelAPIView.as_view(), name='search_air'),
    url(r'^parcel_number/(?P<parcel_external_id>\d+)/$', AirParcelAPIView.as_view()),
    url(r'^parcel_history/(?P<parcel_id>\d+)/$', ParcelHistoryAPIView.as_view(), name='about_air'),
    url(r'^air_fly/$', AirListFlyView.as_view()),
    
    #-- 8.02.19 -- for mobile app China warehouse
    url(r'^createPack/$', PackCreateView.as_view()),
    url(r'^get_customers/$', CustomerListView.as_view()),
    url(r'^client_inkognito/(?P<comment>\d{1,3}/\d{1,3})/$', InkognitoCustomerListView.as_view()),

    #-- 12.06.18 ---
    url(r'^parcel_pack_product/(?P<parcel_id>\d+)/$', ParcelPackProductAPIView.as_view(), name='parcel_pack_product'),
    url(r'^packproduct/(?P<pack_product_id>\d+)/$', PackProductAPIView.as_view(), name='search_pack_product'),
    url(r'^address/(?P<address_id>\d+)/$', AddressAPIView.as_view(), name='get_address'),

    url(r'^get_1C/$', get_data_1C, name='get_1C_data'),
    url(r'^mobileAppCreatePack/$', MobileAppPackCreateAPIView.as_view(), name='create-mobile-app'),
    url(r'^packDateAdded/(?P<date>[\w\-]+)/$', PackToMobileSlavaListView.as_view(), name="packDateAdded"),
    # url(r'^docs/', include_docs_urls(title='SwiftAviaGroup APIs')),

    url(r'^create-plomba-dimension/$', CreatePlombaDimensionAPIView.as_view()),
    url(r'^update-plomba-dimension/(?P<plomba_id>\d+)/$', PlombaDimensionUpdateAPIView.as_view()),
    url(r'^parcel-consolidation/$', parcel_consolidation_data_plomb),
]
