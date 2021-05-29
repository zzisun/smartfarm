from django.urls import path
from . import views
from .views import OrderCreate, OrderListView,AddCart,modify_cart

urlpatterns = [
    path('create/', OrderCreate.as_view()),
    path('addcart/', AddCart.as_view()),
    path('complete/',OrderCreate.as_view(), name='ordercomplete'),
    #path('orderlist/',OrderListView.as_view(), name='orderlist'),
    path('orderlist/<int:pk>',views.order_list, name='order_list'),
    path('cart/<int:pk>',views.cart_list, name='cartlist'),
    path('cart/modify/<int:pk>', views.modify_cart,name='modifycart'),
    path('payment/',views.payment, name='payment'),
    path('payment/complete',views.cart_to_buy, name='cartbuy')
]