import unittest
from data_gen.value_expression_column import ValueExpressionColumn


class TestValueExpressionColumn(unittest.TestCase):
    def test_value_expression(self):
        c = ValueExpressionColumn({'name': 'measure', 'valueExpression': '10'})
        self.assertEquals(c.generate({}), 10, 'Simple python eval failed')

    def test_random_value(self):
        c = ValueExpressionColumn({'name': 'measure', 'valueExpression': 'random()'}) # noqa E50
        v = c.generate({})
        self.assertTrue(0 < v < 1, 'eval random.random() failed')

    def test_column_reference(self):
        c = ValueExpressionColumn({'name': 'measure', 'valueExpression': 'column("m1")*100'}) # noqa E50
        v = c.generate({'m1': 2})
        self.assertEqual(v, 200, 'Column reference')


if __name__ == '__main__':
    unittest.main()
