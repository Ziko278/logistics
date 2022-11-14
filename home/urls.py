from django.urls import path
from home.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('service', ServicePageView.as_view(), name='services'),
    path('shipment/track', track_shipment, name='track'),
    path('shipment/<str:tracking_id>/pin', track_locked_shipment, name='track_locked'),
    path('message/<str:status>', message, name='message'),
    path('get-quote', logistic_quote, name='quote'),

]

