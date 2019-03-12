import math
def func(x):
    return math.sqrt(x)

def rectangle_numerical_integration(func, xmin, xmax, num_intervals):
    # calculate rectangle width
    dx = (xmax - xmin) / num_intervals

    # add rectangles areas
    total_area = 0
    x = xmin
    i = 1
    while i < num_intervals:
        total_area += dx * func(x)
        x += dx
        i += 1

    return total_area

if __name__ == '__main__':
    print(rectangle_numerical_integration(func, 2, 100, 300))