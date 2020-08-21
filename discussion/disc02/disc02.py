def curry2_lambda(h):
    return lambda x: lambda y: h(x, y)
make_adder = curry2_lambda(lambda x, y: x + y)
add_three = make_adder(3)
add_four = make_adder(4)
five = add_three(2)

def keep_ints(cond, n):
    i = 1
    while i <= n:
        if cond(i):
            print(i)
        i += 1
    return

def is_even(x):
    return x % 2 == 0

def keep_keeper(n):
    def check(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i) 
            i += 1
    return check

def print_delayed(x):
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print

def print_n(n):
    def inner_print(x):
        if n <= 0:
            print('done')
        else:
            print(x)
        return print_n(n - 1)
    return inner_print
