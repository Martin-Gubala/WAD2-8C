from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserAuthTests(TestCase):
    # This test checks that when a user logs in with the correct credentials
    # they are redirected to the home page.
    def test_login_view(self):
        User.objects.create_user(username='testuser', password='12345')
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': '12345'})
        self.assertRedirects(response, expected_url=reverse('home_page'), status_code=302, target_status_code=200)

    # This test checks that the logout view works correctly and redirects the user to the login page.
    def test_logout_view(self):
        # Send a GET request to the logout URL.
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, expected_url=reverse('login'))