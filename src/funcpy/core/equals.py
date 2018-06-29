import collections
import builtins
from .keys import _keys
from .identical import _identical
from .has import _has

def _equals(a, b, stack_a=[], stack_b=[]):
    if _identical(a, b):
        return True
    if type(a) != type(b):
        return False
    if a is None or b is None:
        return False
    if isinstance(getattr(a, "equals", None), collections.Callable) or \
            isinstance(getattr(b, "equals", None), collections.Callable):
        return isinstance(getattr(a, "equals", None), collections.Callable) and \
            a.equals(b) and \
            isinstance(getattr(b, "equals", None), collections.Callable) and \
            b.equals(a)
    if isinstance(a, (int, float, str)):
        if not (type(a) == type(b) and _identical(a, b)):
            return False
    if isinstance(a, collections.Callable) and isinstance(b, collections.Callable):
        return id(a) == id(b)
    keys_a = _keys(a)
    if len(keys_a) != len(_keys(b)):
        return False
    for item_a, item_b in builtins.reversed(builtins.list(builtins.zip(stack_a, stack_b))):
        if id(item_a) == id(a):
            return id(item_b) == id(b)
    stack_a.append(a)
    stack_b.append(b)
    for key in keys_a:
        if not (_has(key, b) and _equals(b[key], a[key], stack_a, stack_b)):
            return False
    stack_a.pop()
    stack_b.pop()
    return True