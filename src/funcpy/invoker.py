from src.funcpy.core.curry_2 import _curry2
import collections

@_curry2
def invoker(arity, method):
    def fn(*args):
        target = args[arity] if len(args) > arity else None
        if target and isinstance(getattr(target, method, None), collections.Callable):
            return getattr(target, method)(*args[:arity])
        raise TypeError("{} does not have a method named \"{}\"".format(
            target, method))
    return curry_n(arity + 1, fn)