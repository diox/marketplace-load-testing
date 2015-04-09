import random

from loads.case import TestCase


class TestBasic(TestCase):

    def setUp(self):
        self.search_url = self._build_api_url('apps/search/')
        self.multi_search_url = self._build_api_url('multi-search/')
        self.search_url_q = '%s?%s' % (self.search_url, 'q=europa')
        self.multi_search_url_q = '%s?%s' % (self.multi_search_url, 'q=europa')

    def _build_api_url(self, path):
        return '{0}/api/v2/{1}'.format(self.server_url, path)

    def run_all(self):
        methods = [method 
                   for method in dir(self) if method.startswith('test_')
                   and callable(getattr(self, method))]
        method = random.choice(methods)
        return getattr(self, method)()

    def test_regular_search(self):
        res = self.session.get(self.search_url)
        self.assertEqual(res.status_code, 200)

    def test_multi_search(self):
        res = self.session.get(self.multi_search_url)
        self.assertEqual(res.status_code, 200)

    def test_regular_search_with_q(self):
        res = self.session.get(self.search_url_q)
        self.assertEqual(res.status_code, 200)

    def test_multi_search_with_q(self):
        res = self.session.get(self.multi_search_url_q)
        self.assertEqual(res.status_code, 200)

