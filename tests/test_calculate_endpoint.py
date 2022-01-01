import sys
import unittest

sys.path.append('../')
from app import app


class TestCalculateEndpoint(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['debug'] = False
        self.app = app.test_client()
        self.base_url = '/calculate/'

    def test_can_calculate_storage(self):
        year = '2002'
        storage = {'20021122': 150, '20021022': 150, '20031122': 150, '20021115': 150, '20021123': 150,
                   '20020922': 150, '20031022': 150, '20021113': 150}
        url = self.base_url + '2002'
        response_text = self.app.get(url).data.decode()
        result = 0
        for i in storage:
            if i[:4] == year:
                result += storage[i]
        correct_ans = f"you lost {result}UAH in {year}"
        self.assertTrue(correct_ans in response_text)
