from copy import deepcopy

movements = {'right': (0, 1), 'left': (0, -1), 'down': (1, 0), 'up': (-1, 0),
             'down_right': (1, 1), 'down_left': (1, -1), 'up_right': (-1, 1), 'up_left': (-1, -1)}


def part_1(grid):
    previous_state = deepcopy(grid)

    while True:
        times_changed = 0
        for y_idx, y in enumerate(previous_state):
            for x_idx, x in enumerate(y):
                if grid[y_idx][x_idx] in ["L", "#"]:
                    number_filled_seats = 0
                    for move in movements.values():
                        adjacent_y_idx = y_idx + move[0]
                        adjacent_x_idx = x_idx + move[1]
                        if adjacent_y_idx < 0 or adjacent_x_idx < 0:
                            continue

                        try:
                            adjacent_seat = previous_state[y_idx + move[0]][x_idx + move[1]]
                            if adjacent_seat == "#":
                                number_filled_seats += 1
                        except IndexError:
                            pass

                    if number_filled_seats >= 4:
                        grid[y_idx][x_idx] = "L"
                    elif number_filled_seats == 0:
                        grid[y_idx][x_idx] = "#"

                    if grid[y_idx][x_idx] != previous_state[y_idx][x_idx]:
                        times_changed += 1

        if times_changed == 0:
            break
        else:
            previous_state = deepcopy(grid)

    occupied_seats = 0
    for row in grid:
        occupied_seats += row.count("#")
    print(occupied_seats)


def get_adjacent_seat_part2(grid, direction, y_idx, x_idx):
    if (((y_idx == 0) and (direction in ['up', 'up_left', 'up_right']))
            or ((y_idx == len(grid) - 1) and (direction in ['down', 'down_left', 'down_right']))
            or ((x_idx == 0) and (direction in ['left', 'up_left', 'down_left']))
            or ((x_idx == len(grid[0]) - 1) and (direction in ['right', 'up_right', 'down_right']))):
        return '.'
    else:
        y_move, x_move = movements[direction]
        if grid[y_idx + y_move][x_idx + x_move] != '.':
            return grid[y_idx + y_move][x_idx + x_move]
        else:
            return get_adjacent_seat_part2(grid, direction, y_idx + y_move, x_idx + x_move)


def part_2(grid):
    previous_state = deepcopy(grid)

    while True:
        times_changed = 0
        for y_idx, y in enumerate(previous_state):
            for x_idx, x in enumerate(y):
                if grid[y_idx][x_idx] in ["L", "#"]:
                    number_filled_seats = 0
                    for direction in movements.keys():
                        adjacent_seat = get_adjacent_seat_part2(previous_state, direction, y_idx, x_idx)
                        if adjacent_seat == "#":
                            number_filled_seats += 1

                    if number_filled_seats >= 5:
                        grid[y_idx][x_idx] = "L"
                    elif number_filled_seats == 0:
                        grid[y_idx][x_idx] = "#"

                    if grid[y_idx][x_idx] != previous_state[y_idx][x_idx]:
                        times_changed += 1

        if times_changed == 0:
            break
        else:
            previous_state = deepcopy(grid)

    occupied_seats = 0
    for row in grid:
        occupied_seats += row.count("#")
    print(occupied_seats)


with open('day11.txt') as f:
    part_one_grid = []
    for line in f.readlines():
        line = line.replace('\n', '')
        part_one_grid.append([x for x in line])

part_two_grid = deepcopy(part_one_grid)
part_1(part_one_grid)
part_2(part_two_grid)
