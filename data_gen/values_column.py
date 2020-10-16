import random
from data_gen.column import Column


class ValuesColumn(Column):
    def __init__(self, json, get_value=None):
        super().__init__(json['name'], get_value)
        self.source_values = json['values']
        self.random = json.get('random', True)
        self.current_index = 0

    def generate(self):
        if self.random:
            v = random.choice(self.source_values)
        else:
            v = self.source_values[self.current_index]
            self.current_index += 1
        self.values.append(v)
        return v

    def stop(self):
        return self.current_index >= len(self.source_values)
