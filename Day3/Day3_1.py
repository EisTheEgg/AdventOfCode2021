# https://adventofcode.com/2021/day/3

import math

input = open("input.txt")
lines = input.readlines()

length = len(lines[1].strip())  # gets the length of a binary number

gamma_rate = ""
epsilon_rate = ""


def binaryToDecimal(b: str):
    return int(b, 2)  # handy thing I found on https://stackoverflow.com/questions/21765779/converting-binary-to-decimal-integer-output


for i in range(length):
    common_values = {
        "0": 0,
        "1": 0,
    }
    most_common_value = None
    highest_value = 0

    least_common_value = None
    lowest_value = math.inf

    for idx in range(len(lines)):
        line = lines[idx]
        bit = line[i]
        common_values[str(bit)] += 1

    for idx, val in common_values.items():
        if val > highest_value:
            most_common_value = idx
            highest_value = val

        if val < lowest_value:
            least_common_value = idx
            lowest_value = val

    gamma_rate += most_common_value
    epsilon_rate += least_common_value

print(binaryToDecimal(gamma_rate) * binaryToDecimal(epsilon_rate))
