import test_api
import unittest

class APITestCase(unittest.TestCase):

    def setUp(self):
        test_api.app.testing = True
        self.app = test_api.app.test_client()
