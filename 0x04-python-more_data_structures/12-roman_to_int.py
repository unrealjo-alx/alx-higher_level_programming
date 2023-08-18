#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 100}
    sum = 0
    for i in range(len(roman_string)):
        num = romans.get(roman_string[i])
        if (
            i + 1 < len(roman_string)
            and romans[roman_string[i]] < romans[roman_string[i + 1]]
        ):
            num *= -1
        sum += num
    return sum
