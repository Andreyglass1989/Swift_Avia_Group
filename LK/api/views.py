from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser, JSONParser
from rest_framework import status

from django.contrib import auth
from django.contrib.auth.models import User
from LK.models import (
    Pack, 
    PackProduct, 
    Parcel, 
    AirParcel, 
    Address, 
    ParcelHistory, 
    ParcelPackProduct, 
    PlombaDimension,
    ParcelUaData,
    ParcelUa,
    Air,
    Customer,
    PartnerInc0Sandbox,
    Currency,
    CategoryGroup,
    Sklad,
    PackStatus,
    Language,
)

from login.models import UserProfile, AirDataUploadFrom1C
from LK.api.serializers import (
    PackListSerializer, 
    PackProductSerializer, 
    PackDetailSerializer,
    SearchPackSerializer,
    SearchPaprcelSerializer,
    AirParcelSerializer,
    ParcelHistorySerializer,
    PackProductSerializer,
    ParcelPackProductSerializer,
    AddressSerializer,
    PlombaDimensionSerializer,
    ParcelUaDataCreateSerializer,
    AirSerializer,
    PackClientSerializer,
    ParcelUaSerializer,
    PackCreateSerializer,
    CustomerSerializer,
    PartnerInc0SandboxCreateSerializer,
    MobileAppPackSerializer,
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

from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist




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


class PackList_All_APIView(ListAPIView):
    serializer_class = PackListSerializer
    pagination_class = LimitOffsetPagination#PageNumberPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = UserProfile.objects.get(user_id=self.request.user.id)
        queryset_list = Pack.objects.filter(customer_id=user.code_clienta, date_added__year='2017').order_by('-date_added')
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


from rest_framework import status
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


class SearchPlombaAPIView(RetrieveAPIView):
    serializer_class = PlombaDimensionSerializer
    lookup_field = 'plomba_id'
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        plomba = PlombaDimension.objects.all()
        plombaId = self.kwargs['plomba_id']
        queryset_list = None
        if plombaId:
            queryset_list = plomba.filter(plomba_id = plombaId)
        return queryset_list



class ClientPackAPIView(APIView):
    lookup_field = 'parcel_number'
    permission_classes = [AllowAny]

    def get(self, *args, **kwargs):
        num_parcel = self.kwargs['parcel_number']
        if num_parcel:
            q = Parcel.objects.filter(parcel_number = num_parcel).first()
            # one or more client if delete .first()
            p = ParcelPackProduct.objects.filter(parcel_id=q.parcel_id).first()
            #
            data = Pack.objects.filter(pack_id=p.pack_id)
        serializer = PackListSerializer(data, many=True)
        return Response(serializer.data)


# @api_view()
# def hello_world(request):
#     return Response({"message": "Hello, world!"})




class GetParcelUaDataApiView(RetrieveAPIView):
    serializer_class = ParcelUaSerializer
    lookup_field = 'air_id'
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        airUAid = self.kwargs['air_id']
        if airUAid:
            queryset_list = ParcelUa.objects.filter(air_id = airUAid)
        return queryset_list



class AirParcelAPIView(ListAPIView):
    serializer_class = AirParcelSerializer
    lookup_field = 'parcel_id'
    permission_classes = [AllowAny]

    def get_queryset(self):
        air_id_number = self.kwargs['parcel_id']
        if air_id_number:
            queryset_list = AirParcel.objects.filter(parcel_id=air_id_number)
        return queryset_list



class ParcelHistoryAPIView(ListAPIView):
    serializer_class = ParcelHistorySerializer
    lookup_field = 'parcel_id'
    permission_classes = [AllowAny]

    def get_queryset(self):
        air_id_number = self.kwargs['parcel_id']
        if air_id_number:
            queryset_list = ParcelHistory.objects.filter(parcel_id=air_id_number).order_by('-date_added')
        return queryset_list



#--- 12.06.18 ----------------------------------

class ParcelPackProductAPIView(ListAPIView):
    serializer_class = ParcelPackProductSerializer
    lookup_field = 'parcel_id'
    permission_classes = [AllowAny]

    def get_queryset(self):
        parcel_pack_product = self.kwargs['parcel_id']
        if parcel_pack_product:
            queryset_list = ParcelPackProduct.objects.filter(parcel_id=parcel_pack_product)
        return queryset_list



class PackProductAPIView(ListAPIView):
    serializer_class = PackProductSerializer
    lookup_field = 'pack_product_id'
    permission_classes = [AllowAny]

    def get_queryset(self):
        pack_product = self.kwargs['pack_product_id']
        if pack_product:
            queryset_list = PackProduct.objects.filter(pack_product_id=pack_product)
        return queryset_list



class AddressAPIView(ListAPIView):
    serializer_class = AddressSerializer
    lookup_field = 'address_id'
    permission_classes = [AllowAny]

    def get_queryset(self):
        address = self.kwargs['address_id']
        if address:
            queryset_list = Address.objects.filter(address_id=address)
        return queryset_list


#26.01.19 ----------

class ParcelUaDataCreateAPIView(CreateAPIView):
    queryset = ParcelUaData.objects.all()
    serializer_class = ParcelUaDataCreateSerializer
    permission_classes = [AllowAny]


class AirListFlyView(ListAPIView):
    serializer_class = AirSerializer
    permission_classes =[AllowAny]

    def get_queryset(self):
        queryset_list = Air.objects.exclude(air_status_id=6).exclude(
                        date_added__year="2018").exclude(date_added__year="2017").exclude(
                        date_added__year="2016").exclude(date_added__year="2015")
        return queryset_list


class PackCreateView(CreateAPIView):
    queryset = Pack.objects.all()
    serializer_class = PackCreateSerializer
    permissions_classes = [AllowAny]

    def perform_create(self, serializer):
        last_partner = PartnerInc0Sandbox.objects.all().last()
        last_partner = int(last_partner.number)+1
        PartnerInc0Sandbox.objects.create(number=last_partner)

        serializer.save(
            pack_status = PackStatus.objects.get(pack_status_id=1), 
            external_id = "",
            total= 1,
            currency_code = "USD",
            currency_value= 1.0,
            sandbox= 0,
            def_field = 0,
            packlist = 0,
            sklad = Sklad.objects.get(sklad_id=1),
            language = Language.objects.get(language_id=2),
            currency = Currency.objects.get(currency_id=2),
            category_group = CategoryGroup.objects.get(category_group_id = 3),
            pack_number = str(last_partner),
            )


class CustomerListView(ListAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset_list = Customer.objects.filter(typ=1).order_by("-date_added")
        return queryset_list


class InkognitoCustomerListView(ListAPIView):
    serializer_class = PackListSerializer
    lookup_field = 'comment'
    permission_classes = [AllowAny]

    def get_queryset(self):
        search_query = self.kwargs['comment']
        if search_query:
            queryset_list = Pack.objects.filter(comment__icontains=str(search_query))
        return queryset_list
        # queryset_list = Pack.objects.filter(typ=1).order_by("-date_added")
        # return queryset_list

# @api_view()
# def get_next_partner(request):
#     partner = PartnerInc0Sandbox.objects.all().last()
#     last_partner = str(int(partner.number)+1)
#     return Response({"number": last_partner})



# def warehouse_ua_view(request, parcel_number):
#     parcel = Parcel.objects.get(parcel_number = parcel_number)
#     # search air and parcel_ua_id
#     air = AirParcel.objects.get(parcel_id = parcel.parcel_id)
#     parcel_ua = ParcelUa.objects.get(air_id=air.air_id)
#     #
#     plomba = PlombaDimension.objects.get(plomba_id=parcel.external_id)
#     p = ParcelPackProduct.objects.filter(parcel_id=parcel.parcel_id).first()
#     d = Pack.objects.get(pack_id=p.pack_id)

#     data= {
#         "height": plomba.plomba_height,
#         "weight": plomba.plomba_weight,
#         "width": plomba.plomba_width,
#         "length": plomba.plomba_length,
#         "customer": str(d.customer),
#         "plomba": plomba.plomba_id,
#         "parcel_ua_id": parcel_ua.parcel_ua_id
#     }
#     return JsonResponse(data) 



def warehouse_ua_view(request, parcel_number):
    parcel = Parcel.objects.get(parcel_number = parcel_number)
    # search air and parcel_ua_id
    air = AirParcel.objects.get(parcel_id = parcel.parcel_id)
    parcel_ua = ParcelUa.objects.get(air_id=air.air_id)
    #
    plomba = PlombaDimension.objects.get(plomba_id=parcel.external_id)
    parcel1 = Parcel.objects.filter(external_id = parcel.external_id)
    lll=[]

    if len(parcel1)>1:
        for ppp in parcel1:
            l = ParcelPackProduct.objects.filter(parcel_id=ppp.parcel_id).first()
            l1 = Pack.objects.get(pack_id=l.pack_id) 
            if str(l1.customer) not in lll:
                lll.append(str(l1.customer))
    elif len(parcel1)==1:
        plomba = PlombaDimension.objects.get(plomba_id=parcel.external_id)
        p = ParcelPackProduct.objects.filter(parcel_id=parcel.parcel_id).first()
        d = Pack.objects.get(pack_id=p.pack_id)
        lll.append(str(d.customer))

    data= {
        "height": plomba.plomba_height,
        "weight": plomba.plomba_weight,
        "width": plomba.plomba_width,
        "length": plomba.plomba_length,
        "customer": ' '.join(lll),
        "plomba": plomba.plomba_id,
        "parcel_ua_id": parcel_ua.parcel_ua_id
    }
    return JsonResponse(data)




def pack_today_Slava(request, date):
    q = Parcel.objects.filter(date_added__contains = date)
    pack_today=[]
    full_data = []
    for n in q:
        p = ParcelPackProduct.objects.filter(parcel_id=n.parcel_id).first()
        if p.pack_id not in pack_today:
            pack_today.append(p.pack_id)

    for p in pack_today:
        data = Pack.objects.get(pack_id=p)
        parcel_number=[]
        dict_00 = {"date": data.date_added.strftime("%Y-%m-%d"),
                   "weight": data.weight,
                   "customer": data.customer.external_id,
                   "comment": data.comment,
                   # "group": data.category_group.category_group_id, 
        }
        parcel = Parcel.objects.filter(parcelpackproduct__pack_id=data.pack_id).order_by('parcel_id')
        for z in parcel:
            if z.external_id not in parcel_number:
                parcel_number.append(z.external_id)
                # print(z.external_id)
        dict_00['parcel'] = parcel_number
        full_data.append(dict_00)
    return JsonResponse(full_data, safe=False)









def get_data_1C(request):
    list0 = AirDataUploadFrom1C.objects.filter(air=324)
    data = {"results": list(list0.values("customer", "packing_1C", "manager", "weight", "volume", 
                                         "cost", "transaction_amount", "insurance", "china_expenses", 
                                         "packing_amount", "additional_expense", "subtotal", "one_percent_for_UAH",
                                         "total"))}
    return JsonResponse(data)




class MobileAppPackCreateAPIView(CreateAPIView):
    queryset = Pack.objects.all()
    serializer_class = MobileAppPackSerializer
    permission_classes = [AllowAny]
    parser_class = (FileUploadParser, MultiPartParser)

    def perform_create(self, serializer):
        last_partner = PartnerInc0Sandbox.objects.all().last()
        last_partner = int(last_partner.number)+1
        PartnerInc0Sandbox.objects.create(number=last_partner)

        serializer.save(
            pack_status = PackStatus.objects.get(pack_status_id=1), 
            external_id = "",
            total= 1,
            currency_code = "USD",
            currency_value= 1.0,
            sandbox= 0,
            def_field = 0,
            packlist = 0,
            sklad = Sklad.objects.get(sklad_id=1),
            language = Language.objects.get(language_id=2),
            currency = Currency.objects.get(currency_id=2),
            category_group = CategoryGroup.objects.get(category_group_id = 3),
            pack_number = str(last_partner),
            )

    # def post(self, request, *args, **kwargs):
    #     # file_serializer = FileSerializer(data=request.data)
    #     # print(dir(request))
    #     print(request.data)
    #     print(request.FILES)
    #     serializer = MobileAppPackSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         # return Response(data=request.DATA)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PackToMobileSlavaListView(ListAPIView):
    serializer_class = PackListSerializer
    # lookup_field = 'date_added'
    permission_classes = [AllowAny]

    def get_queryset(self):
        query = self.kwargs['date']
        print(query)
        if query:
            queryset_list = Pack.objects.filter(date_added__icontains=query).order_by("date_added")
        return queryset_list




# def packDateAdded(request, date):
#     print(date)
#     pack = Pack.objects.filter(date_added__icontains=date)

#     data = {"results": list(pack.values)}

#     # data= {
#     #     "pack": list(pack),
#     # }
#     return JsonResponse(data)



class CreatePlombaDimensionAPIView(CreateAPIView):
    serializer_class = PlombaDimensionSerializer
    permission_classes = [AllowAny]
    queryset = PlombaDimension.objects.all()

class PlombaDimensionUpdateAPIView(UpdateAPIView):
    queryset = PlombaDimension.objects.all()
    serializer_class = PlombaDimensionSerializer
    lookup_field = 'plomba_id'


def parcel_consolidation_data_plomb(request):
    parcel = Parcel.objects.filter(parcel_status_id=2, sklad_id=1)
    list_exist=[]
    # list_none = []
    plomb_data = []
    data_dict = {}
    for p in parcel:
        try:
            plomb=PlombaDimension.objects.get(plomba_id=p.external_id)
            data_dict = {
                "plomba": str(plomb.plomba_id),
                "weight": round(float(plomb.plomba_weight),2),
                "width": plomb.plomba_width,
                "height": plomb.plomba_height,
                "length": plomb.plomba_length,
            }
            if p.external_id not in plomb_data:
                plomb_data.append(p.external_id)
                list_exist.append(data_dict)
        except ObjectDoesNotExist:
            pass
            # if p.external_id not in list_none:
            #     list_none.append(p.external_id)


    data = {
        "list_exist": list_exist,
        # "list_none": list_none,
    }
    return JsonResponse(data)