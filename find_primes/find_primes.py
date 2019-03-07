import math

def find_primes(max_num):
    """
    O(n * log( log(n) ))
    """
    is_composite = [False] * (max_num + 1)
    for i in range(4, max_num, 2):
        is_composite[i] = True

    next_prime = 3
    stop_at = math.sqrt(max_num)
    while next_prime < stop_at:
        for i in range(next_prime * 2, max_num, next_prime):
            is_composite[i] = True
        next_prime += 2
        while next_prime <=  max_num \
            and (is_composite[next_prime]):
            next_prime += 2

    primes = []
    for i in range(2, max_num):
        if not is_composite[i]:
            primes.append(i)

    return primes

if __name__ == '__main__':
    print(find_primes(100))