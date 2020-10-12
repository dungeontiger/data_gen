from data_gen.column import Column


class KeyColumn(Column):
    def __init__(self, json):
        super().__init__(json['name'])
        self.start_int = json['startInt']
        self.end_int = json['endInt']
        self.prefix = json.get('prefix')
        self.loop = json.get('loop', False)
        self.current_int = self.start_int

    def generate(self, _):
        if self.prefix:
            v = '{}{}'.format(self.prefix, self.current_int)
        else:
            v = self.current_int
        self.current_int += 1
        if self.loop and self.current_int > self.end_int:
            self.current_int = self.start_int
        return v

    def stop(self):
        return self.current_int > self.end_int
