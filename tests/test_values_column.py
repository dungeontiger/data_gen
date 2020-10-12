import unittest
from data_gen.values_column import ValuesColumn


class TestValuesColumns(unittest.TestCase):
    def test_default_random(self):
        c = ValuesColumn({'name': 'column', 'values': ['A', 'B', 'C']})
        v = c.generate({})
        self.assertIn(v, ['A', 'B', 'C'])

    def test_not_random(self):
        c = ValuesColumn({'name': 'column', 'random': False, 'values': ['A', 'B', 'C']})  # noqa ES501
        v = c.generate({})
        self.assertEqual(v, 'A')
        self.assertFalse(c.stop())
        v = c.generate({})
        self.assertEqual(v, 'B')
        self.assertFalse(c.stop())
        v = c.generate({})
        self.assertEqual(v, 'C')
        self.assertTrue(c.stop())
