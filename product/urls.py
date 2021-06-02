from order.views import OrderCreate
from product.views import ProductRegister, ProductDetailView
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', ProductListView.as_view(), name='ProductListView'),

    path('register/', ProductRegister.as_view(), name='ProductRegister'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    #path('order/create/', OrderCreate.as_view(), name='ordercreate'),
    path('category/<int:pk>',views.category_list, name='category'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)