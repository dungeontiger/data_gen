import os
from data_gen.table import Table


class Dataset:
    def __init__(self, json):
        self.name = json['name']
        self.output_location = json['output_location']
        self.seed = json.get('seed')
        self.tables = [Table(t) for t in json['tables']]

    def generate(self):
        for t in self.tables:
            t.generate()

    def write(self):
        dir = os.path.join(self.output_location, self.name)
        try:
            os.makedirs(dir)
        except FileExistsError:
            pass
        for t in self.tables:
            t.write(dir)
