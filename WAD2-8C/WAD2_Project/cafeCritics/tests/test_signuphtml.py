from django.test import TestCase
from django.urls import reverse
from cafeCritics.forms import UserRegistrationForm
from django.contrib.auth.models import User

class SignupViewTests(TestCase):

    def test_signup_view_get(self):
        """
        Test that a GET request to the signup page returns a status code of 200 and utilizes the appropriate template
        """
        url = reverse('cafeCritics:signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
        self.assertIsInstance(response.context['form'], UserRegistrationForm)

    def test_signup_view_post_invalid(self):
        """
        Test that a POST request with invalid data, such as an empty form, does not redirect and instead re-renders the page with error messages.
        """
        url = reverse('cafeCritics:signup')
        response = self.client.post(url, data={})
        self.assertEqual(response.status_code, 200)
        # Check that errors are present; adjust error keys depending on your form's fields.
        self.assertFormError(response, 'form', 'username', 'This field is required.')

    def test_signup_view_post_valid(self):
        """
        Test that a POST request with valid data successfully creates a new user and redirects to the appropriate page.
        """
        url = reverse('cafeCritics:signup')
        valid_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'StrongPassword123!',
            'password2': 'StrongPassword123!',
            'user_type': 'personal',
        }
        response = self.client.post(url, data=valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())