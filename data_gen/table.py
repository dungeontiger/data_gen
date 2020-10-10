from data_gen.column import Column


class Table:
    def __init__(self, json):
        self.name = json['name']
        self.rows = json['rows']
        self.columns = [Column(c) for c in json['columns']]
        self.generated_rows = []

    def generate(self):
        for _ in range(self.rows):
            row = []
            column_values = {}
            for c in self.columns:
                # need to pass the current list of values
                # this is because columns can reference other columns
                v = c.generate(column_values)
                column_values[c.get_name()] = v
                row.append(v)
            self.generated_rows.append(row)

    def get_rows(self):
        return self.generated_rows
