from datetime import date
from datetime import timedelta
from data_gen.column import Column


class SequentialDateColumn(Column):
    def __init__(self, json):
        super().__init__(json['name'])
        json_seq = json['sequentialDate']
        self.start_date = date.fromisoformat(json_seq['startDate'])
        self.end_date = date.fromisoformat(json_seq['endDate'])
        self.current_value = None

    def generate(self, column_values):
        if not self.current_value:
            self.current_value = self.start_date
        else:
            self.current_value = self.current_value + timedelta(days=1)
        return self.current_value.isoformat()

    def stop(self):
        return self.current_value > self.end_date

