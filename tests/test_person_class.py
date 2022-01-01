import sys
import unittest

sys.path.append('../')
from person import Person


class TestPersonClass(unittest.TestCase):
    def setUp(self) -> None:
        self.person = Person("misha", 2002, 'Solonka')

    def test_can_get_proper_age(self):
        test_ans = self.person.get_age()
        correct_ans = 19
        self.assertEqual(correct_ans, test_ans)

    def test_can_get_name(self):
        test_ans = self.person.get_name()
        correct_ans = 'misha'
        self.assertEqual(test_ans, correct_ans)

    def test_can_set_name(self):
        self.person.set_name("Paul")
        test_ans = self.person.get_name()
        self.assertEqual(test_ans, 'Paul')

    def test_can_get_address(self):
        test_ans = self.person.get_address()
        correct_ans = 'Solonka'
        self.assertEqual(test_ans, correct_ans)

    def test_can_set_address(self):
        self.person.set_address("lviv")
        test_ans = self.person.get_address()
        self.assertEqual(test_ans, "lviv")

    def test_can_get_if_person_is_homeless(self):
        self.person.set_address('')
        self.person.is_homeless()
        test_ans = self.person.is_homeless()
        self.assertEqual(test_ans, True)
