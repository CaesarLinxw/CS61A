def curry2_lambda(h):
    return lambda x: lambda y: h(x, y)
make_adder = curry2_lambda(lambda x, y: x + y)
add_three = make_adder(3)
add_four = make_adder(4)
five = add_three(2)