from src.funcpy.core.curry_1 import _curry1
from src.funcpy.converge import converge

@_curry1
def juxt(fns):
    return converge(lambda *args: list(args), fns)