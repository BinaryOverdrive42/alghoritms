# Description: 
# Author: Kireev Georgiy <metallerok@gmail.com>
# Copyright (C) 2019 by Kireev Georgiy


def greatest_common_factor(a, b):
    """
    calculate greatest common factor for a and b
    :type a: object
    :param a: int
    :param b: int
    :return: int
    """
    while not b == 0:
        reminder = a % b
        a = b
        b = reminder

    return a


if __name__ == '__main__':
    print(greatest_common_factor(8, 16))
