from data_gen.table import Table


class Dataset:
    def __init__(self, json):
        self.name = json['name']
        self.output_location = json['output_location']
        self.seed = json['seed']
        self.tables = [Table(t) for t in json['tables']]

    def generate(self):
        for t in self.tables:
            t.generate()
