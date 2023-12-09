# from django.test import TestCase, Client
# from django.urls import reverse
# from rest_framework import status
# from django.contrib.auth import get_user_model
# from .models import CustomUser
# from organization.models import Company
# from django.contrib.auth.models import Group
# import factory
#
#
#
#
# class TestLoginView(TestCase):
#     def setUp(self):
#         self.company = Company.objects.create(name="Test Company")
#         self.user = get_user_model().objects.create_user(username="testuser",
#                                                          password="testpasword",
#                                                          company=self.company,
#                                                          job_position='none')
#         self.login_url = reverse("login")
#         self.group_name = 'none'
#
#         try:
#             self.group = Group.objects.get(name=self.group_name)
#         except Group.DoesNotExist:
#             self.group = Group.objects.create(name=self.group_name)
#
#         self.user.groups.add(self.group)
#
#
#     def test_login_success(self):
#
#         data = {'username': 'testuser', 'password': 'testpassword'}
#         response = self.client.post(self.login_url, data, follow=True)
#         self.assertEquals(response.status_code, status.HTTP_200_OK)
#         self.assertRedirects(response, reverse("home"))
#         self.assertTrue(response.context["user"].is_authenticated)
#
#
