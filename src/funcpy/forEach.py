from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.checkForMethod import _check_for_method


@_curry2
@_check_for_method("for_each")
def for_each(fn, xs):
    [fn(item) for item in xs]
    return xs