import itertools

with open('day1.txt') as f:
    lines = [int(x) for x in f.readlines()]

target_year = 2020

for numbers in itertools.combinations(lines, 2):
    if sum(numbers) == target_year:
        print(numbers[0] * numbers[1])
        break

for numbers in itertools.combinations(lines, 3):
    if sum(numbers) == target_year:
        print(numbers[0] * numbers[1] * numbers[2])
        break
