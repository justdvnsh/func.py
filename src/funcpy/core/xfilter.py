from .curry_2 import _curry2
from .xfBase import _XFBase


@_curry2
def _xfilter(f, xf):
    class _XFilter(_XFBase):
        def __init__(self, f, xf):
            self.xf = xf
            self.f = f

        def _transducer_init(self):
            return super().init()

        def _transducer_result(self, result):
            return super().result(result)

        def _transducer_step(self, result, input):
            if self.f(input):
                return self.xf._transducer_step(result, input)
            return result

    return _XFilter(f, xf)