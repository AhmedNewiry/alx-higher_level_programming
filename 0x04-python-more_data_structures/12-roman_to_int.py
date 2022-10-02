#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    res = 0
    for char in roman_string:
        if char == 'I':
            res += 1
        elif char == 'V':
            res += 5
        elif char == 'X':
            res += 10
        elif char == 'L':
            res +=  50
        elif char == 'C':
            res +=  100
        elif char == 'D':
            res +=  500
        else:
            res +=  1000
    return res
