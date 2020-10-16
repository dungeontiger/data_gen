import random
import json
from data_gen.column import Column


class PersonNameColumn(Column):
    first = []
    last = []

    def __init__(self, _json, get_value=None):
        super().__init__(_json['name'], get_value)
        self.person_name = _json['personName']
        if len(PersonNameColumn.first) == 0:
            with open('data_gen/data/people_names.json') as f:
                names = json.load(f)
            PersonNameColumn.first = names['firstNames']
            PersonNameColumn.last = names['lastNames']

    def generate(self):
        v = None
        if self.person_name == 'first':
            v = random.choice(PersonNameColumn.first)
        elif self.person_name == 'last':
            v = random.choice(PersonNameColumn.last)
        elif self.person_name == 'full':
            first_name = random.choice(PersonNameColumn.first)
            last_name = random.choice(PersonNameColumn.last)
            v = '{} {}'.format(first_name, last_name)
        self.values.append(v)
        return v
