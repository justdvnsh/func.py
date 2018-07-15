from src.funcpy.core.curry_1 import _curry1
from src.funcpy.core.makeFlat import _make_flat

flatten = _curry1(_make_flat(True))
