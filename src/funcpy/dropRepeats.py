from src.funcpy.core.curry_1 import _curry1
from src.funcpy.core.dispatchable import _dispatchable
from src.funcpy.core.xdropRepeatsWith import _xdrop_repeats_with
from src.funcpy.core.equals import _equals

drop_repeats = _curry1(_dispatchable(
    [], _xdrop_repeats_with(_equals), drop_repeats_with(_equals)))