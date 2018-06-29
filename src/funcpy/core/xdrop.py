from .curry_2 import _curry2
from .xfBase import _XFBase

@_curry2
def _xdrop(n, xf):
    class _XDrop(_XFBase):
        def __init__(self, n, xf):
            self.xf = xf
            self.n = n

        def _transducer_init(self):
            return super().init()

        def _transducer_result(self, result):
            return super().result(result)

        def _transducer_step(self, result, input):
            if self.n > 0:
                self.n -= 1
                return result
            return self.xf._transducer_step(result, input)

    return _XDrop(n, xf)