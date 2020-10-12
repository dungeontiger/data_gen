import random
import json
from data_gen.column import Column


class PersonNameColumn(Column):
    first = []
    last = []

    def __init__(self, _json):
        super().__init__(_json['name'])
        self.person_name = _json['personName']
        if len(PersonNameColumn.first) == 0:
            with open('data_gen/data/people_names.json') as f:
                names = json.load(f)
            PersonNameColumn.first = names['firstNames']
            PersonNameColumn.last = names['lastNames']

    def generate(self, _):
        if self.person_name == 'first':
            return random.choice(PersonNameColumn.first)
        elif self.person_name == 'last':
            return random.choice(PersonNameColumn.last)
        elif self.person_name == 'full':
            first_name = random.choice(PersonNameColumn.first)
            last_name = random.choice(PersonNameColumn.last)
            return '{} {}'.format(first_name, last_name)
