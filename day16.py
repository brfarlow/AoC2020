from functools import reduce
from operator import mul


def part2(fields, my_ticket, valid_tickets):
    possible_fields = [set() for _ in range(len(my_ticket))]
    fields_order = ['' for _ in range(len(fields))]

    for i in range(len(my_ticket)):
        for field, (min1, max1, min2, max2) in fields.items():
            if all(min1 <= ticket[i] <= max1 or min2 <= ticket[i] <= max2 for ticket in valid_tickets):
                possible_fields[i].add(field)

    while any(not field for field in fields_order):
        pos = next(pos for pos, possible_values in enumerate(possible_fields) if len(possible_values) == 1)
        value = possible_fields[pos].pop()
        for possible_values in possible_fields:
            if value in possible_values:
                possible_values.remove(value)
        fields_order[pos] = value

    return reduce(mul, [my_ticket[pos] for pos, field in enumerate(fields_order) if field.startswith('departure')], 1)


def validate_ticket(ticket, fields_and_rules):
    invalid = []
    for value in ticket:
        valid_at_least_once = True
        if not any(min1 <= value <= max1 or min2 <= value <= max2 for
                   min1, max1, min2, max2 in fields_and_rules.values()):
            valid_at_least_once = False
        if not valid_at_least_once:
            invalid.append(value)

    return invalid


def main():
    with open('day16.txt') as f:
        fields_and_rules = dict()
        my_ticket = []
        other_tickets = []
        lines = f.readlines()

        part = 1
        for line in lines:
            if line == '\n':
                part += 1
                continue
            elif 'ticket' in line:
                continue

            line = line.replace('\n', '')
            if part == 1:
                field, tmp = line.split(':')
                rules = []
                tmp = [x.strip() for x in tmp.split('or')]
                for i in tmp:
                    for j in i.split('-'):
                        rules.append(int(j))
                fields_and_rules[field] = rules
            elif part == 2:
                my_ticket = [int(x) for x in line.split(',')]
            elif part == 3:
                other_tickets.append([int(x) for x in line.split(',')])

    valid_tickets = []
    invalid_value_sum = 0

    for ticket in other_tickets:
        invalid_values = validate_ticket(ticket, fields_and_rules)
        if len(invalid_values):
            invalid_value_sum += sum(invalid_values)
        else:
            valid_tickets.append(ticket)

    print(invalid_value_sum)
    print(part2(fields_and_rules, my_ticket, valid_tickets))


if __name__ == "__main__":
    main()
