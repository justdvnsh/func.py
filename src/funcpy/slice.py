from src.funcpy.core.curry_3 import _curry3
from src.funcpy.core.checkForMethod import _check_for_method

@_curry3
@_check_for_method("slice")
def slice(from_index, to_index, xs):
    return xs[from_index: to_index]