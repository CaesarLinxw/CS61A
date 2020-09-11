def multiply(m, n):
    if n == 1:
        return m
    else:
        return m + multiply(m, n - 1)

def is_prime(n):
    def prime_helper(index):
        if index == n and n != 1:
            return True
        elif (n % index == 0 and index != 1) or n == 1:
            return False
        else:
            return prime_helper(index + 1)
    return prime_helper(1)

def count_stair_ways(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)

def count_k(n, k):
    if k == 1:
        return 1
    elif n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        i = 1
        total = 0
        while i <= k:
            total += count_k(n - i, k)
            i += 1
    return total