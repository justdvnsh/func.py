from .curry_2 import _curry2
from .xfBase import _XFBase
from .reduced import _reduced

@_curry2
def _xfind_last_index(pred, xf):
    class _XFindLastIndex(_XFBase):
        def __init__(self, pred, xf):
            self.pred = pred
            self.xf = xf
            self.idx = -1
            self.last_idx = -1

        def _transducer_init(self):
            return super().init()

        def _transducer_result(self, result):
            return self.xf._transducer_result(
                self.xf._transducer_step(result, self.last_idx))

        def _transducer_step(self, result, input):
            self.idx += 1
            if self.pred(input):
                self.last_idx = self.idx
            return result

    return _XFindLastIndex(pred, xf)