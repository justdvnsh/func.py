from src.funcpy.core.curry_3 import _curry3
from src.funcpy.core.isTransformer import _is_transformer
from src.funcpy.core.reduce import _reduce
from src.funcpy.core.stepCat import _step_cat
import copy

@_curry3
def into(acc, xf, xs):
    if _is_transformer(acc):
        return _reduce(xf(acc), acc._transducer_init(), xs)
    return _reduce(xf(_step_cat(acc)), copy.copy(acc), xs)