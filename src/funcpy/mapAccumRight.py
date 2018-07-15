from src.funcpy.core.curry_3 import _curry3

@_curry3
def map_accum_right(fn, acc, xs):
    result = []
    tuple_ = [acc]
    for item in reversed(xs):
        tuple_ = fn(item, tuple_[0])
        result.append(tuple_[1])
    return [list(reversed(result)), tuple_[0]]