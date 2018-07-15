from src.funcpy.core.curry_3 import _curry3
from src.funcpy.core.checkForMethod import _check_for_method
import builtins 
import itetools

@_curry2
@_check_for_method("intersperse")
def intersperse(seperator, xs):
    return list(
        builtins.filter(
            None,
            itertools.chain.from_iterable(
                itertools.zip_longest(xs, itertools.repeat(seperator, len(xs) - 1)))))