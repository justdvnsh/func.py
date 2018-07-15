from src.funcpy.core.curry_2 import _curry2
from src.funcpy.invoker import invoker
import builtins

@_curry2
def join(seperator, xs):
    return invoker(1, "join")(builtins.map(str, xs))(seperator)