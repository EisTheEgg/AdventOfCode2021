# https://adventofcode.com/2021/day/1

input = open("input.txt")
lines = input.readlines()

counter = 0
prev = None

window = []

for idx in range(len(lines)):
    val = int(lines[idx])

    if len(window) == 3:
        window.pop(0)

    window.append(val)

    if len(window) == 3:
        x = sum(window)
        print(x)

        if prev and x > prev:
            counter += 1

        prev = x

print(counter)
