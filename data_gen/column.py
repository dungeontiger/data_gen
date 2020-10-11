class Column:
    def __init__(self, name):
        self.name = name

    # returns the generated value
    def generate(self, column_values):
        return None

    # returns true of a condition in this column says it should stop
    # for example, have generated all necessary dates
    def stop(self):
        return False

    def get_name(self):
        return self.name
