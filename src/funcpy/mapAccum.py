from src.funcpy.core.curry_3 import _curry3

@_curry3
def map_accum(fn, acc, xs):
    result = []
    tuple_ = [acc]
    for item in xs:
        tuple_ = fn(tuple_[0], item)
        result.append(tuple_[1])
    return [tuple_[0], result]