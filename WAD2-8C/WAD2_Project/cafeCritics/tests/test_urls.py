from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from cafeCritics import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

class TestUrls(SimpleTestCase):
    # Test if the home page URL resolves to the correct view function.
    def test_home_page_url_resolves(self):
        url = reverse('cafeCritics:home_page')
        self.assertEqual(resolve(url).func, views.home_view)
    # Test if the URL for listing cafes resolves correctly.
    def test_cafes_url_resolves(self):
        url = reverse('cafeCritics:cafes')
        self.assertEqual(resolve(url).func, views.cafes_view)
    # Test if the search URL resolves correctly.
    def test_search_url_resolves(self):
        url = reverse('cafeCritics:search')
        self.assertEqual(resolve(url).func, views.search_results)

    # Test if the about page URL resolves to the about view.
    def test_about_url_resolves(self):
        url = reverse('cafeCritics:about')
        self.assertEqual(resolve(url).func, views.about_view)

    # Test if the account settings URL resolves correctly.
    def test_account_settings_url_resolves(self):
        url = reverse('cafeCritics:account_settings')
        self.assertEqual(resolve(url).func, views.account_settings_view)

    #Test if the show cafe URL (with a slug) resolves to the correct view.
    def test_show_cafe_url_resolves(self):
        slug = "test-cafe"
        url = reverse('cafeCritics:show_cafe', args=[slug])
        self.assertEqual(resolve(url).func, views.show_cafe)

    #Test if the drinks URL for a cafe resolves properly.
    def test_show_drinks_url_resolves(self):
        slug = "test-cafe"
        url = reverse('cafeCritics:show_drinks', args=[slug])
        self.assertEqual(resolve(url).func, views.show_drinks)

    # Test if the AJAX URL for updating cafe details resolves.
    def test_show_cafeAJAX_url_resolves(self):
        slug = "test-cafe"
        url = reverse('cafeCritics:show_cafeAJAX', args=[slug])
        self.assertEqual(resolve(url).func, views.show_cafeAJAX)

    # Test if the review URL resolves to the review view.
    def test_review_url_resolves(self):
        slug = "test-cafe"
        url = reverse('cafeCritics:review', args=[slug])
        self.assertEqual(resolve(url).func, views.review_view)

    #Test if the signup URL resolves to the signup view.
    def test_signup_url_resolves(self):
        url = reverse('cafeCritics:signup')
        self.assertEqual(resolve(url).func, views.signup_view)

    # Test if the login URL resolves to the correct view.
    # Since we use Django's built-in LoginView, we check the view class.
    def test_login_url_resolves(self):
        url = reverse('cafeCritics:login')
        resolved = resolve(url)
        self.assertEqual(resolved.func.view_class, LoginView)

    # Test if the cafe setup URL resolves properly.
    def test_cafe_setup_url_resolves(self):
        url = reverse('cafeCritics:cafe_setup')
        self.assertEqual(resolve(url).func, views.cafe_setup_view)

    #Test if the logout URL resolves properly.
    def test_logout_url_resolves(self):
        url = reverse('cafeCritics:logout')
        self.assertEqual(resolve(url).func, views.logout_view)
    # Test if the profile URL for a given username resolves correctly.
    def test_profile_url_resolves(self):
        username = "testuser"
        url = reverse('cafeCritics:profile', args=[username])
        self.assertEqual(resolve(url).func, views.profile_view)
    #Test if the edit cafe URL resolves correctly.
    def test_edit_cafe_url_resolves(self):
        slug = "test-cafe"
        url = reverse('cafeCritics:edit_cafe', args=[slug])
        self.assertEqual(resolve(url).func, views.edit_cafe_view)
