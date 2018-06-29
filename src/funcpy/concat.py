import collections
from src.funcpy.core.curry_2 import _curry2

@_curry2
def concat(a, b):
    if isinstance(a, collections.Sequence):
        if isinstance(b, collections.Sequence):
            return a + b
        raise TypeError("{} is not an array".format(b))
    if hasattr(a, "concat"):
        return a.concat(b)
    raise TypeError("{} does not have a method named \"concat\"".format(a))
