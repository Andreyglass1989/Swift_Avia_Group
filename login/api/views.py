from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,

)

from login.models import UserProfile, Reviews, CalculatorGroup
from LK.models import CustomerRecipients

from django.contrib.auth import get_user_model

from rest_framework.generics import (
    CreateAPIView, 
    UpdateAPIView, 
    RetrieveAPIView, 
    RetrieveUpdateAPIView, 
    DestroyAPIView, 
    ListAPIView
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer,
    UserDetalSerializer,
    UserProfileDetalSerializer,

    CustomerRecipientsListSerializer,
    CustomerRecipientsDetailSerializer,
    CustomerRecipientsCreateUpdateSerializer,

    ReviewsListSerializer,
    ReviewsCreateUpdateSerializer,

    CalculatorSerializer,
)


User = get_user_model()

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

class UserDetailAPIView(RetrieveAPIView):
    serializer_class = UserDetalSerializer
    #queryset = User.objects.all()
    lookup_field = 'username'

    def get_queryset(self, *args, **kwargs):
        queryset_list = User.objects.filter(username=self.kwargs['username'])
        return queryset_list


class UserProfileDetailAPIView(RetrieveAPIView):
    serializer_class = UserProfileDetalSerializer
    #queryset = User.objects.all()
    lookup_field = 'user_id'

    def get_queryset(self, *args, **kwargs):
        queryset_list = UserProfile.objects.filter(user_id=self.kwargs['user_id'])
        return queryset_list


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data #request.POST
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)






#------------------------------BEGIN CUSTOMER_RECIPIENTS----------------------------------------------
#------------------------------BEGIN List CUSTOMER_RECIPIENTS----------------------------------------------
class CustomerRecipientsListAPIView(ListAPIView):
    serializer_class = CustomerRecipientsListSerializer
    #pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = UserProfile.objects.get(user_id=self.request.user.id)
        queryset_list = CustomerRecipients.objects.filter(customer_id=user.code_clienta)

        # queryset_list = Pack.objects.filter(customer_id=user.code_clienta, pack_status=7,
        #                                     date_added__year='2017').order_by('-date_added')
        return queryset_list
# ------------------------------END List CUSTOMER_RECIPIENTS----------------------------------------

# ------------------------------BEGIN Detail CUSTOMER_RECIPIENTS-------------------------------------
class CustomerRecipientsDetailAPIView(RetrieveAPIView):
    serializer_class = CustomerRecipientsDetailSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        queryset_list = CustomerRecipients.objects.filter(cr_id=self.kwargs['pk'])
    #    user = UserProfile.objects.get(user_id=self.request.user.id)
     #   queryset_list = CustomerRecipients.objects.filter(customer_id=user.code_clienta)

        # queryset_list = Pack.objects.filter(customer_id=user.code_clienta, pack_status=7,
        #                                     date_added__year='2017').order_by('-date_added')
        return queryset_list
# ------------------------------END Detail CUSTOMER_RECIPIENTS----------------------------------------

        # ------------------------------BEGIN Create CUSTOMER_RECIPIENTS-------------------------------------
class CustomerRecipientsCreateAPIView(CreateAPIView):
    queryset = CustomerRecipients.objects.all()
    serializer_class = CustomerRecipientsCreateUpdateSerializer
    permission_classes = [IsAuthenticated]


    def initial(self, *args, **kwargs):
        initial = super(CustomerRecipientsCreateAPIView, self).initial(*args, **kwargs)
       # username = self.request.user
       # user = UserProfile.objects.get(user_id=username.id)
        self.initial = {#'customer': user.code_clienta,
                        'country': 220,
                        'room': 1,
                        }
        return self.initial

    def perform_create(self, serializer):
        username = self.request.user
        user = UserProfile.objects.get(user_id=username.id)
        code = user.code_clienta
        serializer.save(customer=code)  # , title="my title")

    # def get_queryset(self, *args, **kwargs):
    #     queryset_list = CustomerRecipients.objects.filter(cr_id=self.kwargs['pk'])
    #     #    user = UserProfile.objects.get(user_id=self.request.user.id)
    #     #   queryset_list = CustomerRecipients.objects.filter(customer_id=user.code_clienta)
    #
    #     # queryset_list = Pack.objects.filter(customer_id=user.code_clienta, pack_status=7,
    #     #                                     date_added__year='2017').order_by('-date_added')
    #     return queryset_list
# ------------------------------END Create CUSTOMER_RECIPIENTS-------------------------------------


class CustomerRecipientsUpdateAPIView(UpdateAPIView):
    queryset = CustomerRecipients.objects.all()
    serializer_class = CustomerRecipientsCreateUpdateSerializer
    lookup_field = 'cr_id'
    permission_classes = [IsAuthenticated]
    # lookup_url_kwarg = "abc"



class CustomerRecipientsDeleteAPIView(DestroyAPIView):
    queryset = CustomerRecipients.objects.all()
    serializer_class = CustomerRecipientsDetailSerializer
    lookup_field = 'cr_id'
    # lookup_url_kwarg = "abc"

#------------------------------END CUSTOMER_RECIPIENTS------------------------------------------------


#------------------------------BEGIN Reviews----------------------------------------------
# ------------------------------BEGIN List Reviews----------------------------------------------
class ReviewsListAPIView(ListAPIView):
    serializer_class = ReviewsListSerializer
    # pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = UserProfile.objects.get(user_id=self.request.user.id)
        queryset_list = Reviews.objects.filter(reviews_client=user.code_clienta).order_by('-date_add')
        return queryset_list
# ------------------------------END List Reviews---------------------------------------

        # ------------------------------BEGIN Create CUSTOMER_RECIPIENTS-------------------------------------
class ReviewsCreateAPIView(CreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    # def initial(self, *args, **kwargs):
    #     initial = super(ReviewsCreateAPIView, self).initial(*args, **kwargs)
    #     self.initial = { 'recomend': True, }
    #     return self.initial

    def perform_create(self, serializer):
        username = self.request.user
        user = UserProfile.objects.get(user_id=username.id)
        code = user.code_clienta
        serializer.save(reviews_client=code)  # , title="my title")

# ------------------------------END Create CUSTOMER_RECIPIENTS-------------------------------------


class ReviewsUpdateAPIView(UpdateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsCreateUpdateSerializer
    lookup_field = 'id'



class ReviewsDeleteAPIView(DestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsCreateUpdateSerializer
    lookup_field = 'id'


#------------------------------END Reviews----------------------------------------------


class CalculatorListAPIView(ListAPIView):
    serializer_class = CalculatorSerializer
    queryset = CalculatorGroup.objects.all()
    permission_classes = [AllowAny]