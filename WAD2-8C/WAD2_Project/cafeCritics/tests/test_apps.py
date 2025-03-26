from django.test import SimpleTestCase
from cafe.apps import CafeConfig

class CafeConfigTest(SimpleTestCase):
    # This test checks if the app configuration for the cafe app is correct
    #It makes sure that the name of the app is set to 'cafe'
    def test_app_config_name(self):
        self.assertEqual(CafeConfig.name, 'cafe')