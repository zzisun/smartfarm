from django.db import transaction
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from product.models import Product
from order.models import Order, Cart
from users.models import Users
from .form import OrderForm, CartForm
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

#주문 생성 view
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
                user = Users.objects.get(email = self.request.user.email),
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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Users.objects.get(email=self.request.user.email)
        return context

class AddCart(FormView):
    form_class = CartForm

    def form_valid(self, form):
        with transaction.atomic():
            prod = Product.objects.get(pk=form.data.get('product'))
            user = Users.objects.get(email=self.request.user.email)
            quant = int(form.data.get('quantity'))
            prev_cart = Cart.objects.filter(user=user)
            flag = False
            for i in prev_cart:
                if prod.id == i.product.id:
                    i.amount += prod.price * quant
                    i.quantity += quant
                    i.save()
                    break
            else:
                amou = prod.price * int(form.data.get('quantity'))
                newcart = Cart(
                    quantity = form.data.get('quantity'),
                    product = prod,
                    user = user,
                    amount = amou
                )
                newcart.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect('/product/')

    def get_success_url(self):
        user = Users.objects.get(email=self.request.user.email)
        return '/order/cart/{}'.format(user.pk)

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw


def order_list(request, pk):
    user = Users.objects.get(pk=pk)
    orders = Order.objects.filter(user=user)
    ongoing = []
    fo = True
    history =[]
    fh = True
    for i in orders:
        #history
        if i.status == 'Deli':
            history.append(i)
            fh = False
        else:
            ongoing.append(i)
            fo = False
    context = {'history':history, 'fh':fh,'ongoing':ongoing, 'fo':fo}
    return render(request, 'account3.html',context)

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
    user = Users.objects.get(email=request.user.email)

    return redirect('cartlist',user.pk)

def payment(request):
    return render(request,'payment.html')

def cart_to_buy(request):
    user = Users.objects.get(email=request.user.email)
    cart = Cart.objects.filter(user=user)
    for prod in cart:
        product = Product.objects.get(pk=prod.product.id)
    #prod = Product.objects.get(pk=form.data.get('product'))
        amou = product.price * int(prod.quantity)
    #print(amou)
        order = Order(
            quantity=prod.quantity,
            product=product,
            user=Users.objects.get(email=request.user.email),
            amount=amou
        )
        order.save()
        product.stock -= int(prod.quantity)
        product.save()
        prod.delete()
    return redirect('ordercomplete')