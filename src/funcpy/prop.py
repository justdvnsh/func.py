from src.funcpy.core.curry_2 import _curry2


@_curry2
def prop(p, obj):
    return obj[p]
