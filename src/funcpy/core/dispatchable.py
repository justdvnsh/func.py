from .isList import isList
import collections
from .curry_3 import _curry3
from isTransformer import _is_transformer

'''
Returns a function that dispatches with different strategies based on the
object in list position (last argument). If it is an array, executes [fn].
Otherwise, if it has a function with [methodname], it will execute that
function (functor case). Otherwise, if it is a transformer, uses transducer
[xf] to return a new transformer (transducer case). Otherwise, it will
default to executing [fn].
@private
@param {String} methodname property to check for a custom implementation
@param {Function} xf transducer to initialize if object is transformer
@param {Function} fn default ramda implementation
@return {Function} A function that dispatches on object in list position
'''

@_curry3
def _dispatchable(method_names, xf, fn):
    def _fn(*args):
        if len(args) == 0:
            return fn()
        obj = args[-1]
        for method_name in method_names:
            if isinstance(getattr(obj, method_name, None), collections.Callable):
                return getattr(obj, method_name)(*args[:-1])
        if _is_transformer(obj):
            transducer = xf(*args[:-1])
            return transducer(obj)
        return fn(*args)
    return _fn

