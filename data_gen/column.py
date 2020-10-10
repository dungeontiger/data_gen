# for not this is here to make the expressions eval, need to pass it instead
import random


class Column:
    def __init__(self, json):
        self.name = json['name']
        self.value_expression = json['valueExpression']
        self.eval_global = {'column': self.column, 'random': random.random}

    def get_name(self):
        return self.name

    def generate(self, column_values):
        self.column_values = column_values
        # if value expression is defined, use eval to get the result
        return eval(self.value_expression, self.eval_global)

    def column(self, name):
        return self.column_values[name]
