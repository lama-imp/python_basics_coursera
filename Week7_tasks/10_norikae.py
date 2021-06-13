stops = list(map(int, input().split()))
first_bus = stops[:2]
second_bus = stops[2:]
first_bus.sort()
second_bus.sort()
first_bus_stops = set()
second_bus_stops = set()
for i in range(first_bus[0], first_bus[1] + 1):
    first_bus_stops.add(i)
for i in range(second_bus[0], second_bus[1] + 1):
    second_bus_stops.add(i)
print(len(first_bus_stops & second_bus_stops))
