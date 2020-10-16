import unittest
import os
from data_gen.table import Table


class TestTable(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestTable, self).__init__(*args, **kwargs)
        self.output_dir = 'tests/test_output'
        try:
            os.makedirs(self.output_dir)
        except FileExistsError:
            pass

    def test_single_column(self):
        json = {'name': 't', 'rows': 3, 'columns': [
            {'name': 'm', 'valueExpression': 'random()'}
        ]}
        t = Table(json)
        t.generate()
        self.assertTrue(len(t.get_columns()) == 1, 'Only one column')

    def test_two_column(self):
        json = {'name': 't', 'rows': 3, 'columns': [
            {'name': 'm1', 'valueExpression': 'random()'},
            {'name': 'm2', 'valueExpression': 'random()'},
        ]}
        t = Table(json)
        t.generate()
        self.assertTrue(len(t.get_columns()) == 2, 'Two columns')

    def test_column_reference(self):
        json = {'name': 't', 'rows': 3, 'columns': [
            {'name': 'm1', 'valueExpression': 'random()'},
            {'name': 'm2', 'valueExpression': 'column("m1") * 100'},
        ]}
        t = Table(json)
        t.generate()
        self.assertTrue(t.get_value('m2') == t.get_value('m1') * 100, 'Simple column ref')  # noqa ES501

    def test_write_csv(self):
        json = {'name': 't', 'rows': 3, 'columns': [
            {'name': 'm1', 'valueExpression': 'random()'},
            {'name': 'm2', 'valueExpression': 'random()'},
        ]}
        t = Table(json)
        t.generate()
        # TODO: need some asserts
        t.write(self.output_dir)
