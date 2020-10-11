import unittest
import json
from data_gen.dataset import Dataset


class TestDataset(unittest.TestCase):
    def test_simple(self):
        with open('tests/resources/simple.json') as f:
            d = Dataset(json.load(f))
        d.generate()
        d.write()
