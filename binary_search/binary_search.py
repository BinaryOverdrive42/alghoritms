# Description: binary search
# Author: Kireev Georgiy <metallerok@gmail.com>
# Copyright (C) 2018 by Kireev Georgiy


def bsearch(array, value):
    """
    binary search
    :param array:
    :param value:
    :return: int
        searchable value index
    """
    size = len(array)
    low = 0
    high = size - 1

    while low <= high:
        mid = int((low + high) / 2)

        if value == array[mid]:
            return mid
        elif value > array[mid]:
            low = mid + 1
        elif value < array[mid]:
            high = mid - 1

    return False


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(bsearch(array, 4))

