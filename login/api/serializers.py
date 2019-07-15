# -*- coding: utf-8 -*-
from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    ValidationError,
)
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from login.models import UserProfile, Reviews, CalculatorGroup, Buyout, AirDataUploadFrom1C
from LK.models import CustomerRecipients

User = get_user_model()



class ReviewsListSerializer(ModelSerializer):

    class Meta:
        model = Reviews
        fields = [
            'id',
            'text_reviews',
            'reviews_client',
            'date_add',
            'recomend',
        ]


class ReviewsCreateUpdateSerializer(ModelSerializer):

    class Meta:
        model = Reviews
        fields = [
            'recomend',
            'text_reviews',
            'date_add',
        ]


class CustomerRecipientsListSerializer(ModelSerializer):

    class Meta:
        model = CustomerRecipients
        fields = [
            'cr_id',
            'lastname',
            'name',
            'city',
            'street',
        ]



class CustomerRecipientsDetailSerializer(ModelSerializer):
    customer = SerializerMethodField()
    country = SerializerMethodField()
    date_fix =SerializerMethodField()

    class Meta:
        model = CustomerRecipients
        fields = [
            'cr_id',
            'customer',
            'country',
            'name',
            'lastname',
            'city',
            'street',
            'home',
            'room',
            'phone',
            #'pos_item',
            'date_fix',
        ]

    def get_country(self, obj):
        return obj.country.name

    def get_customer(self, obj):
        return obj.customer.external_id

    def get_date_fix(self, obj):
        return obj.date_fix.strftime("%d.%m.%Y %H:%M:%S")

# --------------------------END Detail CustomerRecipients---------------------------------------------

#--------------------------BEGIN CreateUpdate CustomerRecipients---------------------------------------------


class CustomerRecipientsCreateUpdateSerializer(ModelSerializer):

    class Meta:
        model = CustomerRecipients
        fields = [
        #    'customer',
        #    'country',
            'name',
            'lastname',
            'city',
            'street',
            'home',
            'room',
            'phone',
            'date_fix',
        ]



class UserDetalSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'full_name',
        ]

class UserProfileDetalSerializer(ModelSerializer):
    code_clienta = SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = [
            'user_id',
            'phone',
            'skype',
            'code_clienta',
            'stavka',
        ]

    def get_code_clienta(self, obj):
        return obj.code_clienta.external_id

        

class UserCreateSerializer(ModelSerializer):
    password2 = CharField(label='Пароль для подтверждения')
    #username = CharField(label='Логин')
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            #'password2',

        ]
        extra_kwargs = {"password":
                            {"write_only":True}
                       }

    def validate(self, data):
        email = data['email']
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("Такой логин зарегестрирован.")
        return data

    def password2(self, value):
        data = self.get_initial()
        password1 = data.get("password")
        password2 = value
        if password1 != password2:
            raise ValidationError("Пароли должны совпадать")
        return value


    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email,
            password=password,
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True, label='Логин')
   # email = EmailField(label='Почта')
    class Meta:
        model = User
        fields = [
            'username',
       #     'email',
            'password',
            'token',
        ]
        extra_kwargs = {"password":
                            {"write_only":True}
                        }

    def validate(self, data):
        user_obj = None
       # email = data.get("email", None)
        username = data.get("username", None)
        password = data["password"]
        if not username:  # or not email and 
            raise ValidationError("Логин обязателен для входа в аккаунт.")#Login and email is required for login in account"")
        user = User.objects.filter(
            #Q(email=email) |
            Q(username=username)
        ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        # print(user)
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            # raise ValidationError("Пользователь с таким логином не найден.")#This Login/email not corrcet
            raise ValidationError("User not found")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Неверный пароль, пожалуйста повторите еще.")#"Password is not true, please repeate again")

        data["token"] = "SOME RANDOM TOKEN"
        return data


class CalculatorSerializer(ModelSerializer):
    #name = SerializerMethodField()

    class Meta:
        model = CalculatorGroup
        fields = [
            'name',
            'price',
        ]

    # def get_pack_status(self, obj):
    #     return obj.pack_status.name


class BuyoutSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(BuyoutSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Buyout
        fields = '__all__'



class AirDataUploadFrom1CSerializer(ModelSerializer):
    # customer = SerializerMethodField()

    class Meta:
        model = AirDataUploadFrom1C
        fields = '__all__'

    # def get_customer(self, obj):
    #     return obj.customer.external_id