import unittest
from data_gen.data_gen import main


class TestDataGen(unittest.TestCase):
    def test_simple(self):
        main('tests/resources/simple.json')
