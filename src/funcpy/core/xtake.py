from .curry_2 import _curry2
from .xfBase import _XFBase

from .reduced import _reduced

@_curry2
def _xtake(n, xf):
    class _XTake(_XFBase):
        def __init__(self, n, xf):
            self.xf = xf
            self.n = n
            self.i = 0

        def _transducer_init(self):
            return super().init()

        def _transducer_result(self, result):
            return super().result(result)

        def _transducer_step(self, result, input):
            self.i += 1
            ret = result if self.n == 0 else self.xf._transducer_step(
                result, input)
            return _reduced(ret) if self.n >= 0 and self.i >= self.n else ret

    return _XTake(n, xf)