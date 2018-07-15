from src.funcpy.core.curry_1 import _curry1

@_curry1
def always(val):
    return lambda *_: val