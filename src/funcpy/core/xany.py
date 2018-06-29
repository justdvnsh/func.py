from .curry_2 import _curry2
from .xfBase import _XFBase
from .reduced import _reduced

@_curry2
def _xany(f, xf):
    class _Xany(_XFBase):
        def __init__(self, f, xf):
            self.xf = xf
            self.f = f
            self.any = False

        def _transducer_init(self):
            return super().init()

        def _transducer_result(self, result):
            if not self.any:
                result = self.xf._transducer_step(result, False)
            return super().result(result)

        def _transducer_step(self, result, input):
            if self.f(input):
                self.any = True
                result = _reduced(self.xf._transducer_step(result, True))
            return result

    return _Xany(f, xf)