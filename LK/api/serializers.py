from rest_framework.serializers import ModelSerializer, SerializerMethodField
# from login.models import UserProfile
# from django.contrib import auth
# from django.contrib.auth.models import User
from login.api.serializers import UserDetalSerializer
from LK.models import (
    Pack, 
    PackProduct, 
    Parcel, 
    AirParcel, 
    ParcelHistory, 
    ParcelPackProduct,
    Address,
    PlombaDimension,
    ParcelUaData,
    ParcelUa,
    Air,
    Customer,
    PartnerInc0Sandbox,
    )
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers


class PackListSerializer(ModelSerializer):
    customer = SerializerMethodField()
    pack_status = SerializerMethodField()
    date_added =SerializerMethodField()

    class Meta:
        model = Pack
        # fields = '__all__'
        fields = [
            'pack_id',
            'pack_number',
            'customer',
            'pack_status',
            'date_added',
            'weight',
            'comment',
            'point',
            #'date0',
        ]

    def get_pack_status(self, obj):
        return obj.pack_status.name

    def get_customer(self, obj):
        try:
            return obj.customer.external_id
        except ObjectDoesNotExist:
            return None

    def get_date_added(self, obj):
        return obj.date_added.strftime("%d.%m.%Y")


class PackProductSerializer(ModelSerializer):
    class Meta:
        model = PackProduct
        fields = [
            'name',
            'price',
            'quantity',
            'pack',
        ]


class PackProductChildSerializer(ModelSerializer):
    user = UserDetalSerializer(read_only=True)
    class Meta:
        model = PackProduct
        fields = [
            'name',
            'price',
            'quantity',
        ]


class PackProductDetailSerializer(ModelSerializer):
    user = UserDetalSerializer(read_only=True)

   # replies = SerializerMethodField()
    class Meta:
        model = PackProduct
        fields = [
            'name',
            'price',
            'quantity',
            'pack',
            #'replies',
        ]

    # def get_replies(self):
    #     if obj.is_pack:
    #         print(obj)
    #         return PackProductChildSerializer(obj.children(), many=True).data
    #     return None



class PackDetailSerializer(ModelSerializer):
    #user = UserDetalSerializer(read_only=True)

   # replies = SerializerMethodField()
    class Meta:
        model = Pack
        fields = [
            'pack_number',
            'customer',
            'pack_status',
            'date_added',
            'weight',
            #'replies',
        ]


class SearchPackSerializer(ModelSerializer):
    pack_status = SerializerMethodField()
    date_added = SerializerMethodField()

    class Meta:
        model = Pack
        fields = [
            'pack_number',
            'pack_status',
            'date_added',
            'weight',
        ]

    def get_pack_status(self, obj):
        return obj.pack_status.name

    def get_date_added(self, obj):
        return obj.date_added.strftime("%d.%m.%Y")



class SearchPaprcelSerializer(ModelSerializer):
    parcel_status = SerializerMethodField()
    date_added = SerializerMethodField()

    class Meta:
        model = Parcel
        fields = [
            'parcel_id',
            'parcel_number',
            'parcel_status',
            'date_added',
            'total',
            'external_id'
        ]

    def get_parcel_status(self, obj):
        return obj.parcel_status.name

    def get_date_added(self, obj):
        return obj.date_added.strftime("%d.%m.%Y")


#-- 13.03.18  ---
class AirParcelSerializer(ModelSerializer):

    class Meta:
        model = AirParcel
        fields = [
            'air_id',
            'parcel_id',
            'address_id',
        ]


class ParcelHistorySerializer(ModelSerializer):
    parcel_status_id = SerializerMethodField()
    date_added = SerializerMethodField()

    class Meta:
        model = ParcelHistory
        fields = [
            'parcel_status_id',
            'date_added',
        ]

    def get_parcel_status_id(self, obj):
        #print(dir(obj.parcel_status_id))
        return obj.parcel_status.next_status_text

    def get_date_added(self, obj):
        return obj.date_added.strftime("%d.%m.%Y")
#-------------------------------------------------
#------- 12.06.18---------------------------------
class PackProductSerializer(ModelSerializer):

    class Meta:
        model = PackProduct
        fields = [
            'pack_product_id',
            'pack',
            'name',
            'price',
            'quantity',
        ]

class ParcelPackProductSerializer(ModelSerializer):

    class Meta:
        model = ParcelPackProduct
        fields = [
            'parcel_pack_product_id',
            'parcel_id',
            'pack_product_id',
            'quantity',
        ]

class AddressSerializer(ModelSerializer):

    class Meta:
        model = Address
        fields = [
            'firstname',
            'lastname',
            'address_1',
            'city',
            'dom',
            'zone_id'
        ]

#-------------------------------------------------
#-- 26.01.19 -------------------------------------
class PlombaDimensionSerializer(ModelSerializer):

    class Meta:
        model = PlombaDimension
        fields = [
            'plomba_id',
            'plomba_width',
            'plomba_height',
            'plomba_length',
            'plomba_weight'
        ]

class ParcelUaDataCreateSerializer(ModelSerializer):
    class Meta:
        model = ParcelUaData
        fields = [
            'parcel_ua_id',
            'plomba_id',
            'width',
            'height',
            'length',
            'volume',
            'weight',
        ]


class AirSerializer(ModelSerializer):
    # air_status_id = SerializerMethodField()
    
    class Meta:
        model = Air
        fields = [
            'air_id',
            'name',
            'air_status_id',
        ]

    # def get_air_status_id(self, obj):
    #     return obj.air_status_id.name


class PackClientSerializer(ModelSerializer):
    # customer = SerializerMethodField()

    class Meta:
        model = Pack
        fields = [
            "customer",
            "pack_status",
            "weight",
        ]

    # def get_customer(self, obj):
    #     return obj.customer.external_id



class ParcelUaSerializer(ModelSerializer):

    class Meta:
        model = ParcelUa
        fields = [
            "parcel_ua_id",
        ]


class PackCreateSerializer(ModelSerializer):
    class Meta:
        model = Pack
        # fields = '__all__'
        exclude = [
            'pack_id',
            'date_added',
            'is_received_1c',
            'sklad',
            'language',
            'pack_status',
            'category_group',
            'currency',
        ]


class CustomerSerializer(ModelSerializer):
    # date_added = SerializerMethodField()

    class Meta:
        model = Customer
        fields = [
            "external_id",
            "customer_id",
            # "date_added",
        ]

    # def get_date_added(self, obj):
    #     return obj.date_added.strftime("%d.%m.%Y")


class PartnerInc0SandboxCreateSerializer(ModelSerializer):
    class Meta:
        model = PartnerInc0Sandbox
        fields = '__all__'




# class PackProductSerializer(ModelSerializer):
#     class Meta:
#         model = PackProduct
#         fields = ('name', 'quantity', 'price')

class PackProductSerializer(ModelSerializer):
    class Meta:
        model = PackProduct
        fields = [
            'name',
            'price',
            'quantity',
            'item_class_id',
            'weight',
            'volume',
            'point',
            'url',
            'packed_quantity',
        ]



class MobileAppPackSerializer(ModelSerializer):
    products = PackProductSerializer(many=True)
    # image = serializers.ImageField(max_length=None, allow_empty_file=True)

    class Meta:
        model = Pack
        exclude = [
            'pack_id',
            'date_added',
            'is_received_1c',
            'sklad',
            'language',
            'pack_status',
            'category_group',
            'currency',
        ]

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        pack = Pack.objects.create(**validated_data)
        for product_data in products_data:
            PackProduct.objects.create(pack=pack, **product_data)
        return pack