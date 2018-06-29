from .curry_2 import _curry2
from .xfBase import _XFBase
from .reduced import _reduced

@_curry2
def _xall(f, xf):
    class _Xall(_XFBase):
        def __init__(self, f, xf):
            self.xf = xf
            self.f = f
            self.all = True

        def _transducer_init(self):
            return super().init()

        def _transducer_result(self, result):
            if self.all:
                result = self.xf._transducer_step(result, True)
            return super().result(result)

        def _transducer_step(self, result, input):
            if not self.f(input):
                self.all = False
                result = _reduced(self.xf._transducer_step(result, False))
            return result

    return _Xall(f, xf)