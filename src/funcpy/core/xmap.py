from .curry_2 import _curry2
from .xfBase import _XFBase


@_curry2
def _xmap(f, xf):
    class _XMap(_XFBase):
        def __init__(self, f, xf):
            self.xf = xf
            self.f = f

        def _transducer_init(self):
            return super().init()

        def _transducer_result(self, result):
            return super().result(result)

        def _transducer_step(self, result, input):
            return self.xf._transducer_step(result, self.f(input))

    return _XMap(f, xf)