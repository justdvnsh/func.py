from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.keys import _keys as keys

@_curry2
def omit(names, obj):
    result = {}
    for key in obj.keys():
        if not _contains(key, names):
            result[key] = obj[key]
    return result