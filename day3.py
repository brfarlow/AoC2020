def move(pattern, x_slope, y_slope):
    x_length = len(lines[0])
    y_length = len(lines)

    x_position = 0
    y_position = 0

    trees_hit = 0

    while y_position <= y_length:
        if pattern[y_position % y_length][x_position % x_length] == "#":
            trees_hit += 1

        x_position += x_slope
        y_position += y_slope

    return trees_hit


with open('day3.txt') as f:
    lines = [x.replace('\n', '') for x in f.readlines()]


print(move(lines, 3, 1))

part_2_total = move(lines, 1, 1) * move(lines, 3, 1) * move(lines, 5, 1) * move(lines, 7, 1) * move(lines, 1, 2)
print(part_2_total)
