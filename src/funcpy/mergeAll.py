from src.funcpy.core.curry_1 import _curry1
import functools

@_curry1
def merge_all(xs):
    return functools.reduce(
        lambda acc, item: acc.update(item) or acc, xs, {})