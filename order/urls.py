from django.urls import path

from .views import OrderCreate, OrderListView

urlpatterns = [
    path('create/', OrderCreate.as_view()),
    path('complete/',OrderCreate.as_view(), name='ordercomplete'),
    path('orderlist/',OrderListView.as_view(), name='orderlist'),
]