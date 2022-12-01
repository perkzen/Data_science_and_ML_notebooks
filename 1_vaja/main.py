from series import Series
from spreadsheet import Spreadsheet


def main():
    s1 = Series("height", [1.5, 1.7, 1.4, 1.3, 1.9])
    s2 = Series("width", [5, 7, 4, 3, 9, 6])
    s3 = Series("age", [15, 11, 10, 12])

    print(s1.count())
    print(s2.count())
    print(s3.count())

    s2.delete(2)
    s3.add(13, index=1)

    print(s1.count())
    print(s2.count())
    print(s3.count())

    spreadsheet = Spreadsheet([s1, s2, s3])
    print(spreadsheet.count())

    spreadsheet.add_row([1.6, 8, 14])
    spreadsheet.add_column(Series("weight", [34, 21, 56, 43, 51, 28]))

    print(spreadsheet.count())
    print(spreadsheet.average())


if __name__ == "__main__":
    main()
