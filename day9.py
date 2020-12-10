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

input_length = len(lines)
minimum, maximum = None, None

for i in range(input_length):
    for j in range(input_length - 1):
        if sum(lines[i:j]) == invalid_value and not i == j - 1:
            minimum = min(lines[i:j])
            maximum = max(lines[i:j])
            break

    if minimum and maximum:
        break

print(minimum + maximum)

