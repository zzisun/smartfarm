from django.db import transaction
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from product.models import Product
from order.models import Order, Cart
from users.models import Users
from users.decorators import login_required
from .form import OrderForm, CartForm
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

#주문 생성 view
@method_decorator(login_required, name = 'dispatch')
class OrderCreate(FormView):
    form_class = OrderForm
    success_url = '/order/complete'
    template_name = 'order_complete.html'
    def form_valid(self, form):
        with transaction.atomic():
            prod = Product.objects.get(pk=form.data.get('product'))
            amou = prod.price * int(form.data.get('quantity'))
            print(amou)
            order = Order(
                quantity = form.data.get('quantity'),
                product = prod,
                user = Users.objects.get(email = self.request.session.get('user')),
                amount = amou
            )
            order.save()

            prod.stock -= int(form.data.get('quantity'))
            prod.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect('/product/')

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw

@method_decorator(login_required, name = 'dispatch')
class AddCart(FormView):
    form_class = CartForm

    #template_name = 'order_complete.html'
    def form_valid(self, form):
        with transaction.atomic():
            prod = Product.objects.get(pk=form.data.get('product'))
            amou = prod.price * int(form.data.get('quantity'))
            #print(amou)
            order = Cart(
                quantity = form.data.get('quantity'),
                product = prod,
                user = Users.objects.get(email = self.request.session.get('user')),
                amount = amou
            )
            order.save()
            #prod.stock -= int(form.data.get('quantity'))
            #prod.save()
        return super().form_valid(form)

    def get_success_url(self):
        user = Users.objects.get(email=self.request.session.get('user'))
        return '/order/cart/{}'.format(user.pk)

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw

@method_decorator(login_required, name = 'dispatch')
class OrderListView(ListView):
    template_name = 'order_list.html'
    model = Order

def order_list(request, pk):
    user = Users.objects.get(pk=pk)
    orders = Order.objects.filter(user=user)
    context = {'orders':orders}
    return render(request, 'order_list2.html',context)

def cart_list(request, pk):
    user = Users.objects.get(pk=pk)
    cart = Cart.objects.filter(user=user)
    amount = 0
    for prod in cart:
        amount += prod.amount
    vat = (int) (amount * 0.15)
    delivery = 200
    total = amount + vat + delivery
    context = {'cart':cart, 'amount':amount, 'vat':vat,'delivery':delivery, 'total':total}

    return render(request, 'cart.html',context)

@csrf_exempt
def modify_cart(request,pk):
    cart = Cart.objects.get(pk=pk)
    cart.quantity = int(request.POST.get('quantity'))
    cart.amount = cart.product.price * cart.quantity
    cart.save()
    user = Users.objects.get(email=request.session.get('user'))

    return redirect('cartlist',user.pk)