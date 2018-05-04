'''
Possible source of test data: http://clagnut.com/blog/2380/

'''

import json

from unittest import TestCase

from chalice.config import Config
from chalice.local import LocalGateway

from app import app


class TestApp(TestCase):

    def setUp(self):
        self.gw = LocalGateway(app, Config())

    def test_pangram_good(self):

        response = self.gw.handle_request(method='GET',
                                          path='/pangram/thequickbrownfoxjumpsoverthelazydog',
                                          headers={},
                                          body='')

        assert response['statusCode'] == 200
        assert json.loads(response['body']) == dict(pangram=True)

    def test_pangram_bad(self):

        response = self.gw.handle_request(method='GET',
                                          path='/pangram/thequickbrownfoxjumpsoverthelazy',
                                          headers={},
                                          body='')

        assert response['statusCode'] == 200
        assert json.loads(response['body']) == dict(pangram=False)

    def test_pangram_mixed_input(self):

        response = self.gw.handle_request(method='GET',
                                          path='/pangram/the1quick2brown3fox4jumps5over6the7lazy8dog9',
                                          headers={},
                                          body='')

        assert response['statusCode'] == 200
        assert json.loads(response['body']) == dict(pangram=True)

    def test_pangram_mixed_input_extended(self):

        response = self.gw.handle_request(method='GET',
                                          path='/pangram/the1qu%40ick2bro%24wn3fox4jum%25ps5ov%5Eer6the7la%2Azy8dog9',
                                          headers={},
                                          body='')

        assert response['statusCode'] == 200
        assert json.loads(response['body']) == dict(pangram=True)

    def test_pangram2_good(self):

        response = self.gw.handle_request(method='GET',
                                          path='/pangram2/thequickbrownfoxjumpsoverthelazydog',
                                          headers={},
                                          body='')

        assert response['statusCode'] == 200
        assert json.loads(response['body']) == dict(pangram=True)

    def test_pangram2_bad(self):

        response = self.gw.handle_request(method='GET',
                                          path='/pangram2/thequickbrownfoxjumpsoverthelazy',
                                          headers={},
                                          body='')

        assert response['statusCode'] == 200
        assert json.loads(response['body']) == dict(pangram=False)

    def test_pangram2_mixed_input(self):

        response = self.gw.handle_request(method='GET',
                                          path='/pangram2/the1quick2brown3fox4jumps5over6the7lazy8dog9',
                                          headers={},
                                          body='')

        assert response['statusCode'] == 200
        assert json.loads(response['body']) == dict(pangram=True)

    def test_pangram2_mixed_input_extended(self):

        response = self.gw.handle_request(method='GET',
                                          path='/pangram2/the1qu%40ick2bro%24wn3fox4jum%25ps5ov%5Eer6the7la%2Azy8dog9',
                                          headers={},
                                          body='')

        assert response['statusCode'] == 200
        assert json.loads(response['body']) == dict(pangram=True)
