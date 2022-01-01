import sys
import unittest

sys.path.append('../')
from app import app


class TetsAddGet(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['debug'] = False
        self.app = app.test_client()
        self.base_url = '/add_get/'

    def test_can_work_with_integer(self):
        query = "?num=1&num=4&num=3&num=5"
        url = self.base_url + query
        responce_text = self.app.get(url).data.decode()
        correct_answer = "sum: 13</br>mult: 60"
        self.assertEqual(responce_text, correct_answer)
