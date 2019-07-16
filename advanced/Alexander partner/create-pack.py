from LK.models import (
    Pack, 
    PackProduct, 
    ParcelPackProduct, 
    Currency,
    CategoryGroup,
    Language,
)

pack_partner = Pack(
pack_number = 130200009,
customer_id = 1005,
pack_status = PackStatus.objects.get(pack_status_id=1), 
volume = 1,
weight = 1,
point = 1,
comment = "1-450",
external_id = "",
total= 1,
currency_code = "USD",
currency_value= 1.0,
sandbox= 0,
def_field = 0,
packlist = 0,
sklad_id = 6,
# sklad = Sklad.objects.get(sklad_id=1),
language = Language.objects.get(language_id=2),
currency = Currency.objects.get(currency_id=2),
category_group = CategoryGroup.objects.get(category_group_id = 3))
pack_partner.save()

pack_product = PackProduct (
pack = pack_partner,
name = "bla",
price = 100,
quantity = 100,
item_class_id = 0,
weight = 10,
weight_netto = 9,
volume = 1,
point = 1,
# url = None
)
pack_product.save()