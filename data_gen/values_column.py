import random
from data_gen.column import Column


class ValuesColumn(Column):
    def __init__(self, json):
        super().__init__(json['name'])
        self.values = json['values']
        self.random = json.get('random', True)
        self.current_index = 0

    def generate(self, _):
        if self.random:
            v = random.choice(self.values)
        else:
            v = self.values[self.current_index]
            self.current_index += 1
        return v

    def stop(self):
        return self.current_index >= len(self.values)
