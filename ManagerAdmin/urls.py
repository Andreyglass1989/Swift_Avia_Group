from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from .views import ( 
    ClientsListView,
    ClientCreateView,
    NewPostListView,
    CargoListView,
    # paymentCard,
    todayPayment,
    lastdayPayment,
    example_payment
   )

urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name='dashboard.html'), name='home'),
    url(r'^clients/$', ClientsListView.as_view(), name='clients'),
    # url(r'^client-add/$', ClientCreateView.as_view(), name='AddClient'),
    # url(r'^payment/$', paymentCard, name='payment'),
    url(r'^lastdayPayment/$', lastdayPayment, name='paymentLastday'),
    url(r'^todayPayment/$', todayPayment, name='paymentToday'),
    url(r'^Payment/$', example_payment, name='payment_example'),
    url(r'^calendar/$', TemplateView.as_view(template_name='calendar.html'), name='calendar'),
    url(r'^new-post/$', NewPostListView.as_view(template_name='NewPost.html'), name='new_post'),
    url(r'^cargo-list/$', CargoListView.as_view(template_name='CargoList.html'), name='cargo_list'),
    url(r'^create-client/$', ClientCreateView.as_view(), name='create_client'),
    # url(r'^about_user/$', about_user, name='about_user'),
    # url(r'^edit_user/(?P<pk>\d+)/$', UserUpdateView.as_view(), name='update_user'),
    # url(r'^consolidation/$', consolidation),
    # url(r'^v_puti/$', v_puti),
    # url(r'^detail/(?P<pack_number>\d+)/$', detail),
    # # url(r'^(?P<username>[\w-]+)/priletel/$', DetailDetailView.as_view()),
    # url(r'^priletel/$', priletel),
    # url(r'^recipients/$', recipients, name='recipients'),
    # url(r'^add_recipients/$', RecipientsCreateView.as_view(), name='create_recipients'),
    # url(r'^edit_recipients/(?P<pk>\d+)/$', RecipientsUpdateView.as_view(), name='edit_recipients'),
    # url(r'^delete_recipients/(?P<pk>\d+)/$', remove_recip, name='delete_recipients'),
    # #url(r'^contacts/send_mail/$', send_mail_to_us, name='send_mail_to_us'),

    # url(r'^oplata/$', oplata),
    # url(r'^excepted_cargo/$', ExpectedCargoListView.as_view(), name='excepted_cargo'),
    # #url(r'^add_expected_cargo/$', pack_children),

    # url(r'^add_expected_cargo/$', ExpectedCargoCreateView.as_view()),
    # url(r'^edit_expected_cargo/(?P<pk>\d+)/$', ExpectedCargoUpdateView.as_view()),
    # url(r'^delete_excepted_cargo/(?P<pk>\d+)/$', remove_excepted_cargo, name='delete_excepted_cargo'),
    # url(r'^statistic/$', statistic),

    # url(r'^buyout/$', BuyoutListView.as_view(), name='buyout'),
    # url(r'^add_buyout/$', formset_view, name='add-buyout'),

]
