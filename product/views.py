from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView

from order.form import OrderForm
from product.models import Product
from .form import RegisterForm
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from users.decorators import admin_required

class ProductListView(ListView):
    template_name = 'product_list.html'
    model = Product

@method_decorator(admin_required, name = 'dispatch')
class ProductRegister(FormView):
    template_name = 'product_register.html'
    form_class = RegisterForm
    success_url = '/product'
    def form_valid(self, form):
        product = Product(
            name = form.data.get('name'),
            price = form.data.get('price'),
            stock = form.data.get('stock'),
            image=form.cleaned_data['image'],
            description = form.data.get('description')
        )
        product.save()
        return super().form_valid(form)

class ProductDetailView(DetailView):
    template_name = "product_detail.html"
    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(self.request)
        return context