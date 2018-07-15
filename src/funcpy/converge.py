from src.funcpy.core.curry2 import _curry2
import builtins


@_curry2
def converge(after, fns):
    def call_fn(fn, args):
        return fn(*args[: _get_arity(fn)])

    @curry_n(builtins.max([_get_arity(fn) for fn in fns], default=0))
    def fn(*args):
        return after(*[call_fn(fn, args) for fn in fns])
    return fn
