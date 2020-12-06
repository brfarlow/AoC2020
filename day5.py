def find_number(group, start, end, lower_half_letter):
    if group[0] == lower_half_letter:
        end = (start + end) // 2
    else:
        start = ((start + end) // 2) + 1

    if start == end:
        return start
    else:
        return find_number(group[1::], start, end, lower_half_letter)


def find_seat_number(seats):
    while len(seats) > 1:
        first = seats.pop(0)
        second = seats[0]
        if second - first > 1:
            return first + 1


with open('day5.txt') as f:
    lines = [x.replace('\n', '') for x in f.readlines()]


seat_ids = []
for line in lines:
    row = find_number(line[:-3], 0, 127, 'F')
    column = find_number(line[-3:], 0, 7, 'L')
    seat_id = row * 8 + column
    seat_ids.append(seat_id)
    print(row, column, seat_id)

seat_ids.sort()

print(max(seat_ids))
print(find_seat_number(seat_ids))
