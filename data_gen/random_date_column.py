from datetime import date
from datetime import timedelta
import random
from data_gen.column import Column


class RandomDateColumn(Column):
    def __init__(self, json, get_value=None):
        super().__init__(json['name'], get_value)
        json_seq = json['randomDate']
        self.start_date = date.fromisoformat(json_seq['startDate'])
        self.end_date = date.fromisoformat(json_seq['endDate'])
        self.span = self.end_date - self.start_date

    def generate(self):
        d = self.start_date + timedelta(days=random.randint(0, self.span.days))
        v = d.isoformat()
        self.values.append(v)
        return v
