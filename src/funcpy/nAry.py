from src.funcpy.core.curry_2 import _curry2

@_curry2
def n_ary(n, fn):
    if n == 0:
        return lambda: fn()
    elif n == 1:
        return lambda a0=None: fn(a0)
    elif n == 2:
        return lambda a0=None, a1=None: fn(a0, a1)
    elif n == 3:
        return lambda a0=None, a1=None, a2=None: fn(a0, a1, a2)
    elif n == 4:
        return lambda a0=None, a1=None, a2=None, a3=None: fn(a0, a1, a2, a3)
    elif n == 5:
        return lambda a0=None, a1=None, a2=None, a3=None, a4=None: fn(a0, a1, a2, a3, a4)
    elif n == 6:
        return lambda a0=None, a1=None, a2=None, a3=None, a4=None, a5=None: \
            fn(a0, a1, a2, a3, a4, a5)
    elif n == 7:
        return lambda a0=None, a1=None, a2=None, a3=None, a4=None, a5=None, a6=None: \
            fn(a0, a1, a2, a3, a4, a5, a6)
    elif n == 8:
        return lambda a0=None, a1=None, a2=None, a3=None, a4=None, a5=None, a6=None, \
            a7=None: fn(a0, a1, a2, a3, a4, a5, a6, a7)
    elif n == 9:
        return lambda a0=None, a1=None, a2=None, a3=None, a4=None, a5=None, a6=None, \
            a7=None, a8=None: fn(a0, a1, a2, a3, a4, a5, a6, a7, a8)
    elif n == 10:
        return lambda a0=None, a1=None, a2=None, a3=None, a4=None, a5=None, a6=None, \
            a7=None, a8=None, a9=None: fn(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9)
    raise ValueError(
        "First argument to nAry must be a non-negative integer no greater than ten")