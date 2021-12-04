# https://adventofcode.com/2021/day/1

input = open("input.txt")
lines = input.readlines()

counter = 0
prev = None

for idx in range(len(lines)):
    val = int(lines[idx])

    if prev and val > prev:
        counter += 1

    prev = val

print(counter)
