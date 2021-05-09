"""
Author: Masud Hussain
Course: CS162
Assignment: 6B
"""


def is_decreasing(a_list):
    list_length = len(a_list)

    if list_length == 1:
        return True
    elif a_list[0] > a_list[1]:
        a_list.pop(0)
        return is_decreasing(a_list)
    else:
        return False
