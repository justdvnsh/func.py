from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.isInteger import _is_integer

@_curry2
def math_mod(m, p):
    if not _is_integer(m):
        return
    if not _is_integer(p) or p < 1:
        return
    return m % p