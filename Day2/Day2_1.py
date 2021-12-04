# https://adventofcode.com/2021/day/2

input = open("input.txt")
lines = input.readlines()

axes = {
    "x": 0,  # forward
    "y": 0  # up and down (depth)
}

commands = {
    "forward": ["x", 1],
    "up": ["y", -1],
    "down": ["y", 1]
}

for idx in range(len(lines)):
    val = lines[idx]
    command_name, unit = val.split()
    unit = int(unit)

    axis, direction = commands[command_name]
    axes[axis] += direction * unit

product = axes["x"] * axes["y"]
print(product)
