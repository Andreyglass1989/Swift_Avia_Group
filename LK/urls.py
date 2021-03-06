from django.conf.urls import url, include
from LK.views import (
  #  lk,
    about_user,
    UserUpdateView,
    consolidation,
    v_puti,
    priletel,
    detail,
    recipients,
    get_data,

    HomeView,
    ChartData,

    RecipientsCreateView,
    RecipientsUpdateView,
    #RecipientsDeleteView,
    oplata,
    ExpectedCargoListView,
    ExpectedCargoCreateView,
    ExpectedCargoUpdateView,
    remove_recip,
    remove_excepted_cargo,
    # DetailDetailView,
   # search,
   # send_mail_to_us
    #pack_children,
    BuyoutListView,
    formset_view,
    hello_world_ex,
    )


urlpatterns = [
    
    url(r'^about_user/$', about_user, name='about_user'),
    url(r'^edit_user/(?P<pk>\d+)/$', UserUpdateView.as_view(), name='update_user'),
    url(r'^consolidation/$', consolidation),
    url(r'^v_puti/$', v_puti),
    url(r'^detail/(?P<pack_number>\d+)/$', detail),
    # url(r'^(?P<username>[\w-]+)/priletel/$', DetailDetailView.as_view()),
    url(r'^priletel/$', priletel),
    url(r'^recipients/$', recipients, name='recipients'),
    url(r'^add_recipients/$', RecipientsCreateView.as_view(), name='create_recipients'),
    url(r'^edit_recipients/(?P<pk>\d+)/$', RecipientsUpdateView.as_view(), name='edit_recipients'),
    url(r'^delete_recipients/(?P<pk>\d+)/$', remove_recip, name='delete_recipients'),
    #url(r'^contacts/send_mail/$', send_mail_to_us, name='send_mail_to_us'),

    url(r'^oplata/$', oplata),
    url(r'^excepted_cargo/$', ExpectedCargoListView.as_view(), name='excepted_cargo'),
    #url(r'^add_expected_cargo/$', pack_children),

    url(r'^add_expected_cargo/$', ExpectedCargoCreateView.as_view()),
    url(r'^edit_expected_cargo/(?P<pk>\d+)/$', ExpectedCargoUpdateView.as_view()),
    url(r'^delete_excepted_cargo/(?P<pk>\d+)/$', remove_excepted_cargo, name='delete_excepted_cargo'),
#    url(r'^search/$', search),

    url(r'^for-Sashka/$', get_data, name='Sashka'),
    url(r'^for-Sashka-class/$', HomeView.as_view(), name='Sashka0'),
    url(r'^for-Sashka-class1/$', ChartData.as_view(), name='Sashka1'),

    url(r'^buyout/$', BuyoutListView.as_view(), name='buyout'),
    url(r'^add_buyout/$', formset_view, name='add-buyout'),

    url(r'^hello_world/$', hello_world_ex)

    #url(r'^', lk, name='lk'),
]
