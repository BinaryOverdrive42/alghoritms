def mergesort(items: list, scratch: list, start: int, end: int):
    if not scratch:
        scratch = [0] * len(items)

    if start == end:
        return

    midpoint = (start + end) // 2

    mergesort(items, scratch, start, midpoint)
    mergesort(items, scratch, midpoint+1, end)

    left_index = start
    right_index = midpoint + 1
    scratch_index = left_index

    while (left_index <= midpoint) and (right_index <= end):
        if items[left_index] <= items[right_index]:
            scratch[scratch_index] = items[left_index]
            left_index += 1
        else:
            scratch[scratch_index] = items[right_index]
            right_index += 1

        scratch_index += 1

    
    for i in range(left_index, midpoint+1):
        scratch[scratch_index] = items[i]
        scratch_index += 1

    for i in range(right_index, end+1):
        scratch[scratch_index] = items[i]
        scratch_index += 1


    for i in range(start, end+1):
        items[i] = scratch[i]

if __name__ == '__main__':
    arr = [3, 2, 3, 36, 14, 5, 11, 56, 1, 3, 6, 6]
    mergesort(arr, None, 0, len(arr) - 1)

    print(arr)