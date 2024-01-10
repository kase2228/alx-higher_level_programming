#!/usr/bin/python3
""" Roman to Integer test file
"""
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_value = 0

    for i in range(len(roman_string)):
        if i + 1 < len(roman_string) and roman_to_int[roman_string[i]] < roman_to_int[roman_string[i + 1]]:
            int_value -= roman_to_int[roman_string[i]]
        else:
            int_value += roman_to_int[roman_string[i]]

    return int_value
