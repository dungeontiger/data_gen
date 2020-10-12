import unittest
from data_gen.person_name_column import PersonNameColumn


class TestPersonNameColumn(unittest.TestCase):
    def test_first(self):
        # TODO need a seed to test this properly
        c = PersonNameColumn({'name': 'n', 'personName': 'first'})
        self.assertIsNotNone(c.generate({}))

    def test_last(self):
        # TODO need a seed to test this properly
        c = PersonNameColumn({'name': 'n', 'personName': 'last'})
        self.assertIsNotNone(c.generate({}))

    def test_full(self):
        # TODO need a seed to test this properly
        c = PersonNameColumn({'name': 'n', 'personName': 'full'})
        self.assertIsNotNone(c.generate({}))
