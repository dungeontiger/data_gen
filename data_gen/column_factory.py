from data_gen.value_expression_column import ValueExpressionColumn
from data_gen.sequential_date_column import SequentialDateColumn


def create_column(json):
    # return the correct column type based on json definition
    if json.get('valueExpression'):
        return ValueExpressionColumn(json)
    elif json.get('sequentialDate'):
        return SequentialDateColumn(json)
