direction_changes = {'E': {'L': {1: 'N', 2: 'W', 3: 'S'},
                           'R': {1: 'S', 2: 'W', 3: 'N'}
                           },
                     'W': {'L': {1: 'S', 2: 'E', 3: 'N'},
                           'R': {1: 'N', 2: 'E', 3: 'S'}
                           },
                     'N': {'L': {1: 'W', 2: 'S', 3: 'E'},
                           'R': {1: 'E', 2: 'S', 3: 'W'}
                           },
                     'S': {'L': {1: 'E', 2: 'N', 3: 'W'},
                           'R': {1: 'W', 2: 'N', 3: 'E'}
                           },
                     }


def change_face(facing, left_or_right, degrees):
    amount_to_move = degrees // 90
    return direction_changes[facing][left_or_right][amount_to_move]


def part_1_move(direction, amount, facing, x_pos, y_pos):
    if direction == 'N':
        y_pos += amount
    elif direction == 'S':
        y_pos -= amount
    elif direction == 'E':
        x_pos += amount
    elif direction == 'W':
        x_pos -= amount
    elif direction == 'L':
        facing = change_face(facing, direction, amount)
    elif direction == 'R':
        facing = change_face(facing, direction, amount)
    else:  # F
        return part_1_move(facing, amount, facing, x_pos, y_pos)

    return x_pos, y_pos, facing


def part_2_move(direction, amount, facing, x_pos, y_pos, way_x, way_y):
    if direction == 'N':
        way_y += amount
    elif direction == 'S':
        way_y -= amount
    elif direction == 'E':
        way_x += amount
    elif direction == 'W':
        way_x -= amount
    elif direction == 'L':
        for _ in range(amount // 90):
            way_x, way_y = -way_y, way_x
    elif direction == 'R':
        for _ in range( amount // 90):
            way_x, way_y = way_y, -way_x
    else:  # F
        x_pos += way_x * amount
        y_pos += way_y * amount

    return x_pos, y_pos, facing, way_x, way_y


with open('day12.txt') as f:
    lines = [x.replace('\n', '') for x in f.readlines()]

x, y = 0, 0
current_facing = 'E'
for line in lines:
    x, y, current_facing = part_1_move(line[0], int(line[1:]), current_facing, x, y)

print((abs(x) + abs(y)))

x, y = 0, 0
current_facing = 'E'
waypoint_x, waypoint_y = 10, 1
for line in lines:
    x, y, current_facing, waypoint_x, waypoint_y = part_2_move(line[0], int(line[1:]), current_facing, x, y, waypoint_x, waypoint_y)

print((abs(x) + abs(y)))
