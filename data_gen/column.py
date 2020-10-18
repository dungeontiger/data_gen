import random


class Column:
    def __init__(self, name, get_value):
        self.name = name
        self.values = []
        self._get_value = get_value

    # returns the generated value
    def generate(self):
        return None

    # returns true of a condition in this column says it should stop
    # for example, have generated all necessary dates
    def stop(self):
        return False

    def get_name(self):
        return self.name

    def get_value(self, column_name, table_name=None, random_value=False):
        if table_name is None and column_name == self.name:
            if random_value:
                return random.choice(self.values)
            return self.values[-1]
        return self._get_value(column_name, table_name, random_value)
