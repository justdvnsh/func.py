from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.checkForMethod import _check_for_method
from src.funcpy.indexOf import _index_of

@_curry2
@_check_for_method("index_of")
def index_of(target, xs):
    return _index_of(xs, target, 0)