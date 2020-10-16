import os
import random
from data_gen.table import Table


class Dataset:
    def __init__(self, json):
        self.name = json['name']
        self.output_location = json['output_location']
        self.seed = json.get('seed')
        random.seed(self.seed)
        self.tables = [Table(t, self.get_value) for t in json['tables']]

    def generate(self):
        for t in self.tables:
            t.generate()
        # TODO accumlate errors and return them
        return []

    def write(self):
        dir = os.path.join(self.output_location, self.name)
        try:
            os.makedirs(dir)
        except FileExistsError:
            pass
        for t in self.tables:
            t.write(dir)

    def get_value(self, column_name, table_name):
        for t in self.tables:
            if t.get_name() == table_name:
                return t.get_value(column_name)
        # TODO: error, could not find table
        return None
