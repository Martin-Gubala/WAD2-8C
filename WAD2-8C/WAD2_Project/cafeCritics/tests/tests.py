from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
class UserAuthTests(TestCase):
    # This test checks that when a user logs in with the correct credentials,
    # they are redirected to the home page.
    def test_login_view(self):
        User.objects.create_user(username='testuser', password='12345')
        response = self.client.post(reverse('cafeCritics:login'), {
            'username': 'testuser', 
            'password': '12345'
        })
        self.assertRedirects(response, expected_url=reverse('cafeCritics:home_page'),
                             status_code=302, target_status_code=200)

