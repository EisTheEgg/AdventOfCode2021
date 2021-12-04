# https://adventofcode.com/2021/day/2

input = open("input.txt")
lines = input.readlines()

properties = {
    "x": 0,  # forward
    "y": 0,  # up and down (depth)
    "aim": 0
}

directions = {
    "up": -1,
    "down": 1
}

for idx in range(len(lines)):
    val = lines[idx]
    command_name, unit = val.split()
    unit = int(unit)

    if command_name == "forward":
        properties["x"] += unit
        properties["y"] += properties["aim"] * unit
    else:
        properties["aim"] += directions[command_name] * unit

print(properties["x"] * properties["y"])
