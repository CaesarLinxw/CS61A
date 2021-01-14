def height(t):
    '''
    Return the height of a tree
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    '''
    if is_leaf(t):
        return 0
    else:
        return 1 + max([height(branch) for branch in branches(t)])

def square_tree(t):
    if is_leaf(t):
        return tree(label(t) * label(t))
    else:
        return tree(label(t) * label(t),[square_tree(branch) for branch in branches(t)])

def find_path(tree, x):
    if label(tree) == x:
        return [label(tree)]
    for branch in branches(tree):
        path = find_path(branch, x)
        if path:
            return [label(tree)] + path

def add_this_many(x, el, lst):
    times = 0
    i = 0
    while i <= (len(lst) - 1):
        if lst[i] == x:
            times += 1
        i += 1 
    while times > 0:
        lst.append(el)
        times -= 1

def group_by(s, fn):
    group = [(fn(s[0]), [s[0]])]
    i = 1
    add = 0
    while i <= (len(s) - 1):
        group_index = 0
        while group_index <= (len(group) - 1):
            if group[group_index][0] == fn(s[i]):
                group[group_index][1].append(s[i])
                add = 1
                break
            group_index += 1
        if add == 0:
            group.append((fn(s[i]), [s[i]]))
        add = 0
        i += 1
    group_result = dict(group)
    return sorted(group_result.items(),key=lambda x:x[0],reverse=False)


def partition_options(total, biggest):
    if total == 0:
        return [[]]
    elif total < 0 or biggest == 0:
        return []
    else:
        with_biggest = partition_options(total - biggest, biggest)
        without_biggest = partition_options(total, biggest - 1)
        with_biggest = [[biggest] + elem for elem in with_biggest]
        return with_biggest + without_biggest

def min_elements(T, lst):
    if T == 0:
        return 0
    return 1 + min([min_elements(T - i, lst) for i in lst if T - i >= 0])
        


    


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
