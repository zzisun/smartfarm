from users.models import Users
from django.test import TestCase

# Create your tests here.
from django.contrib import auth

class AuthTestCase(TestCase):
    def setUp(self):
        self.u = Users.objects.create_superuser('test@dom.com', 'pass')
        self.u.save()

    def testLogin(self):
        self.client.login(username='test@dom.com', password='pass')

# class emailTestCase(TestCase):
#     def setUp(self) -> None:
#         self.user = Users.objects.create_user('test@dom.com')
#         self.user.save()
    
#     def testLogin(self):
#         self.client.login(username='test@dom.com', password='pass')