"""
Author: Aidan Shannon
Program: set_membership.py

says true or false if a value is in a set
"""


def in_set(some_set, some_value):
    pass


if __name__ == '__main__':
    my_set = set('12345')
    print(my_set)
    print("Is {} in {}? {}". format(5, my_set, in_set(my_set, str(5))))
