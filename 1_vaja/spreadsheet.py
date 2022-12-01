class Spreadsheet:

    def __init__(self, columns):
        if columns is None:
            columns = []
        self.columns = columns

    def count(self):
        return [max(len(row.values) for row in self.columns), len(self.columns)]

    def average(self):
        values = {}
        for col in self.columns:
            values[col.name] = col.average()
        return values

    def head(self, x=5):
        return self.columns[0:x]

    def tail(self, x=5):
        return self.columns[-x: -1]

    def add_row(self, row, index=None):
        for i in range(len(self.columns)):
            self.columns[i].add(row[i], index)

    def add_column(self, column, index=None):
        if index is None:
            self.columns.append(column)
            return
        self.columns.insert(index, column)
