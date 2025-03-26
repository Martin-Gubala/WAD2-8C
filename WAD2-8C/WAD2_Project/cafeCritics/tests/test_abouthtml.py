from django.test import TestCase
from django.urls import reverse

class AboutPageTests(TestCase):
    #This test makes sure that the About page returns a 200 OK status code.
    def test_about_page_status_code(self):
        url = reverse('cafeCritics:about')# Get the URL for the about page using reverse
        response = self.client.get(url) # Send a GET request to that URL
        self.assertEqual(response.status_code, 200)# Check the if the response is 200 OK

    # This test checks if the About page uses the correct template.
    def test_about_page_uses_correct_template(self):
        url = reverse('cafeCritics:about')# Again this gets the URL for the about page using reverse
        response = self.client.get(url)# Get a GET request to that URL
        self.assertTemplateUsed(response, 'about.html')# Check if the 'about.html' template is used