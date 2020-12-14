from collections import defaultdict


def mask_value(value_to_save, mask):
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

    new_value = new_value.replace("X", "0")

    return int(new_value, 2)


with open('day14.txt') as f:
    lines = [x.replace('\n', '') for x in f.readlines()]


mask = ""
values = defaultdict(int)

for line in lines:
    if line.startswith("mask ="):
        mask = line.split('=')[1].strip()
    else:
        value_to_save = int(line.split('=')[1].strip())
        address = int(line[line.find("[") + 1: line.find("]")])

        values[address] = mask_value(value_to_save, mask)

print(sum(values.values()))
