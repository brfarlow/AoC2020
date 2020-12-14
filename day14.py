from collections import defaultdict
from itertools import product


def do_mask(value_to_save, mask):
    binary = bin(value_to_save).replace("0b", "")
    new_value = mask
    current = len(binary)
    for i in binary:
        if current == 1:
            if mask[-current] != "X":
                new_value = new_value[:-1] + mask[-1]
            else:
                new_value = new_value[:-1] + i
        else:
            if mask[-current] != "X":
                new_value = new_value[:-current] + mask[-current] + new_value[-current + 1:]
            else:
                new_value = new_value[:-current] + i + new_value[-current+1:]
        current -= 1

    return new_value


def mask_value_part_1(value_to_save, mask):
    new_value = do_mask(value_to_save, mask)
    new_value = new_value.replace("X", "0")

    return int(new_value, 2)


def mask_value_part_2(value_to_save, mask):
    num = bin(value_to_save)[2:].zfill(36)
    res = []
    x_count = mask.count('X')
    new_value = ''.join('{}' if v == 'X' else '1' if v == '1' else num[i] for i, v in enumerate(mask))
    for i in range(2 ** x_count):
        i = bin(i)[2:].zfill(x_count)
        res.append(new_value.format(*i))
    return [int(x, 2) for x in res]


with open('day14.txt') as f:
    lines = [x.replace('\n', '') for x in f.readlines()]


mask = ""
part_1_values = defaultdict(int)
part_2_values = defaultdict(int)

for line in lines:
    if line.startswith("mask ="):
        mask = line.split('=')[1].strip()
    else:
        value_to_save = int(line.split("=")[1].strip())
        address = int(line[line.find("[") + 1: line.find("]")])

        part_1_values[address] = mask_value_part_1(value_to_save, mask)
        for value_to_change in mask_value_part_2(address, mask):
            part_2_values[value_to_change] = int(value_to_save)

print(sum(part_1_values.values()))
print(sum(part_2_values.values()))
