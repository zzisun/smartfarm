from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from users.models import Users
from .form import RegisterForm, LoginForm
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer

def signIn(request):
    return render(request, "users/templates/sign_in1.html")

def home(request):
    return render(request, 'home.html', {'user' : request.session.get('user')})


class RegisterView(FormView):
    template_name = 'user_register.html'
    form_class = RegisterForm
    success_url = '/login'

    def form_valid(self, form):
        user = Users(
            email=form.data.get('email'),
            name=form.data.get('name'),
            password=make_password(form.data.get('password')),
            level='user'
        )
        user.save()

        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/product'

    def form_valid(self, form):
        self.request.session['user'] = form.data.get('email')
        return super().form_valid(form)

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')

@api_view(['GET'])
def userAPI(request):
    userlist = list(Users.objects.all())
    serializer = UserSerializer(userlist, many=True)
    return Response(serializer.data)