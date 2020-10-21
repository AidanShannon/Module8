"""
Author: Aidan Shannon
Program: date_time.py


"""
import datetime
from datetime import timedelta


def half_birthday():
    birthday = datetime.datetime(2003, 9, 17)
    return birthday + timedelta(days=182)


if __name__ == '__main__':
    print(half_birthday())
