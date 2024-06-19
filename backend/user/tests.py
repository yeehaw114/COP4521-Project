from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User, Group
from .models import UserManager

class RBACModelTest(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(username='admin', password='admin')
        self.normal_user = User.objects.create_user(username='user', password='user')
        self.admin_group = Group.objects.create(name='Admin')
        self.user_group = Group.objects.create(name='User')

        self.admin_user.groups.add(self.admin_group)
        self.normal_user.groups.add(self.user_group)

    def test_admin_permissions(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)

    def test_user_permissions(self):
        self.client.login(username='user', password='user')
        response = self.client.get('/user/')
        self.assertEqual(response.status_code, 200)