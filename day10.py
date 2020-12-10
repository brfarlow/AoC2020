with open('day10.txt') as f:
    lines = [int(x.replace('\n', '')) for x in f]

lines.sort()
lines.append(lines[-1] + 3)
current_voltage = 0
one_jolt_diffs = 0
three_jolt_diffs = 0
for line in lines:
    diff = line - current_voltage
    current_voltage = line
    if diff == 1:
        one_jolt_diffs += 1
    elif diff == 3:
        three_jolt_diffs += 1
    else:
        print(diff, line)

print(one_jolt_diffs * three_jolt_diffs)
