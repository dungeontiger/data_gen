import unittest
from data_gen.sequential_date_column import SequentialDateColumn


class TestSequentialDateColumn(unittest.TestCase):
    def test_simple_date(self):
        c = SequentialDateColumn({'name': 'd', 'sequentialDate': {'startDate': '1990-01-01', 'endDate': '1990-02-01'}})  # noqa E50
        self.assertEqual(c.generate(), '1990-01-01', 'Simple sequential date')  # noqa E50

    def test_one_step(self):
        c = SequentialDateColumn({'name': 'd', 'sequentialDate': {'startDate': '1990-01-01', 'endDate': '1990-02-01'}})  # noqa E50
        # this will be the start date
        c.generate()
        self.assertEqual(c.generate(), '1990-01-02', 'Adding one day works')  # noqa E50

    def test_stop(self):
        c = SequentialDateColumn({'name': 'd', 'sequentialDate': {'startDate': '1990-01-01', 'endDate': '1990-01-05'}})  # noqa E50
        for _ in range(5):
            c.generate()
            self.assertFalse(c.stop(), 'Not stopping yet')
        # generate once more and it should stop
        c.generate()
        self.assertTrue(c.stop())

    def test_two_rows_per_date(self):
        c = SequentialDateColumn({'name': 'd', 'sequentialDate': {'startDate': '1990-01-01', 'endDate': '1990-01-05', 'minRowsPerDay': 2, 'maxRowsPerDay': 2}})  # noqa E50
        v1 = c.generate()
        v2 = c.generate()
        self.assertEqual(v1, v2, 'Two rows per date on the first date')
        v1 = c.generate()
        v2 = c.generate()
        self.assertEqual(v1, v2, 'Two rows per date')
