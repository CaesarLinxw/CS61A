def memory(n):
    def update(func):
        nonlocal n
        n = func(n)
        return n
    return update

def nonlocalist():
    get = lambda x: "Index out of range!"
    def prepend(value):
        nonlocal get
        f = get
        def get(i):
            if i == 0:
                return value
            return f(i - 1)
        return prepend, lambda x: get(x)

def f(x):
    def helper(x, i):
        print(i)
        if i < x:
            helper(x, i+1)
    return helper(x, 1)




square = lambda x: x * x
double = lambda x: 2 * x
def memory_new(x, f):
    """Return a higher-order function that prints its
    memories.
    >>> f = memory(3, lambda x: x)
    >>> f = f(square)
    3
    >>> f = f(double)
    9
    >>> f = f(print)
    6
    >>> f = f(square)
    3
    None
    """
    def g(h):
        print(f(x))
        return memory_new(x, h)
    return g    

def announce_losses(who, last_score=0):
    """
    >>> f = announce_losses(0)
    >>> f1 = f(10, 0)
    >>> f2 = f1(1, 10) # Player 0 loses points due to swine swap
    Oh no! Player 0 just lost 9 point(s).
    >>> f3 = f2(7, 10)
    >>> f4 = f3(7, 11) # Should not announce when player 0's score does not change
    >>> f5 = f4(11, 12)
    """
    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    def say(score0, score1):
        if who == 0:
            score = score0
        elif who == 1:
            score = score1
        if score < last_score:
            print('Oh no! Player %d just lost %d point(s).'%(who, last_score - score))
        return announce_losses(who, score)
    return say

def fox_says(start, middle, end, num):
    """
    >>> fox_says('wa', 'pa', 'pow', 3)
    'wa-pa-pa-pa-pow'
    >>> fox_says('fraka', 'kaka', 'kow', 4)
    'fraka-kaka-kaka-kaka-kaka-kow'
    """
    def repeat(k):
        if k == 1:
            return middle
        else:
            return middle + '-' + repeat(k - 1)
    return start + '-' + repeat(num) + '-' + end

def primary_stress(t):
    """
    >>> word = tree("", [
    tree("w", [tree("s", [tree("min")]), tree("w", [tree("ne")])]),
    tree("s", [tree("s", [tree("so")]), tree("w", [tree("ta")])])])
    >>> primary_stress(word)
    'so'
    >>> phrase = tree("", [
    tree("s", [tree("s", [tree("law")]), tree("w", [tree("degree")])]),
    tree("w", [tree("requirement")])])
    >>> primary_stress(phrase)
    'law'
    """
    def helper(t, num_s):
        if is_leaf(t):
            return [label(t), num_s]
        if label(t) == "s":
            num_s = num_s + 1
        return max([helper(b, num_s) for b in branches(t)], key = lambda x: x[1])
    return helper(t, 0)

def subset_sum(seq, k):
    if k in seq:
        return True
    elif len(seq) == 1 and k not in seq:
        return False
    else:
        return subset_sum(seq[1:], k-seq[0]) or subset_sum(seq[1:], k)

# Tree ADT
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])