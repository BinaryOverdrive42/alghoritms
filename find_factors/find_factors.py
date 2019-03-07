import math

def find_factors(num):
    """
    O(N)
    """
    factors = []
    i = 2
    while i < num:
        while num % i == 0:
            factors.append(i)
            num = num / i
        i += 1
    if num > 1:
        factors.append(num)
    return factors

def fast_find_factors(num):
    """
    O(sqrt(n))
    """
    factors = []
    # check divisibility by 2
    while num % 2 == 0:
        factors.append(2)
        num = num / 2
    
    # search odd multipliers
    i = 3
    max_factor = math.sqrt(num)
    while i <= max_factor:
        while num % i == 0:
            factors.append(i)
            num = num / i

            max_factor = math.sqrt(num)
        i += 2
    if num > 1:
        factors.append(num)
    return factors

if __name__ == "__main__":
    print(find_factors(12221))
    print(fast_find_factors(12221))



