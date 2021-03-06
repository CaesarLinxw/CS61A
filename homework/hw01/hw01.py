from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return h(a, b)']
    """
    if b >= 0:
        h = lambda a, b: add(a, b)
    else:
        h = lambda a, b: sub(a, b)
    return h(a, b)


def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    >>> # check that your code consists of nothing but an expression (this docstring)
    >>> # a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    return x*x + y*y + z*z - max(x, y, z)*max(x, y, z)
    
def largest_factor(x):
    """Return the largest factor of x that is smaller than x.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    n = 1
    y = 1
    while n < x:
        if (x % n == 0) & (n != 1):
            y = x / n
            if y < n:
                y = n
        if n == 1:
            pass
        n += 1
    return y
                



def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    47
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    """
    >>> result = with_if_function()
    42
    47
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func())

def cond():
    "*** YOUR CODE HERE ***"
    return False
    
def true_func():
    "*** YOUR CODE HERE ***"
    print(42)

def false_func():
    "*** YOUR CODE HERE ***"
    print(47)

def hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length.
<<<<<<< HEAD
    
    1. Pick a positive integer x as the start.
    2. If x is even, divide it by 2.
    3. If x is odd, multiply it by 3 and add 1.
    4. Continue this process until x is 1.
=======
>>>>>>> a283ee99194257e5270889f495993fffa1514d47

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
<<<<<<< HEAD
    i = 1
    while True:
        if x <= 0:
            print('You should input a positive number!')
            return None
        elif x == 1:
            print(int(x))
            return(int(i))
        elif x%2 == 0:
            print(int(x))
            x = x/2
            i += 1
        elif x%2 != 0:
            print(int(x))
            x = x*3 + 1
            i += 1
    
=======

>>>>>>> a283ee99194257e5270889f495993fffa1514d47
