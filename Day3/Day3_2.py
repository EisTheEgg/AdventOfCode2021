# https://adventofcode.com/2021/day/3

import math

input = open("input.txt")
lines = input.readlines()

length = len(lines[1].strip())  # gets the length of a binary number
oxygen_open_values = lines
co2_open_values = lines


def oxygenIsMostCommon(val, current):
    return val > current


def co2IsMostCommon(val, current):
    return val < current


rating_info = {
    "oxygen": {
        "open_values": lines,
        "primary": "1",
        "rating": None,
        "current": 0,
        "most_common_determinator": oxygenIsMostCommon,
    },

    "co2": {
        "open_values": lines,
        "primary": "0",
        "rating": None,
        "current": math.inf,
        "most_common_determinator": co2IsMostCommon,
    }
}


def binaryToDecimal(b: str):
    return int(b, 2)  # handy thing I found on https://stackoverflow.com/questions/21765779/converting-binary-to-decimal-integer-output


for i in range(length):
    for key, info in rating_info.items():
        common_values = {
            "0": 0,
            "1": 0,
        }

        new_open_values = []

        most_common = None
        highest_value = info["current"]

        for idx in range(len(info["open_values"])):
            line = info["open_values"][idx]
            bit = line[i]
            common_values[str(bit)] += 1

        # get the most common bit
        if common_values["0"] == common_values["1"]:
            most_common = info["primary"]
        else:
            for idx, val in common_values.items():
                if info["most_common_determinator"](val, highest_value):
                    most_common = idx
                    highest_value = val

        for idx in range(len(info["open_values"])):
            line = info["open_values"][idx]
            bit = line[i]

            if bit == most_common:
                new_open_values.append(line)

        info["open_values"] = new_open_values

        if len(info["open_values"]) == 1:
            info["rating"] = info["open_values"][0]


print(binaryToDecimal(rating_info["oxygen"]["rating"]) * binaryToDecimal(rating_info["co2"]["rating"]))
