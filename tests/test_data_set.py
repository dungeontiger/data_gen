import unittest
import json
from data_gen.dataset import Dataset


class TestDataset(unittest.TestCase):
    def test_simple(self):
        with open('tests/resources/simple.json') as f:
            d = Dataset(json.load(f))
        d.generate()
        # TODO: all these require asserts
        d.write()

    def test_trend(self):
        with open('tests/resources/trend.json') as f:
            d = Dataset(json.load(f))
        d.generate()
        d.write()

    def test_staff_table(self):
        with open('tests/resources/staff_table.json') as f:
            d = Dataset(json.load(f))
        d.generate()
        d.write()

    def test_referencing_another_table(self):
        with open('tests/resources/two_joined_tables.json') as f:
            d = Dataset(json.load(f))
        d.generate()
        d.write()