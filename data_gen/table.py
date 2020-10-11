import os
import csv
from data_gen.column_factory import create_column


class Table:
    def __init__(self, json):
        self.name = json['name']
        self.rows = json['rows']
        self.columns = [create_column(c) for c in json['columns']]
        self.generated_rows = []

    def generate(self):
        for _ in range(self.rows):
            row = []
            column_values = {}
            stop = False
            for c in self.columns:
                # need to pass the current list of values
                # this is because columns can reference other columns
                v = c.generate(column_values)
                column_values[c.get_name()] = v
                row.append(v)
                # does this column think we should stop?
                # if any column says we should stop we will
                if not stop:
                    stop = c.stop()
            self.generated_rows.append(row)
            # if a column told us to stop, we will
            if stop:
                break

    def get_rows(self):
        return self.generated_rows

    def write(self, dir):
        file_name = os.path.join(dir, self.name) + '.csv'
        with open(file_name, 'w') as f:
            writer = csv.writer(f)
            header = [c.get_name() for c in self.columns]
            writer.writerow(header)
            writer.writerows(self.generated_rows)