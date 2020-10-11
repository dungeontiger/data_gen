# for not this is here to make the expressions eval, need to pass it instead
import random

from data_gen.column import Column


class ValueExpressionColumn(Column):
    def __init__(self, json):
        super().__init__(json['name'])
        self.value_expression = json.get('valueExpression')
        self.eval_global = {'column': self.column, 'random': random.random}

    def generate(self, column_values):
        self.column_values = column_values
        # if value expression is defined, use eval to get the result
        if self.value_expression:
            return eval(self.value_expression, self.eval_global)

    def column(self, name):
        return self.column_values[name]
