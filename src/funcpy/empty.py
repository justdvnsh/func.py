from src.funcpy.core.curry_1 import _curry1
import collections
from src.funcpy.core.isList import isList
from src.funcpy.core.isString import _is_string
from src.funcpy.core.isObject import _is_object

@_curry1
def empty(x):
    if isinstance(getattr(x, "empty", None), collections.Callable):
        return x.empty()
    elif isinstance(x, collections.Callable):
        return lambda _: None
    elif isList(x):
        return []
    elif _is_string(x):
        return ""
    elif _is_object(x):
        return {}