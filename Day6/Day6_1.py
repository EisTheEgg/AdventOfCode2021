# https://adventofcode.com/2021/day/6

input = None

with open("input.txt") as file:
    input = file.read()

fish = input.split(",")

for i in range(len(fish)):
    fish[i] = int(fish[i])

DAYS = 80

for _ in range(DAYS):
    for i in range(len(fish)):
        fish[i] -= 1

        if fish[i] < 0:
            fish[i] = 6
            fish.append(8)

print(len(fish))
