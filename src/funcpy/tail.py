from src.funcpy.core.curry_1 import _curry1
from src.funcpy.core.checkForMethods import _checkForMethod

@_curry1
@_checkForMethod("tail")
def tail(xs):
    return xs[1:]