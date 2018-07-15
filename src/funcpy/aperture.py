from src.funcpy.core.curry_2 import _curry2
from src.funcpy.core.dispatchable import _dispatchable
from src.funcpy.core.aperture import _aperture
from src.funcpy.core.xaperture import _xaperture

aperture = _curry2(_dispatchable([], _xaperture)(_aperture))