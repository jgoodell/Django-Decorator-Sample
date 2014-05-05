from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from geodata import views

class MockRequest(object):
    def __init__(self,method='GET', content_type='text/html'):
        self.method = method
        self.environ = dict()
        self.environ['CONTENT_TYPE'] = content_type

class IndexTestCase(TestCase):
    def setUp(self):
        pass

    def test_index_get(self):
        '''Simple sanity check.'''
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code,200)

    def test_allowed_method(self):
        '''Test of allowed methods.'''
        response = views.index(MockRequest(method='POST'))
        self.assertEqual(response.status_code,405)
        response = views.index(MockRequest(method='PUT'))
        self.assertEqual(response.status_code,405)
        response = views.index(MockRequest(method='OPTIONS'))
        self.assertEqual(response.status_code,405)
        response = views.index(MockRequest(method='HEAD'))
        self.assertEqual(response.status_code,405)
        response = views.index(MockRequest(method='DELETE'))
        self.assertEqual(response.status_code,405)
        response = views.index(MockRequest(method='PATCH'))
        self.assertEqual(response.status_code,405)
        response = views.index(MockRequest(method='TRACE'))
        self.assertEqual(response.status_code,405)
        response = views.index(MockRequest(method=''))
        self.assertEqual(response.status_code,405)


class DataTestCase(TestCase):
    def setUp(self):
        pass

    def test_get_200(self):
        '''Simple test of a good URI.'''
        response = views.data(MockRequest(),'ct')
        self.assertEqual(response.status_code,200)

    def test_get_200_json(self):
        '''Simple test of a good URI.'''
        response = views.data(MockRequest(content_type="application/json"),'ct')
        self.assertEqual(response.status_code,200)
        try:
            import json
            json.dumps(response.content)
        except Exception, e:
            raise AssertionError(e)

    def test_get_400_json(self):
        '''Simple test of a bad URI.'''
        response = views.data(MockRequest(content_type="application/json"),'bogus')
        self.assertEqual(response.status_code,400)

    def test_get_400(self):
        '''Simple test of a bad URI.'''
        response = views.data(MockRequest(),'bogus')
        self.assertEqual(response.status_code,400)

    def test_allowed_method(self):
        '''Test of allowed methods.'''
        response = views.data(MockRequest(method='POST'),'nc')
        self.assertEqual(response.status_code,405)
        response = views.data(MockRequest(method='PUT'),'nc')
        self.assertEqual(response.status_code,405)
        response = views.data(MockRequest(method='OPTIONS'),'nc')
        self.assertEqual(response.status_code,405)
        response = views.data(MockRequest(method='HEAD'),'nc')
        self.assertEqual(response.status_code,405)
        response = views.data(MockRequest(method='DELETE'),'nc')
        self.assertEqual(response.status_code,405)
        response = views.data(MockRequest(method='PATCH'),'nc')
        self.assertEqual(response.status_code,405)
        response = views.data(MockRequest(method='TRACE'),'nc')
        self.assertEqual(response.status_code,405)
        response = views.data(MockRequest(method=''),'nc')
        self.assertEqual(response.status_code,405)


class AllDataTestCase(TestCase):
    def setUp(self):
        pass

    def test_get_200(self):
        '''Simple test of a good URI.'''
        response = views.all_data(MockRequest())
        self.assertEqual(response.status_code,200)

    def test_get_200_json(self):
        '''Simple test of a good URI.'''
        response = views.all_data(MockRequest(content_type="application/json"))
        self.assertEqual(response.status_code,200)
        try:
            import json
            json.dumps(response.content)
        except Exception, e:
            raise AssertionError(e)

    def test_allowed_method(self):
        '''Test of allowed methods.'''
        response = views.all_data(MockRequest(method='POST'))
        self.assertEqual(response.status_code,405)
        response = views.all_data(MockRequest(method='PUT'))
        self.assertEqual(response.status_code,405)
        response = views.all_data(MockRequest(method='OPTIONS'))
        self.assertEqual(response.status_code,405)
        response = views.all_data(MockRequest(method='HEAD'))
        self.assertEqual(response.status_code,405)
        response = views.all_data(MockRequest(method='DELETE'))
        self.assertEqual(response.status_code,405)
        response = views.all_data(MockRequest(method='PATCH'))
        self.assertEqual(response.status_code,405)
        response = views.all_data(MockRequest(method='TRACE'))
        self.assertEqual(response.status_code,405)
        response = views.all_data(MockRequest(method=''))
        self.assertEqual(response.status_code,405)
