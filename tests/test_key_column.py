import unittest
from data_gen.key_column import KeyColumn


class TestKeyColumn(unittest.TestCase):
    def test_years(self):
        c = KeyColumn({'name': 'years', 'startInt': 2000, 'endInt': 2002})
        v = c.generate({})
        self.assertEqual(v, 2000)
        self.assertFalse(c.stop())
        v = c.generate({})
        v = c.generate({})
        self.assertEqual(v, 2002)
        self.assertTrue(c.stop())

    def test_prefix(self):
        c = KeyColumn({'name': 'years', 'startInt': 1, 'endInt': 10, 'prefix': 'ID_'})  # noqa ES501
        v = c.generate({})
        self.assertEqual(v, 'ID_1')

    def test_loop(self):
        c = KeyColumn({'name': 'months', 'startInt': 1, 'endInt': 3, 'loop': True})  # noqa ES501
        v = c.generate({})
        self.assertEqual(v, 1)
        c.generate({})
        c.generate({})
        self.assertFalse(c.stop())
        v = c.generate({})
        self.assertEqual(v, 1)
