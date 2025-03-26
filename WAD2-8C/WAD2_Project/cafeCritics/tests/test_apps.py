from django.test import SimpleTestCase
from cafe.apps import CafeConfig

class CafeConfigTest(SimpleTestCase):
    def test_app_config_name(self):
        self.assertEqual(CafeConfig.name, 'cafe')