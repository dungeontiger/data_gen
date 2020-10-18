import os
import csv
from data_gen.column_factory import create_column


class Table:
    def __init__(self, json, get_value=None):
        self.name = json['name']
        self.rows = json['rows']
        self.columns = [create_column(c, self.get_value) for c in json['columns']]
        self._get_value = get_value

    def generate(self):
        for _ in range(self.rows):
            stop = False
            for c in self.columns:
                c.generate()
                # does this column think we should stop?
                # if any column says we should stop we will
                if not stop:
                    stop = c.stop()
            # if a column told us to stop, we will
            if stop:
                break

    def write(self, dir):
        file_name = os.path.join(dir, self.name) + '.csv'
        with open(file_name, 'w') as f:
            writer = csv.writer(f)
            header = [c.get_name() for c in self.columns]
            writer.writerow(header)
            # write out all the values of the columns
            # the length of the columns must all be the same
            for i in range(len(self.columns[0].values)):
                row = []
                for c in self.columns:
                    row.append(c.values[i])
                writer.writerow(row)

    def get_name(self):
        return self.name

    def get_value(self, column_name, table_name=None, random_value=False):
        if table_name is None or table_name == self.name:
            for c in self.columns:
                if c.get_name() == column_name:
                    return c.get_value(column_name, random_value=random_value)
            # TODO: Error, column name not found in this table
            return None
        return self._get_value(column_name, table_name, random_value=random_value)

    def get_columns(self):
        return self.columns
