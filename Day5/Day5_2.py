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
    x = pos[1]
    y = pos[0]

    return int(x), int(y)


def sign(x):
    return 0 if x == 0 else 1 if x > 0 else -1


for idx in range(len(lines)):
    line = lines[idx]
    line = line.split(" -> ")

    first_pos = line[0]
    second_pos = line[1]

    x1, y1 = posToCoordinates(first_pos)
    x2, y2 = posToCoordinates(second_pos)

    path = None
    x = x1
    y = y1
    diagram[x][y] += 1

    x_difference = abs(x1 - x2)
    y_difference = abs(y1 - y2)
    difference = x_difference if x_difference > y_difference else y_difference

    for i in range(difference):
        x += sign(x2 - x1)
        y += sign(y2 - y1)

        diagram[x][y] += 1

counter = 0

for i in range(len(diagram)):
    row = ""

    for j in diagram[i]:
        row += str(diagram[i][j])
        if diagram[i][j] > 1:
            counter += 1

print(counter)
