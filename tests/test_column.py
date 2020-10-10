import unittest
from data_gen.column import Column


class TestColumn(unittest.TestCase):
    def test_value_expression(self):
        c = Column({'name': 'measure', 'valueExpression': '10'})
        self.assertEquals(c.generate({}), 10, 'Simple python eval failed')

    def test_random_value(self):
        c = Column({'name': 'measure', 'valueExpression': 'random()'})
        v = c.generate({})
        self.assertTrue(0 < v < 1, 'eval random.random() failed')

    def test_column_reference(self):
        c = Column({'name': 'measure', 'valueExpression': 'column("m1")*100'})
        v = c.generate({'m1': 2})
        self.assertEqual(v, 200, 'Column reference')


if __name__ == '__main__':
    unittest.main()
