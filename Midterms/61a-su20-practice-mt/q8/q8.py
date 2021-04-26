def compound(f):
    h = lambda x: x
    def g(x):
        nonlocal h; old_h = h
        h = lambda x: f(old_h(x))
        return h(x)
    return g