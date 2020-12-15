def find_number_spoken(spoken_numbers, last_turn):
    last_number_spoken = 0
    for i in range(len(spoken_numbers) + 1, last_turn):
        if last_number_spoken in spoken_numbers:
            temp = spoken_numbers[last_number_spoken]
            spoken_numbers[last_number_spoken] = i
            last_number_spoken = i - temp
        else:
            spoken_numbers[last_number_spoken] = i
            last_number_spoken = 0
    return last_number_spoken


puzzle_input = [0, 14, 1, 3, 7, 9]
already_spoken = {puzzle_input[i]: i + 1 for i in range(len(puzzle_input))}
print(find_number_spoken(already_spoken, 2020))

already_spoken = {puzzle_input[i]: i + 1 for i in range(len(puzzle_input))}
print(find_number_spoken(already_spoken, 30000000))
