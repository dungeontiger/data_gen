import random
from data_gen.column import Column


class PersonNameColumn(Column):
    male_first = []
    female_first = []
    last = []

    def __init__(self, _json, get_value=None):
        super().__init__(_json['name'], get_value)
        self.person_name = _json['personName']
        self.sex = _json.get('sex', 'B')
        # load all the resource files on first access
        if len(PersonNameColumn.last) == 0:
            with open('data_gen/data/last_name.csv', encoding='utf-8-sig') as f:
                PersonNameColumn.last = f.read().splitlines()
            with open('data_gen/data/male_first_name.csv', encoding='utf-8-sig') as f:
                PersonNameColumn.male_first = f.read().splitlines()
            with open('data_gen/data/female_first_name.csv', encoding='utf-8-sig') as f:
                PersonNameColumn.female_first = f.read().splitlines()

    def generate(self):
        v = None
        if self.person_name == 'first':
            v = random.choice(PersonNameColumn.male_first).capitalize()
        elif self.person_name == 'last':
            v = random.choice(PersonNameColumn.last).capitalize()
        elif self.person_name == 'full':
            first_name = random.choice(PersonNameColumn.male_first).capitalize()
            last_name = random.choice(PersonNameColumn.last).capitalize()
            v = '{} {}'.format(first_name, last_name)
        self.values.append(v)
        return v

    def _get_first_name(self, sex):
        if sex == 'M':
            return random.choice(PersonNameColumn.male_first).capitalize()
        elif sex == 'F':
            return random.choice(PersonNameColumn.female_first).capitalize()
        elif sex == 'B':
            if random.random() <= 0.5:
                return random.choice(PersonNameColumn.male_first).capitalize()
            return random.choice(PersonNameColumn.female_first).capitalize()
        # TODO Error
        return None
