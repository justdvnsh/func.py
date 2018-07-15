from src.funcpy.core.arity import _arity
from src.funcpy.core.reduce import _reduce
from src.funcpy.core.pipe import _pipe

def pipe(*args):
    from .list import tail

    if len(args) == 0:
        raise ValueError("pipe requires at least one argument")
    return _arity(_get_arity(args[0]),
                  _reduce(_pipe, args[0], tail(args)))