from .curry_2 import _curry2
from .xfBase import _XFBase
from .reduced import _reduced

@_curry2
def _xfind_last(pred, xf):
    class _XFindLast(_XFBase):
        def __init__(self, pred, xf):
            self.pred = pred
            self.xf = xf
            self.last = None

        def _transducer_init(self):
            return super().init()

        def _transducer_result(self, result):
            return self.xf._transducer_result(
                self.xf._transducer_step(result, self.last))

        def _transducer_step(self, result, input):
            if self.pred(input):
                self.last = input
            return result

    return _XFindLast(pred, xf)