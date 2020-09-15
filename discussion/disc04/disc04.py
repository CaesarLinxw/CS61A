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

def even_weighted(s):
    return [x * s.index(x) for x in s if s.index(x) % 2 == 0]

def max_product(s):
    gap = 2
    max_gap = len(s) - 1
    final_product = 1
    while gap <= max_gap:
        index = 0
        product = 1
        new_list = s[::gap]
        while index <= len(new_list) - 1:
            product *= new_list[index]
            index += 1
        if product > final_product:
            final_product = product
        gap += 1
    return final_product

def check_hole_number(n):
    n = [int(x) for x in str(n)]
    if n[int((len(n) - 1) / 2) : int((len(n) - 1) / 2) + 1] < n[int((len(n) - 1) / 2) - 1 : int((len(n) - 1) / 2)] and n[int((len(n) - 1) / 2) : int((len(n) - 1) / 2) + 1] < n[int((len(n) - 1) / 2) + 1 : int((len(n) - 1) / 2) + 2]:
        return True
    return False

def check_mountain_number(n):
    def helper(x, is_increasing):
        if x // 10 == 0:
            return True
        elif is_increasing and (x % 10) < (x // 10) % 10:
            return helper(x // 10, is_increasing)
        return (x % 10) > (x // 10) % 10 and helper(x // 10, False)
    return helper(n, True)