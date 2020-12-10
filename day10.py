with open('day10.txt') as f:
    lines = [int(x.replace('\n', '')) for x in f]

lines.sort()
lines.insert(0, 0)
lines.append(lines[-1] + 3)
current_voltage, one_jolt_diffs, three_jolt_diffs = 0, 0, 0
for line in lines:
    diff = line - current_voltage
    current_voltage = line
    if diff == 1:
        one_jolt_diffs += 1
    elif diff == 3:
        three_jolt_diffs += 1

print(one_jolt_diffs * three_jolt_diffs)

combinations = [1] + [0] * (len(lines) - 1)

for i, line in enumerate(lines):
    for j in range(i - 3, i):
        if line - lines[j] <= 3:
            combinations[i] += combinations[j]

print(combinations[-1])
