from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.dispatchable import _dispatchable
from src.funcpy.core.xdropWhile import _xdrop_while
import itetools

@_curry2
@_dispatchable(["drop_while"], _xdrop_while)
def drop_while(pred, xs):
    return list(itertools.dropwhile(pred, xs))