# for not this is here to make the expressions eval, need to pass it instead
import random
from data_gen.column import Column


class ValueExpressionColumn(Column):
    days_per_month = 30
    days_per_quarter = 90
    days_per_year = 365

    def __init__(self, json):
        super().__init__(json['name'])
        self.value_expression = json['valueExpression']
        self.eval_global = {'column': self.column,
                            'random': random.random,
                            'uniform': random.uniform,
                            'randint': random.randint,
                            'normalvariate': random.normalvariate}
        self.trends = json.get('trends')
        if self.trends:
            self.trend_date_ref = self.trends['dateColumn']
            self.daily = self.trends.get('daily')
            self.monthly = self.trends.get('monthly')
            self.quarterly = self.trends.get('quarterly')
            self.yearly = self.trends.get('yearly')
            self.last_date = None
            self.accum_trend = 0

    def generate(self, column_values):
        self.column_values = column_values
        v = eval(self.value_expression, self.eval_global)
        v = self._apply_trend(v)
        return v

    def _apply_trend(self, value):
        v = value
        if self.trends:
            if self.last_date != self.column_values[self.trend_date_ref]:
                if self.daily:
                    daily = eval(self.daily, self.eval_global)
                if self.monthly:
                    monthly = eval(self.monthly, self.eval_global)
                    daily = monthly / ValueExpressionColumn.days_per_month
                if self.quarterly:
                    quarterly = eval(self.quarterly, self.eval_global)
                    daily = quarterly / ValueExpressionColumn.days_per_quarter
                if self.yearly:
                    yearly = eval(self.yearly, self.eval_global)
                    daily = yearly / ValueExpressionColumn.days_per_year
                self.accum_trend += daily
                v += v * self.accum_trend
                self.last_date = self.column_values[self.trend_date_ref]
        return v

    def column(self, name):
        # this method can be called from the value expression
        return self.column_values[name]
