import unittest
import json
from data_gen.column_factory import create_column
from data_gen.value_expression_column import ValueExpressionColumn
from data_gen.random_date_column import RandomDateColumn
from data_gen.sequential_date_column import SequentialDateColumn
from data_gen.values_column import ValuesColumn
from data_gen.key_column import KeyColumn
from data_gen.person_name_column import PersonNameColumn
from data_gen.date_multi_column import DateMultiColumn


class TestColumnFactory(unittest.TestCase):
    def test_create_value_expression_column(self):
        with open('tests/resources/columns/value_expression_column.json') as f:  # noqa ES501
            c = create_column(json.load(f))
        self.assertIsInstance(c, ValueExpressionColumn, 'Create the correct value expression column')  # noqa ES501

    def test_create_random_date_column(self):
        with open('tests/resources/columns/random_date_column.json') as f:  # noqa ES501
            c = create_column(json.load(f))
        self.assertIsInstance(c, RandomDateColumn, 'Create the correct random date column')  # noqa ES501

    def test_create_sequential_date_column(self):
        with open('tests/resources/columns/sequential_date_column.json') as f:  # noqa ES501
            c = create_column(json.load(f))
        self.assertIsInstance(c, SequentialDateColumn, 'Create the correct sequential date column')  # noqa ES501

    def test_create_values_column(self):
        with open('tests/resources/columns/values_column.json') as f:
            c = create_column(json.load(f))
        self.assertIsInstance(c, ValuesColumn, 'Create the correct value column')  # noqa ES501

    def test_create_key_column(self):
        with open('tests/resources/columns/key_column.json') as f:
            c = create_column(json.load(f))
        self.assertIsInstance(c, KeyColumn, 'Create the correct key column')

    def test_create_person_name_column(self):
        with open('tests/resources/columns/person_name_column.json') as f:
            c = create_column(json.load(f))
        self.assertIsInstance(c, PersonNameColumn, 'Create the correct person name column')  # noqa ES501

    def test_create_date_multi_column(self):
        with open('tests/resources/columns/date_multi_column.json') as f:
            c = create_column(json.load(f))
        self.assertIsInstance(c, DateMultiColumn, 'Create the date multi column')  # noqa ES501
