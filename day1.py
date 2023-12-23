import csv


def day1part1():
    digits = []
    with open('day1input.txt') as input_file:
        reader = csv.reader(input_file, delimiter=',', quotechar='"')
        for row in reader:
            text = row[0]
            numericals = [i for i in text if i in '123456789']

            digits.append(int(numericals[0] + numericals[-1]))

    return sum(digits)

print(day1part1())