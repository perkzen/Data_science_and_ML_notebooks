class Series:

    def __init__(self, name, values):
        if values is None:
            values = []
        self.name = name
        self.values = values

    def count(self):
        return len(self.values)

    def average(self):
        return sum(self.values) / len(self.values)

    def head(self, x=5):
        return self.values[0:x]

    def tail(self, x=5):
        return self.values[-x: -1]

    def add(self, value, index=None):
        if index is None:
            self.values.append(value)
            return
        self.values.insert(index, value)

    def delete(self, index):
        self.values.pop(index)
