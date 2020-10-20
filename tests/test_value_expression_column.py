import unittest
import random
from data_gen.value_expression_column import ValueExpressionColumn


class TestValueExpressionColumn(unittest.TestCase):
    def test_value_expression(self):
        c = ValueExpressionColumn({'name': 'measure', 'valueExpression': '10'})
        self.assertEqual(c.generate(), 10, 'Simple python eval failed')

    def test_random_value(self):
        random.seed(345)
        c = ValueExpressionColumn({'name': 'measure', 'valueExpression': 'random()'}) # noqa E501
        v = c.generate()
        self.assertAlmostEqual(v, 0.7706, places=3, msg='eval random() failed') # noqa ES501

    def test_column_reference(self):
        def get_ref(s, c, t):
            return 2
        c = ValueExpressionColumn({'name': 'measure', 'valueExpression': 'column("m1")*100'}, get_ref) # noqa E501
        v = c.generate()
        self.assertEqual(v, 200, 'Column reference')
