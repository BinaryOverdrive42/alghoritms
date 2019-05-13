import math
def func(x):
    return math.sqrt(x)

def trapezoid_numerical_integration(func, xmin, xmax, num_intervals):
    # calculate trapezoid width
    dx = (xmax - xmin) / num_intervals

    # add trapezoid areas
    total_area = 0
    x = xmin
    i = 1
    while i < num_intervals:
        total_area += dx * (func(x) + func(x+dx)) / 2
        i += 1

    return total_area

if __name__ == '__main__':
    print(trapezoid_numerical_integration(func, 2, 100, 300))