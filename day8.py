def run_boot(lines):
    seen_indices = set()
    current_index = 0
    accumulator_value = 0
    while current_index not in seen_indices:
        try:
            current = lines[current_index]
        except IndexError:
            return accumulator_value, True
        op = current[0:3]
        direction = current[4]
        amount = int(current[5:])

        seen_indices.add(current_index)

        if op == 'acc':
            if direction == '+':
                accumulator_value += amount
            else:
                accumulator_value -= amount

            current_index += 1
        elif op == 'jmp':
            if direction == '+':
                current_index += amount
            else:
                current_index -= amount
        elif op == 'nop':
            current_index += 1

    return accumulator_value, False


def main():
    with open('day8.txt') as f:
        lines = [x.replace('\n', '') for x in f]

    print(run_boot(lines))

    all_jmp_indices = [idx for idx, x in enumerate(lines) if x.startswith('jmp')]
    all_nop_indices = [idx for idx, x in enumerate(lines) if x.startswith('nop')]
    result = [0, False]
    for jmp in all_jmp_indices:
        copy = lines.copy()
        copy[jmp] = lines[jmp].replace('jmp', 'nop')
        result = run_boot(copy)
        if result[1] is True:
            break

    if result[1] is False:
        for jmp in all_nop_indices:
            copy = lines.copy()
            copy[jmp] = lines[jmp].replace('jmp', 'nop')
            result = run_boot(copy)
            if result[1] is True:
                break

    print(result)


if __name__ == '__main__':
    main()
