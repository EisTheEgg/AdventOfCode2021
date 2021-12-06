# https://adventofcode.com/2021/day/6

with open("input.txt") as file:
    input = file.read()

input = input.split(",")
fish = {}

for i in range(9):
    fish[i] = 0

for i in range(len(input)):
    val = int(input[i])

    fish[val] += 1

DAYS = 256

for _ in range(DAYS):
    new_fish = {}
    new_fish_amount = 0

    # create keys for new_fish
    for i in range(9):
        new_fish[i] = 0

    for i in range(9):
        next_index = i - 1 if i - 1 >= 0 else None

        if next_index is None:
            new_fish[7] = fish.get(i)
            new_fish_amount = fish.get(i)
            new_fish[i] = 0

            continue

        current_value = fish.get(i) if type(fish.get(i)) == int else 0
        new_fish[next_index] = current_value + new_fish[i] or new_fish[i]  # new_fish[i] instead of 0 in case the new_fish[6] has changed

    new_fish[8] += new_fish_amount

    fish = new_fish

sum = 0

for i in range(9):
    sum += fish[i]

print(sum)
