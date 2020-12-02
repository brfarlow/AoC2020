class PasswordPolicy:
    def __init__(self, lowest, highest, letter):
        self.lowest = lowest
        self.highest = highest
        self.letter = letter


def get_policy(string):
    lowest, remainder = string.split('-')
    highest, letter = remainder.split(' ')
    return PasswordPolicy(int(lowest), int(highest), letter)


with open('day2.txt') as f:
    lines = [line.split(':') for line in f.readlines()]

part_1_valid = 0
part_2_valid = 0

for policy_string, password in lines:
    password = password.replace('\n', '').strip()
    policy = get_policy(policy_string)
    times_seen = password.count(policy.letter)
    if policy.lowest <= times_seen <= policy.highest:
        part_1_valid += 1

    if password[policy.lowest - 1] == policy.letter and password[policy.highest - 1] != policy.letter:
        part_2_valid += 1
    elif password[policy.lowest - 1] != policy.letter and password[policy.highest - 1] == policy.letter:
        part_2_valid += 1

print(part_1_valid)
print(part_2_valid)
