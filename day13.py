with open('day13.txt') as f:
    lines = f.readlines()
    current_time = int(lines[0].replace('\n', ''))
    all_bus_ids = [x for x in lines[1].split(',')]
    in_service_bus_ids = [int(x) for x in all_bus_ids if x != "x"]

smallest_gap = in_service_bus_ids[0]
next_bus = in_service_bus_ids[0]
for bus_id in in_service_bus_ids:
    next_bus_time = (current_time // bus_id) * bus_id + bus_id
    gap = next_bus_time - current_time
    if gap < smallest_gap:
        smallest_gap = gap
        next_bus = bus_id

print(next_bus * smallest_gap)

