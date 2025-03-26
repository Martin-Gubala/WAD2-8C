from django.contrib import admin
from django.test import SimpleTestCase
from cafeCritics.models import UserProfile, Cafe, Drink, Review
from cafeCritics.admin import CafeAdmin

class AdminTests(SimpleTestCase):
    def test_userprofile_registered(self):
        self.assertIn(UserProfile, admin.site._registry,
                      "UserProfile model is not registered in admin")

    def test_cafe_registered(self):
        self.assertIn(Cafe, admin.site._registry,
                      "Cafe model is not registered in admin")

    def test_drink_registered(self):
        self.assertIn(Drink, admin.site._registry,
                      "Drink model is not registered in admin")

    def test_review_registered(self):
        self.assertIn(Review, admin.site._registry,
                      "Review model is not registered in admin")

    def test_cafe_admin_prepopulated_fields(self):
        # Retrieve the admin class registered for Cafe.
        cafe_admin = admin.site._registry.get(Cafe)
        # Check that the prepopulated_fields are set as expected.
        self.assertEqual(cafe_admin.prepopulated_fields, {'slug': ('name',)},
                         "CafeAdmin prepopulated_fields does not match expected configuration")