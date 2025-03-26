from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from cafeCritics import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

class TestUrls(SimpleTestCase):
    def test_home_page_url_resolves(self):
        url = reverse('cafeCritics:home_page')
        self.assertEqual(resolve(url).func, views.home_view)

    def test_cafes_url_resolves(self):
        url = reverse('cafeCritics:cafes')
        self.assertEqual(resolve(url).func, views.cafes_view)

    def test_search_url_resolves(self):
        url = reverse('cafeCritics:search')
        self.assertEqual(resolve(url).func, views.search_results)

    def test_about_url_resolves(self):
        url = reverse('cafeCritics:about')
        self.assertEqual(resolve(url).func, views.about_view)

    def test_account_settings_url_resolves(self):
        url = reverse('cafeCritics:account_settings')
        self.assertEqual(resolve(url).func, views.account_settings_view)

    def test_show_cafe_url_resolves(self):
        slug = "test-cafe"
        url = reverse('cafeCritics:show_cafe', args=[slug])
        self.assertEqual(resolve(url).func, views.show_cafe)

    def test_show_drinks_url_resolves(self):
        slug = "test-cafe"
        url = reverse('cafeCritics:show_drinks', args=[slug])
        self.assertEqual(resolve(url).func, views.show_drinks)

    def test_show_cafeAJAX_url_resolves(self):
        slug = "test-cafe"
        url = reverse('cafeCritics:show_cafeAJAX', args=[slug])
        self.assertEqual(resolve(url).func, views.show_cafeAJAX)

    def test_review_url_resolves(self):
        slug = "test-cafe"
        url = reverse('cafeCritics:review', args=[slug])
        self.assertEqual(resolve(url).func, views.review_view)

    def test_signup_url_resolves(self):
        url = reverse('cafeCritics:signup')
        self.assertEqual(resolve(url).func, views.signup_view)

    def test_login_url_resolves(self):
        url = reverse('cafeCritics:login')
        resolved = resolve(url)
        self.assertEqual(resolved.func.view_class, LoginView)

    def test_cafe_setup_url_resolves(self):
        url = reverse('cafeCritics:cafe_setup')
        self.assertEqual(resolve(url).func, views.cafe_setup_view)

    def test_profile_url_resolves(self):
        username = "testuser"
        url = reverse('cafeCritics:profile', args=[username])
        self.assertEqual(resolve(url).func, views.profile_view)

    def test_edit_cafe_url_resolves(self):
        slug = "test-cafe"
        url = reverse('cafeCritics:edit_cafe', args=[slug])
        self.assertEqual(resolve(url).func, views.edit_cafe_view)
