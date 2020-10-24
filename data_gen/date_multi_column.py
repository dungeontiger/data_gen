import datetime
from data_gen.column import Column


class DateMultiColumn(Column):
    def __init__(self, _json, get_value=None):
        super().__init__(_json['name'], get_value)
        mc = _json['dateMultiColumn']
        self.start_date = datetime.date.fromisoformat(mc['startDate'])
        self.end_date = datetime.date.fromisoformat(mc['endDate'])
        self.cur_date = self.start_date
        self.date_columns = []
        for c in mc['columns']:
            self.date_columns.append(DateMultiColumn.DateColumn(c, get_value))

    def generate(self):
        for c in self.date_columns:
            c.generate(self.cur_date)
        self.cur_date = self.cur_date + datetime.timedelta(days=1)

    def stop(self):
        return self.cur_date > self.end_date

    def get_columns(self):
        return self.date_columns

    class DateColumn(Column):
        def __init__(self, _json, get_value=None):
            super().__init__(_json['name'], get_value)
            # the type in the JSON will match a function that returns
            # the correct information from the date
            self.type = _json['type']

        def generate(self, d):
            v = globals()[self.type](d)
            self.values.append(v)
            return v


def year(d):
    return d.year


def month(d):
    return d.month


def day(d):
    return d.day


def date(d):
    # just return the actual date
    return d.isoformat()
