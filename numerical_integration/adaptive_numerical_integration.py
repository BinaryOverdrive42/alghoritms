import math

def func(x):
    return math.sqrt(x)

def adaptive_numerical_integration(func, xmin, xmax, num_intervals, max_slice_error):
    # calculate primary trapezoids width
    dx = (xmax - xmin) / num_intervals

    total_area = 0
    x = xmin
    i = 1
    while i < num_intervals:
        total_area += slice_area(func, x, x + dx, max_slice_error)
        x += dx
        i += 1

    return total_area

def slice_area(func, x1, x2, max_slice_error):
    # calculate function value on start/end points
    y1 = func(x1)
    y2 = func(x2)
    xm = (x1 + x2) / 2
    ym = func(xm)

    # calculate areas squares
    area12 = (x2 - x1) * (y1 + y2) / 2
    area1m = (xm - x1) * (y1 + ym) / 2
    aream2 = (x2 - xm) * (ym + y2) / 2
    area1m2 = area1m + aream2

    error  = (area1m2 - area12) / area12

    if abs(error) < max_slice_error:
        return area1m2

    return slice_area(func, x1, xm, max_slice_error) + \
        slice_area(func, xm, x2, max_slice_error)

if __name__ == '__main__':
    print(adaptive_numerical_integration(func, 2, 100, 300, 1))