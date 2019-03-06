# Description: square of value throw bsearch
# Author: Kireev Georgiy <metallerok@gmail.com>
# Copyright (C) 2018 by Kireev Georgiy


def square_bsearch(a):
    """
    :param a: float
    :return: float
    """
    epsilon = 0.01
    low = 0.0
    high = a
    guess = (high + low) / 2.0

    while abs((pow(guess, 2)) - a) >= epsilon:

        if pow(guess, 2) < a:
            low = guess
        else:
            high = guess

        guess = (high + low) / 2.0

    return guess


if __name__ == '__main__':
    print(square_bsearch(41.2321432423))
