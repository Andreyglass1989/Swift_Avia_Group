from django.conf.urls import url, include
from LK.views import (
    lk,
    about_user,
    UserUpdateView,
    consolidation,
    v_puti,
    priletel,
    detail,
    recipients,
    RecipientsCreateView,
    RecipientsUpdateView,
    #RecipientsDeleteView,
    oplata,
    ExpectedCargoListView,
    ExpectedCargoCreateView,
    ExpectedCargoUpdateView,
    remove_recip,
   # search,
   # send_mail_to_us
    )

urlpatterns = [

    url(r'^about_user/$', about_user),
    url(r'^edit_user/(?P<pk>\d+)/$', UserUpdateView.as_view(), name='update_user'),
    url(r'^consolidation/$', consolidation),
    url(r'^v_puti/$', v_puti),
    url(r'^detail/(?P<pack_number>\d+)/$', detail),
    url(r'^priletel/$', priletel),
    url(r'^recipients/$', recipients, name='recipients'),
    url(r'^add_recipients/$', RecipientsCreateView.as_view(), name='create_recipients'),
    url(r'^edit_recipients/(?P<pk>\d+)/$', RecipientsUpdateView.as_view(), name='edit_recipients'),
    url(r'^delete_recipients/(?P<pk>\d+)/$', remove_recip, name='delete_recipients'),
    #url(r'^contacts/send_mail/$', send_mail_to_us, name='send_mail_to_us'),

    url(r'^oplata/$', oplata),
    url(r'^expected_cargo/$', ExpectedCargoListView.as_view()),
    url(r'^add_expected_cargo/$', ExpectedCargoCreateView.as_view()),
    url(r'^edit_expected_cargo/(?P<pk>\d+)/$', ExpectedCargoUpdateView.as_view()),
#    url(r'^search/$', search),



    url(r'^', lk, name='lk'),
    #url(r'^', lk, name='lk'),
]
