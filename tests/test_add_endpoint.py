import sys
import unittest
sys.path.append ('../')
from app import app


class TestAddEndpoint(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['debug'] = False
        self.app = app.test_client()
        self.base_url = '/add/'

    def test_add_with_one_elem(self):
        date = 20021122
        money = 150
        url = self.base_url + '/'.join(str(x) for x in (date, money))
        response_text = self.app.get(url).data.decode()
        correct_answer = "saved to storage"
        self.assertTrue(correct_answer in response_text)

    def test_with_incorrect_date(self):
        date = 20021133  # incorrect day
        date_2 = "string"
        money = 150
        url = self.base_url + '/'.join(str(x) for x in (date, money))
        url_2 = self.base_url + '/'.join(str(x) for x in (date_2, money))
        with self.assertRaises(ValueError):
            self.app.get(url)
        with self.assertRaises(ValueError):
            self.app.get(url_2)






