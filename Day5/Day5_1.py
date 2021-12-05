# https://adventofcode.com/2021/day/5

input = open("input.txt")
lines = input.readlines()

diagram = []

# no number is > 1000, so that's the dimensions of the diagram
for i in range(1000):
    y = {}

    for j in range(1000):
        y[j] = 0

    diagram.append(y)


def posToCoordinates(pos):
    pos = pos.split(",")
    x = pos[0]
    y = pos[1]

    return int(x), int(y)


for idx in range(len(lines)):
    line = lines[idx]
    line = line.split(" -> ")

    first_pos = line[0]
    second_pos = line[1]

    x1, y1 = posToCoordinates(first_pos)
    x2, y2 = posToCoordinates(second_pos)

    path = None

    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            diagram[x1][i] += 1

    if y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            diagram[i][y1] += 1

counter = 0

for i in range(len(diagram)):
    for j in diagram[i]:
        if diagram[i][j] > 1:
            counter += 1

print(counter)
