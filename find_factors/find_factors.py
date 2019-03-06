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
        factors.append(i)
    return factors


if __name__ == "__main__":
    print(find_factors(122))



