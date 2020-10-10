import unittest
from data_gen.table import Table


class TestTable(unittest.TestCase):
    def test_single_column(self):
        json = {'name': 't', 'rows': 3, 'columns': [
            {'name': 'm', 'valueExpression': 'random()'}
        ]}
        t = Table(json)
        t.generate()
        rows = t.get_rows()
        self.assertTrue(len(rows) == 3, 'There are three rows')
        self.assertTrue(len(rows[0]) == 1, 'Only one column')

    def test_two_column(self):
        json = {'name': 't', 'rows': 3, 'columns': [
            {'name': 'm1', 'valueExpression': 'random()'},
            {'name': 'm2', 'valueExpression': 'random()'},
        ]}
        t = Table(json)
        t.generate()
        rows = t.get_rows()
        self.assertTrue(len(rows) == 3, 'Only three rows')
        self.assertTrue(len(rows[0]) == 2, 'Two columns')

    def test_column_reference(self):
        json = {'name': 't', 'rows': 3, 'columns': [
            {'name': 'm1', 'valueExpression': 'random()'},
            {'name': 'm2', 'valueExpression': 'column("m1") * 100'},
        ]}
        t = Table(json)
        t.generate()
        rows = t.get_rows()
        self.assertTrue(rows[0][1] == rows[0][0] * 100, 'Simple column ref')


if __name__ == '__main__':
    unittest.main()
