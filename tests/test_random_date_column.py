import unittest
from datetime import date
from data_gen.random_date_column import RandomDateColumn


class TestRandomDateColumn(unittest.TestCase):
    def test_random_date(self):
        d = RandomDateColumn({'name': 'd', 'randomDate': {'startDate': '2000-01-01', 'endDate': '2000-01-03'}})  # noqa ES501
        v = d.generate()
        self.assertTrue(date.fromisoformat('2000-01-01') <= date.fromisoformat(v) <= date.fromisoformat('2000-01-03'))  # noqa ES501
