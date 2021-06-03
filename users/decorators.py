from django.shortcuts import redirect
from .models import Users

def admin_required(func):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user is None or not user:
            return redirect('/login/')
        user = Users.objects.get(email=user)
        if user.is_staff == False:
            return redirect('/product/')
        return func(request, *args, **kwargs)
    return wrap
