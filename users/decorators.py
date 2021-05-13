from django.shortcuts import redirect
from .models import Users

def admin_required(func):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login/')
        user = Users.objects.get(email=user)
        if user.level != 'admin':
            return redirect('/product/')
        return func(request, *args, **kwargs)
    return wrap

def login_required(func):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login/')
        return func(request, *args, **kwargs)
    return wrap