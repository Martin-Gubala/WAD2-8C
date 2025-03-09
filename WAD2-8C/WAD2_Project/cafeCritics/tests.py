from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserAuthTests(TestCase):
    def test_login_view(self):
        User.objects.create_user(username='testuser', password='12345')
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': '12345'})
        self.assertRedirects(response, expected_url=reverse('home_page'), status_code=302, target_status_code=200)

    def test_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, expected_url=reverse('login'))