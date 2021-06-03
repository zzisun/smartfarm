from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView

from order.form import OrderForm, CartForm
from users.models import Users
from product.models import Product, Category, Addfeature
from .form import RegisterForm
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from users.decorators import admin_required

def category_list(request, pk):
    user = Users.objects.get(email=request.user.email)
    if Category.objects.count() > 0:
        while True:
            try:
                category = Category.objects.get(pk=pk)
                break
            except Category.DoesNotExist:
                pk += 1
        all = Category.objects.all()
        product = Product.objects.all()
        context = {'category': category, 'all': all, 'users': user, 'product': product}
    else:
        message = "No Product"
        context = {'message':message}
    return render(request, 'catagory.html',context)


@method_decorator(admin_required, name = 'dispatch')
class ProductRegister(FormView):
    template_name = 'product_register.html'
    form_class = RegisterForm
    success_url = '/product'
    def form_valid(self, form):
        product = Product(
            name = form.data.get('name'),
            price = form.data.get('price'),
            category = Category.objects.get(id = form.data.get('category')),
            stock = form.data.get('stock'),
            image=form.cleaned_data['image'],
            description = form.data.get('description')
        )
        product.save()
        return super().form_valid(form)



class ProductDetailView(DetailView):
    template_name = "product.html"
    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orderform'] = OrderForm(self.request)
        context['cartform'] = CartForm(self.request)
        context['users'] = Users.objects.get(email=self.request.user.email)
        context['option'] = Addfeature.objects.filter(product=self.kwargs['pk'])
        return context