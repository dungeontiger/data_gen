from data_gen.value_expression_column import ValueExpressionColumn
from data_gen.sequential_date_column import SequentialDateColumn
from data_gen.random_date_column import RandomDateColumn
from data_gen.values_column import ValuesColumn
from data_gen.key_column import KeyColumn
from data_gen.person_name_column import PersonNameColumn


def create_column(json, get_value=None):
    # return the correct column type based on json definition
    if json.get('valueExpression'):
        return ValueExpressionColumn(json, get_value)
    elif json.get('sequentialDate'):
        return SequentialDateColumn(json, get_value)
    elif json.get('randomDate'):
        return RandomDateColumn(json, get_value)
    elif json.get('values'):
        return ValuesColumn(json, get_value)
    elif json.get('startInt'):
        return KeyColumn(json, get_value)
    elif json.get('personName'):
        return PersonNameColumn(json, get_value)
    # TODO: Error, unknown type
    return None
