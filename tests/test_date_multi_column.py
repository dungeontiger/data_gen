import unittest
import datetime
from data_gen.date_multi_column import year, month, day, date
from data_gen.date_multi_column import DateMultiColumn


class TestDateMultiColumn(unittest.TestCase):
    def test_year(self):
        d = datetime.date.fromisoformat('2020-04-09')
        v = year(d)
        self.assertEqual(v, 2020, 'Extracted year')

    def test_month(self):
        d = datetime.date.fromisoformat('2020-04-09')
        v = month(d)
        self.assertEqual(v, 4, 'Extracted month')

    def test_day(self):
        d = datetime.date.fromisoformat('2020-04-09')
        v = day(d)
        self.assertEqual(v, 9, 'Extracted day')

    def test_date(self):
        d = datetime.date.fromisoformat('2020-04-09')
        v = date(d)
        self.assertEqual(v, '2020-04-09', 'Original date')

    def test_generate_year(self):
        _json = {'name': 'mc', 'startDate': '2020-01-01', 'endDate': '2020-04-09', 'columns': [{'name': 'd', 'type': 'year'}]}
        mc = DateMultiColumn(_json)
        mc.generate()
        c = mc.get_date_columns()[0]
        self.assertEqual(c.values[0], 2020, 'Generate correct year')
