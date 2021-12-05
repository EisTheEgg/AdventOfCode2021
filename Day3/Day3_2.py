# https://adventofcode.com/2021/day/3

import math

input = open("input.txt")
lines = input.readlines()

length = len(lines[1].strip())  # gets the length of a binary number
open_values = lines

oxygen_rating = 0


def binaryToDecimal(b: str):
    return int(b, 2)  # handy thing I found on https://stackoverflow.com/questions/21765779/converting-binary-to-decimal-integer-output


for i in range(length):
    common_values = {
        "0": 0,
        "1": 0,
    }

    oxygen_most_common = None
    oxygen_highest_value = 0

    for idx in range(len(open_values)):
        line = open_values[idx]
        bit = line[i]
        common_values[str(bit)] += 1

    # get the most common bit
    if common_values["0"] == common_values["1"]:
        oxygen_most_common = "1"
    else:
        for idx, val in common_values.items():
            if val > oxygen_highest_value:
                oxygen_most_common = idx
                oxygen_highest_value = val

    oxygen_new_open_values = []

    for idx in range(len(open_values)):
        line = open_values[idx]
        bit = line[i]

        if bit == oxygen_most_common:
            oxygen_new_open_values.append(line)

    open_values = oxygen_new_open_values

    if len(open_values) == 1:
        oxygen_rating = open_values[0]


print(binaryToDecimal(oxygen_rating))
