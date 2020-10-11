from datetime import date
from datetime import timedelta
from random import randint
from data_gen.column import Column


class SequentialDateColumn(Column):
    def __init__(self, json):
        super().__init__(json['name'])
        json_seq = json['sequentialDate']
        self.start_date = date.fromisoformat(json_seq['startDate'])
        self.end_date = date.fromisoformat(json_seq['endDate'])
        self.min_rows_per_day = json_seq.get('minRowsPerDay', 1)
        self.max_rows_per_day = json_seq.get('maxRowsPerDay', 1)
        
        self.current_value = None
        self.rows_remaining_this_day = None

    def generate(self, column_values):
        if not self.current_value:
            self.current_value = self.start_date
            rows_per_next_day = randint(self.min_rows_per_day, self.max_rows_per_day)  # noqa ES501
            self.rows_remaining_this_day = rows_per_next_day
        else:
            # do we increment the day or not?
            if self.rows_remaining_this_day <= 0:
                self.current_value = self.current_value + timedelta(days=1)
                rows_per_next_day = randint(self.min_rows_per_day, self.max_rows_per_day)  # noqa ES501
                self.rows_remaining_this_day = rows_per_next_day
        self.rows_remaining_this_day -= 1
        return self.current_value.isoformat()

    def stop(self):
        return self.current_value > self.end_date
