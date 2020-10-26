import unittest
import datetime
from data_gen.date_multi_column import year, month, day, date, half, quarter
from data_gen.date_multi_column import day_of_week, week, day_name
from data_gen.date_multi_column import month_name, short_day_name, short_month_name
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

    def test_first_half(self):
        d = datetime.date.fromisoformat('2020-04-09')
        v = half(d)
        self.assertEqual(v, 1, 'First half')

    def test_second_half(self):
        d = datetime.date.fromisoformat('2020-07-09')
        v = half(d)
        self.assertEqual(v, 2, 'Second half')

    def test_first_quarter(self):
        d = datetime.date.fromisoformat('2020-02-09')
        v = quarter(d)
        self.assertEqual(v, 1, 'First quarter')

    def test_second_quarter(self):
        d = datetime.date.fromisoformat('2020-04-09')
        v = quarter(d)
        self.assertEqual(v, 2, 'Second quarter')

    def test_dayOfWeek(self):
        d = datetime.date.fromisoformat('2020-10-26')
        v = day_of_week(d)
        self.assertEqual(v, 1, 'Is Monday')

    def test_day_name(self):
        d = datetime.date.fromisoformat('2020-10-26')
        v = day_name(d)
        self.assertEqual(v, 'Monday', 'Is Monday')

    def test_short_day_name(self):
        d = datetime.date.fromisoformat('2020-10-26')
        v = short_day_name(d)
        self.assertEqual(v, 'Mon', 'Is Mon')

    def test_week(self):
        d = datetime.date.fromisoformat('2020-10-26')
        v = week(d)
        self.assertEqual(v, 44, 'Is correct week')

    def test_month_name(self):
        d = datetime.date.fromisoformat('2020-10-26')
        v = month_name(d)
        self.assertEqual(v, 'October', 'Is October')

    def test_short_month_name(self):
        d = datetime.date.fromisoformat('2020-10-26')
        v = short_month_name(d)
        self.assertEqual(v, 'Oct', 'Is Oct')

    def test_generate_year(self):
        _json = {'name': 'mc', 'dateMultiColumn': {'startDate': '2020-01-01', 'endDate': '2020-04-09', 'columns': [{'name': 'd', 'type': 'year'}]}}
        mc = DateMultiColumn(_json)
        mc.generate()
        c = mc.get_columns()[0]
        self.assertEqual(c.values[0], 2020, 'Generate correct year')

    def test_quarter_prefix(self):
        _json = {'name': 'mc', 'dateMultiColumn': {'startDate': '2020-01-01', 'endDate': '2020-04-09', 'columns': [{'name': 'q', 'type': 'quarter', 'prefix': 'Q'}]}}
        mc = DateMultiColumn(_json)
        mc.generate()
        c = mc.get_columns()[0]
        self.assertEqual(c.values[0], 'Q1', 'Generate correct quarter')
