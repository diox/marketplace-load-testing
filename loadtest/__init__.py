import random
from collections import Counter

from loads.case import TestCase


class TestBasic(TestCase):

    def setUp(self):
        self.search_url = self._build_api_url('apps/search/')
        self.multi_search_url = self._build_api_url('multi-search/')
        self.search_url_q = '%s?%s' % (self.search_url, 'q=europa')
        self.multi_search_url_q = '%s?%s' % (self.multi_search_url, 'q=europa')

    def _build_api_url(self, path):
        return '{0}/api/v2/{1}'.format(self.server_url, path)

    def _assert_2OO_and_objects(self, res):
        self.assertEqual(res.status_code, 200)
        data = res.json()
        assert len(data['objects'])
        assert data['meta']
        return data

    def run_all(self):
        methods = [method 
                   for method in dir(self) if method.startswith('test_')
                   and callable(getattr(self, method))]
        method = random.choice(methods)
        return getattr(self, method)()

    def test_regular_search(self):
        res = self.session.get(self.search_url)
        self._assert_2OO_and_objects(res)

    def test_multi_search(self):
        res = self.session.get(self.multi_search_url)
        data = self._assert_2OO_and_objects(res)
        counts = Counter([c['doc_type'] for c in data['objects']])
        assert counts['webapp']
        assert counts['website']

    def test_regular_search_with_q(self):
        res = self.session.get(self.search_url_q)
        self._assert_2OO_and_objects(res)

    def test_multi_search_with_q(self):
        res = self.session.get(self.multi_search_url_q)
        data = self._assert_2OO_and_objects(res)
        counts = Counter([c['doc_type'] for c in data['objects']])
        assert counts['webapp']
        assert counts['website']
