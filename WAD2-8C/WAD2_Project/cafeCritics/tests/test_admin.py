from django.contrib import admin
from django.test import SimpleTestCase
from cafeCritics.models import UserProfile, Cafe, Drink, Review
from cafeCritics.admin import CafeAdmin
class AdminTests(SimpleTestCase):
    #This test checks if the UserProfile model is registered in the admin site.
    def test_userprofile_registered(self):
        self.assertIn(UserProfile, admin.site._registry,
                      "UserProfile model is not registered in admin")
    #This test checks if the Cafe model is registered in the admin site.
    def test_cafe_registered(self):
        self.assertIn(Cafe, admin.site._registry,
                      "Cafe model is not registered in admin")
    # This test checks if the Drink model is registered in the admin site.
    def test_drink_registered(self):
        self.assertIn(Drink, admin.site._registry,
                      "Drink model is not registered in admin")

    #This test checks if the Review model is registered in the admin site.
    def test_review_registered(self):
        self.assertIn(Review, admin.site._registry,
                      "Review model is not registered in admin")

    # This test verifies that the custom CafeAdmin class has the correct settings.
    def test_cafe_admin_prepopulated_fields(self):
        #Get the admin configuration for the Cafe model.
        cafe_admin = admin.site._registry.get(Cafe)
        #Check if the prepopulated_fields attribute matches what we expect.
        self.assertEqual(cafe_admin.prepopulated_fields, {'slug': ('name',)},
                         "CafeAdmin prepopulated_fields does not match expected configuration")