from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect

from users.models import Users
from .form import RegisterForm, LoginForm
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import inlineformset_factory

def home(request):
    return render(request, "users/sign_in1.html")
def signIn(request):
    return render(request, "users/sign_in2.html")
def signUp(request):
    return render(request, "users/sign_up1.html")
def resetPassword(request):
    return render(request, "users/sign_in3.html")   
def createPassword(request):
    return render(request, "users/sign_in5.html")
def verifyAccount(request):
    return render(request, "users/sign_up2.html")
def success(request):
    return render(request, "users/sign_up3.html")
def mypage(request):
    return render(request, "users/status.html")

def registerPage(request):
    form = UserCreationForm()
    # template_name = 'users/sign_up1.html'

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            
    context = {'form':form}
    return render(request, 'users/sign_up1.html', context)


class RegisterView(FormView):
    template_name = 'users/sign_in2.html'
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
    template_name = 'users/sign_in2.html'
    form_class = LoginForm
    # success_url = '/product'

    def form_valid(self, form):
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authentication_classes.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/success/')
            else:
                return render(request, 'users/sign_in2.html', {'error':'username or password is incorrect'})
            # 로그인 실패시 'username or password is incorrect' 메시지를 띄움  
        else:
            return render(request, 'users/sign_in2.html')
    #     self.request.session['user'] = form.data.get('email')
    #     return super().form_valid(form)

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')

@api_view(['GET'])
def userAPI(request):
    userlist = list(Users.objects.all())
    serializer = UserSerializer(userlist, many=True)
    return Response(serializer.data)