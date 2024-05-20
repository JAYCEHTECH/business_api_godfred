from django.conf.urls.static import static
from django.urls import path

from business_api import views
from django.conf import settings as conf_settings

urlpatterns = [
    path('', views.home, name='home'),
    path('generate_token', views.generate_token, name='generate_token'),
    path('regenerate_token', views.regenerate_token, name='regenerate_token'),
    path('get_user_token', views.get_user_token, name='get_user_token'),

    path('api/initiate_mtn', views.initiate_mtn_transaction, name='initiate_mtn_transaction'),
    path('api/initiate_ishare', views.initiate_ishare_transaction, name='ishare_transaction'),
    path('api/initiate_big_time', views.initiate_big_time, name='big_time'),
    path('api/initiate_wallet_topup', views.wallet_topup, name='wallet_topup'),

    path('hubtel_webhook', views.hubtel_webhook, name='hubtel_webhook'),
    path('paystack_webhook', views.paystack_webhook, name='paystack_webhook'),
    path('export_unknown_transactions/', views.export_unknown_transactions, name='export_unknown_transactions'),

    path('api/initiate_mtn_airtime', views.initiate_at_airtime, name='initiate_mtn_airtime'),
    path('api/initiate_voda_airtime', views.initiate_voda_airtime, name='initiate_voda_airtime'),
    path('api/initiate_at_airtime', views.initiate_at_airtime, name='initiate_at_airtime'),
    path('api/initiate_glo_airtime', views.initiate_glo_airtime, name='initiate_glo_airtime'),

    path('elevated/api/initiate_mtn', views.admin_initiate_mtn_transaction, name='initiate_mtn_transaction'),
    path('elevated/api/initiate_ishare', views.admin_initiate_ishare_transaction, name='ishare_transaction'),
    path('elevated/api/initiate_big_time', views.admin_initiate_big_time, name='big_time'),

    path('api/elevated/initiate_mtn_airtime', views.admin_initiate_mtn_airtime, name='initiate_mtn_airtime'),
    path('api/elevated/initiate_voda_airtime', views.admin_initiate_voda_airtime, name='initiate_voda_airtime'),
    path('api/elevated/initiate_at_airtime', views.admin_initiate_at_airtime, name='initiate_at_airtime'),
    path('api/elevated/initiate_glo_airtime', views.admin_initiate_glo_airtime, name='initiate_glo_airtime'),
] + static(conf_settings.STATIC_URL, document_root=conf_settings.STATIC_ROOT)

