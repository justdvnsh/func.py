from .curry_2 import _curry2
from .xcat import _xcat

@_curry2
def _xchain(f, xf):
    from ..map import map

    return map(f, _xcat(xf))
