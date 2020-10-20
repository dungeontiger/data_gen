# for not this is here to make the expressions eval, need to pass it instead
import random
from datetime import date
from data_gen.column import Column


class ValueExpressionColumn(Column):
    days_per_month = 30
    days_per_quarter = 90
    days_per_year = 365

    def __init__(self, json, get_value=None):
        super().__init__(json['name'], get_value)
        self.value_expression = json['valueExpression']
        self.eval_global = {'column': self.column,
                            'random': random.random,
                            'uniform': random.uniform,
                            'randint': random.randint,
                            'normalvariate': random.normalvariate,
                            'get_value': self.get_value}
        self.trends = json.get('trends')
        if self.trends:
            self.trend_date_ref = self.trends['dateColumn']
            self.daily = self.trends.get('daily')
            self.monthly = self.trends.get('monthly')
            self.quarterly = self.trends.get('quarterly')
            self.yearly = self.trends.get('yearly')
            self.trend_start_date = self.trends.get('startDate')
            if self.trend_start_date:
                self.trend_start_date = date.fromisoformat(self.trend_start_date)
            self.trend_end_date = self.trends.get('endDate')
            if self.trend_end_date:
                self.trend_end_date = date.fromisoformat(self.trend_end_date)
            self.last_date = None
            self.accum_trend = None

    def generate(self):
        v = eval(self.value_expression, self.eval_global)
        v = self._apply_trend(v)
        self.values.append(v)
        return v

    def _apply_trend(self, value):
        # there is some complex logic here
        # first, if there is no trend defined there is nothing to do
        # if the current date is greater than the start date we need to apply a trend
        # if the current date is not the same as the previous one (different day) modify the trend value by the daily amount
        v = value
        if self.trends:
            d = date.fromisoformat(self.get_value(self.trend_date_ref))
            if (self.trend_start_date is None or d >= self.trend_start_date) and (self.trend_end_date is None or d <= self.trend_end_date):
                if self.trend_start_date != d:
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
                    if self.accum_trend:
                        self.accum_trend += daily
                    else:
                        self.accum_trend = daily
            if self.accum_trend:
                v = v + v * self.accum_trend
        return v

    # TODO: better more generic name
    def column(self, name):
        # this method can be called from the value expression
        return self.get_value(name)
