from .curry_2 import _curry2
from .xfBase import _XFBase
from .reduced import _reduced

@_curry2
def _xfind(pred, xf):
    class _XFind(_XFBase):
        def __init__(self, pred, xf):
            self.pred = pred
            self.xf = xf
            self.found = False

        def _transducer_init(self):
            return super().init()

        def _transducer_result(self, result):
            if not self.found:
                result = self.xf._transducer_step(result, None)
            return self.xf._transducer_result(result)

        def _transducer_step(self, result, input):
            if self.pred(input):
                self.found = True
                result = _reduced(self.xf._transducer_step(result, input))
            return result

    return _XFind(pred, xf)