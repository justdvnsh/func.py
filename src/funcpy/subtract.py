from src.funcpy.core.curry_2 import _curry2
from fastnumbers import fast_real

@_curry2
def subtract(a, b):
    try:
        return fast_real(a) - fast_real(b)
    except TypeError:
        return float('nan')