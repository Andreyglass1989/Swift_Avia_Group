from rest_framework.serializers import ModelSerializer, SerializerMethodField
# from login.models import UserProfile
# from django.contrib import auth
# from django.contrib.auth.models import User
from login.api.serializers import UserDetalSerializer
from LK.models import Pack, PackProduct, Parcel



class PackListSerializer(ModelSerializer):
    customer = SerializerMethodField()
    pack_status = SerializerMethodField()
    date_added =SerializerMethodField()

    class Meta:
        model = Pack
        fields = [
            'pack_id',
            'pack_number',
            'customer',
            'pack_status',
            'date_added',
            'weight',
            #'date0',
        ]

    def get_pack_status(self, obj):
        return obj.pack_status.name

    def get_customer(self, obj):
        return obj.customer.external_id

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
            'parcel_number',
            'parcel_status',
            'date_added',
        ]

    def get_parcel_status(self, obj):
        return obj.parcel_status.name

    def get_date_added(self, obj):
        return obj.date_added.strftime("%d.%m.%Y")