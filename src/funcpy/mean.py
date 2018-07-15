from src.funcpy.core.curry_1 import _curry1

@_curry1
def mean(xs):
    try:
        return sum(xs) / len(xs)
    except ZeroDivisionError:
        return float('nan')
