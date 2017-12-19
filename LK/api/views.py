from rest_framework.generics import ListAPIView, RetrieveAPIView

from django.contrib import auth
from django.contrib.auth.models import User
from LK.models import Pack, PackProduct, Parcel
from login.models import UserProfile
from LK.api.serializers import (
    PackListSerializer, 
    PackProductSerializer, 
    PackDetailSerializer,
    SearchPackSerializer,
    SearchPaprcelSerializer,
)

from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)
from .pagination import PackLimitOffsetPagination, PackPageNumberPagination

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

class PackProductListAPIView(ListAPIView):
    #queryset = PackProduct.objects.filter(pack_id=7751)
    serializer_class = PackProductSerializer
    lookup_field = 'pack_id'

    def get_queryset(self, *args, **kwargs):
        # print(self.kwargs)
        # print(args)
        queryset_list = PackProduct.objects.filter(pack_id=self.kwargs['pack_id'])
        # print(self.request.data)
        return queryset_list

class PackDetailAPIView(RetrieveAPIView):
    #queryset = Pack.objects.all()
    serializer_class = PackDetailSerializer
    lookup_field = 'pack_number'
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
       # print(self.kwargs)
        queryset_list = Pack.objects.filter(pack_number=self.kwargs['pack_number'])
      #  print(queryset_list)
        return queryset_list



class PackList_Dostavlen_APIView(ListAPIView):
    serializer_class = PackListSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = UserProfile.objects.get(user_id=self.request.user.id)
        queryset_list = Pack.objects.filter(customer_id=user.code_clienta, pack_status=7, date_added__year='2017').order_by('-date_added')
        return queryset_list




class PackList_vputi_APIView(ListAPIView):
    serializer_class = PackListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = UserProfile.objects.get(user_id=self.request.user.id)
        queryset_list = Pack.objects.filter(customer_id=user.code_clienta, pack_status=5).order_by('-date_added')
        return queryset_list




class PackList_consolidation_APIView(ListAPIView):
    serializer_class = PackListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = UserProfile.objects.get(user_id=self.request.user.id)
        queryset_list = Pack.objects.filter(customer_id=user.code_clienta, pack_status=2).order_by('-date_added')
        return queryset_list



class PackList_NaSklade_APIView(ListAPIView):
    serializer_class = PackListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = UserProfile.objects.get(user_id=self.request.user.id)
        queryset_list = Pack.objects.filter(customer_id=user.code_clienta, pack_status=1).order_by('-date_added')
        return queryset_list



class SearchPackAPIView(ListAPIView):
    serializer_class = SearchPackSerializer
    lookup_field = 'pack_number'
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        pack = Pack.objects.all()
        pack_number = self.kwargs['pack_number']
        queryset_list = None
        if pack_number:
            queryset_list = pack.filter(pack_number__icontains=pack_number)
        return queryset_list        



class SearchParcelAPIView(ListAPIView):
    serializer_class = SearchPaprcelSerializer
    lookup_field = 'parcel_number'
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        parcel = Parcel.objects.all()
        parcel_number = self.kwargs['parcel_number']
        queryset_list = None
        if parcel_number:
            queryset_list = parcel.filter(parcel_number__icontains=parcel_number)
        return queryset_list