from django.test import TestCase
from django.test.client import Client

class IndexTestCase(TestCase):
    def setUp(self):
        pass

    def test_index_get(self):
        '''Simple sanity check.'''
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code,200)

