##            15
##        /       \
##       11       12
##   /      \   /      \
##  7       5   10      2

# calculating child indexes 2i+1, 2i+2, where i is parent index
# calculating parent index floor((j-1)/2), where j is child index

import math
from copy import copy

def array_to_heap(items: list):
    heap = copy(items)
    for i, _ in enumerate(heap):
        index: int = i
        while index != 0:
            parent_index: int = math.floor((index - 1) / 2)

            if heap[index] <= heap[parent_index]:
                break

            temp = heap[index]
            heap[index] = heap[parent_index]
            heap[parent_index] = temp

            index = parent_index

    return heap


def remove_heap_top_item(items: list):
    count = len(items)
    result = items[0]

    items[0] = items[count - 1]
    

    index = 0

    while True:
        # find childs
        child_1 = 2 * index + 1
        child_2 = 2 * index + 2

        # if child index larger then tree length use parent index
        if (child_1 >= count): child_1 = index
        if (child_2 >= count): child_2 = index

        # heap complete
        if items[index] >= items[child_1] \
            and items[index] >= items[child_2]:
            break

        # swap items if heap incomplete
        if items[child_1] > items[child_2]:
            swap_child = child_1
        else:
            swap_child = child_2

        temp = items[index]
        items[index] = items[swap_child]
        items[swap_child] = temp

        index = swap_child
    
    del items[count - 1]

    return result


def heap_sort(items: list):
    heap = array_to_heap(items)
    new_array = []

    for _ in range(len(heap)):
        item = remove_heap_top_item(heap)
        new_array.append(item)

    return new_array

if __name__ == "__main__":
    items = [1, 39, 31, 23, 14, 5]
    print(heap_sort(items))
