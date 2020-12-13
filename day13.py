with open('day13.txt') as f:
    lines = f.readlines()
    current_time = int(lines[0])
    all_bus_ids = [x for x in lines[1].split(',')]
    in_service_bus_ids = [(idx, int(bus)) for idx, bus in enumerate(all_bus_ids) if bus != 'x']

smallest_gap = in_service_bus_ids[0][1]
next_bus = in_service_bus_ids[0][1]
for _, bus_id in in_service_bus_ids:
    next_bus_time = (current_time // bus_id) * bus_id + bus_id
    gap = next_bus_time - current_time
    if gap < smallest_gap:
        smallest_gap = gap
        next_bus = bus_id

print(next_bus * smallest_gap)

time = 0
period = in_service_bus_ids[0][1]
offset = None
for idx, bus in in_service_bus_ids:
    offset = None
    while True:
        if (time + idx) % bus == 0:
            if offset is None:
                offset = time
            else:
                period = time - offset
                break

        time += period

print(offset)
