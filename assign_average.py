"""
Author: Aidan Shannon
Program: assign_average.py


"""


def switch_average(entry):
    my_dict = {'A': 'You entered an A!',
               'B': 'You entered an B!',
               'C': 'You entered an C!',
               'D': 'You entered an D!',
               'F': 'You entered an F!'}
    for key, value in my_dict.items():
        print("{} : {}".format(key, value))
    result = my_dict.get(entry, "This is not a valid grade!")
    return result


if __name__ == '__main__':
    print(switch_average('A'))
