#!/usr/bin/python3
def no_c(my_string):
    original_string = my_string
    letters_to_remove = "cC"
    translation_table = str.maketrans("", "", letters_to_remove)
    modified_string = original_string.translate(translation_table)
    return modified_string
