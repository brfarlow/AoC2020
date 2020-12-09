from itertools import combinations

with open('day9.txt') as f:
    lines = [int(x.replace('\n', '')) for x in f.readlines()]


preamble = 25

xmas = lines[preamble:]
invalid_value = None
for idx, value in enumerate(xmas):
    subset = lines[idx:preamble + idx]
    valid = False
    for number in subset:
        for second in subset:
            if number + second == value:
                valid = True
                break

    if not valid:
        invalid_value = value
        break

print(invalid_value)

