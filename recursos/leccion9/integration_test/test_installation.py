"""Unitest for the social networks components integration"""

import unittest
from installation import instagram_integration, whatsapp_integration


class InstallationTest(unittest.TestCase):
    def test_instagram_integration(self):
        result = instagram_integration()
        self.assertEqual(result, "Hi, from Instagram API")

    def test_not_instagram_integration(self):
        result = instagram_integration()
        self.assertNotEqual(result, "Hello, from Instagram API")

    def test_whatsapp_integration(self):
        result = whatsapp_integration()
        self.assertEqual(result, "Hello, from WhatsApp API")

    def test_not_whatsapp_integration(self):
        result = whatsapp_integration()
        self.assertNotEqual(result, "Hi, from WhatsApp API")


if __name__ == "__main__":
    unittest.main()
