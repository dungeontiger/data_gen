from data_gen.value_expression_column import ValueExpressionColumn
from data_gen.sequential_date_column import SequentialDateColumn
from data_gen.random_date_column import RandomDateColumn
from data_gen.values_column import ValuesColumn
from data_gen.key_column import KeyColumn


def create_column(json):
    # return the correct column type based on json definition
    if json.get('valueExpression'):
        return ValueExpressionColumn(json)
    elif json.get('sequentialDate'):
        return SequentialDateColumn(json)
    elif json.get('randomDate'):
        return RandomDateColumn(json)
    elif json.get('values'):
        return ValuesColumn(json)
    elif json.get('startInt'):
        return KeyColumn(json)
