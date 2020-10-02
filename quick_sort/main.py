def quick_sort(items: list, start_index: int, end_index: int) -> None:
    if start_index >= end_index:
        return

    divider = items[start_index]

    # move elements that are less than the dividing array to the beginning, 
    # and those that are greater or equal to the end
    lo = start_index
    hi = end_index
    while True:
        # Look down from hi for a value < divider.
        while items[hi] >= divider:
            hi -= 1
            if (hi <= lo):
                break

        if hi <= lo:
            items[lo] = divider
            break

        # move fouded value to the lower half.
        items[lo] = items[hi]

        # Look up from lo for a value >= divider
        lo += 1
        while items[lo] < divider:
            lo += 1
            if lo >= hi:
                break
        
        if lo >= hi:
            lo = hi
            items[hi] = divider
            break
        
        # Move founded value to the upper half.
        items[hi] = items[lo]

    quick_sort(items, start_index, lo - 1)
    quick_sort(items, lo + 1, end_index)


if __name__ == '__main__':
    arr = [3, 2, 3, 36, 14, 5, 11, 56, 1, 3, 6, 6]
    quick_sort(arr, 0, len(arr) - 1)

    print(arr)
        